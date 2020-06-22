import re
import json
import subprocess
import sys
import time
import argparse
from datetime import datetime

cmd = ("kubectl logs %s request-benchmark --tail=16 -n default")


def with_retries(retries=5, delay=2):
    def decor(f):
        def wrapper(*args, **kwargs):
            print("retires = {0}, delay ={1}".format(retries, delay))
            for i in range(retries):
                try:
                    return f(*args, **kwargs)
                except Exception as e:
                    print(f.__name__, args, "failed:", e)
                time.sleep(delay)
            print("Giving up!")
        return wrapper
    return decor


def get_cmd_output(cmd):
    ps = subprocess.Popen(
        cmd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    output = ps.communicate()[0]
    if isinstance(output, bytes):
        output = output.decode("utf-8")
    print(output)
    return output


def duration_in_ms(duration):
    if ":" in duration:
        duration = duration.split(":")[-1].strip()

    if "µs" in duration:
        duration = float(duration.strip("µs")) / 1000
    else:
        duration = float(duration.strip("ms"))
    return duration



def get_min_max(durations, **benchmark_args):
    ignore_requests = benchmark_args.pop("ignore_requests", [])
    duration_ = duration_in_ms(durations[0])
    min = duration_
    max = duration_
    tot = 0
    sum_ = 0
    duration_arr = []
    duration_arr_sum = 0
    for duration in durations:
        duration = duration_in_ms(duration)
        tot = tot + duration
        if min > duration:
            min = duration

        if max < duration:
            max = duration
        duration_arr_sum = duration_arr_sum + duration
        duration_arr.append(duration)

    duration_mean = duration_arr_sum/len(durations)

    sum_sdsqr = 0
    for duration_ele in duration_arr:
        sum_sdsqr = sum_sdsqr + (duration_mean - duration_ele)**2

    if len(ignore_requests) != 0:
        avg = float(tot/len(durations))
        return min, max, avg, tot, float(sum_sdsqr/len(durations))
    return min, max, float(sum_sdsqr/len(durations))

def get_current_service_count(**kwargs):
    svc_regexp = kwargs.get("svc_regexp", "target-svc")
    namespace = kwargs.get("namespace", "default")
    target_svc_count_cmd = f"kubectl get svc -n {namespace} | grep {svc_regexp} | wc -l"
    return int(get_cmd_output(target_svc_count_cmd).strip())


def get_headers(headerdata):
    headers_data = {}
    regex_ = re.compile(
        r"(Connection:\[.*\])\s+"
        "(Content-Length:\[\d*\])\s+"
        "(Content-Type:\[.*\])\s+"
        "(Date:\[.*\])\s+"
        "(Server:\[.*\])\s+"
        "(X-Mesh-Request-Id:\[.*\])")

    headers = regex_.search(headerdata)
    for i in range(1, 7):
        data_ = headers.group(i)
        data_ = data_.split(":[")
        try:
            headers_data[data_[0]] = data_[1].strip("]")
        except Exception as exc:
            print(exc)
    return headers_data


@with_retries(retries=10, delay=2)
def get_latest_benchmark(*args, **benchmark_args):
    ignore_requests = benchmark_args.get("ignore_requests", [])
    latest_logs = get_cmd_output(args[0])
    output_list = latest_logs.split("\n")
    durations = output_list[:9]
    durations.append(output_list[-3])
    filtered_durations = []
    if len(ignore_requests) != 0:
        for index, element in enumerate(durations):
            if index not in ignore_requests:
                filtered_durations.append(element)
    req_data = "".join(output_list[x] for x in range(9, 13))
    req_date, req_data = req_data.split("Body debug:")
    req_date = req_date.strip()
    req_data = req_data.strip()

    headers_data = get_headers(output_list[-4])

    all_durations = {}
    temp = output_list[-2].split(" ")

    avg_ = duration_in_ms(temp[1])
    tot_ = duration_in_ms(temp[3])
    if len(ignore_requests)!= 0:
        min_, max_, avg_, tot_, var = get_min_max(filtered_durations, **benchmark_args)
    else:
        min_, max_, var = get_min_max(durations)

    all_durations["minimum"] = min_
    all_durations["maximum"] = max_
    all_durations["average"] = avg_
    all_durations["total"] = tot_
    all_durations["variance"] = var
    
    
    retval = dict(datetime=req_date,
                req=json.loads(req_data)['req'],
                headers=headers_data,
                duration=durations,
                stats=all_durations)
    if len(ignore_requests)!= 0:
        retval["filtered_durations"] = filtered_durations
    return retval 

def get_benchmark_json(log_command, **benchmark_args):
    services_now = benchmark_args.get("services_now", None)
    op_json = "response_%s.json" % time.strftime("%Y%m%d%H%M%S")
    if not services_now:
        services_now = get_current_service_count()
    benchmark_data = get_latest_benchmark(log_command, **benchmark_args)
    benchmark_data["services"] = services_now
    with open(op_json, "w") as fd:
        fd.write(json.dumps(benchmark_data))
    return op_json


if __name__ == "__main__":
    command_line = ''.join(
        sys.argv[i] + ' ' for i in range(len(sys.argv)))

    parser = argparse.ArgumentParser(
        description='Script to check pod logs.')

    parser.add_argument(
        "-p",
        "--pod-name",
        help='Pod to check the log.',
        required=True)

    parser.add_argument(
        "-c",
        "--logs-checkpoint",
        help="after how many service, check the logs",
        required=False)

    parser.add_argument(
        "-i",
        "--ignore-requests",
        help="ignore the first API call response time",
        required=False,
        default=False)

    parser.add_argument(
        "-a",
        "--append-to-list",
        help="append all result to list",
        required=False,
        default=False)

    parser.add_argument(
        "-w",
        "--wait-to-query",
        help="wait to check logs",
        required=False,
        default=None)

    parser.add_argument(
        "-s",
        "--services-deploying",
        help="no of services being deployed",
        required=False,
        default=None)

    parser.add_argument(
        "-m",
        "--minutes-to-monitor",
        help="minutes to monitor the benchmark",
        required=False,
        default=30)

    args = parser.parse_args()

    log_command = cmd % args.pod_name
    services_deploying = int(args.services_deploying)
    logs_checkpoint = int(args.logs_checkpoint)

    ignore_requests = args.ignore_requests
    if ignore_requests:
        ignore_requests = [ int(i_r) for i_r in ignore_requests.split(",")]
    else:
        ignore_requests = []
    benchmark_args = {"ignore_requests": ignore_requests}
    op_json = get_benchmark_json(log_command, **benchmark_args)
    if args.append_to_list:
        json_list = [op_json]

    if not args.wait_to_query:
        service_count = get_current_service_count()
        while service_count <= services_deploying:
            if service_count % logs_checkpoint == 0:
                benchmark_args["services_now"] = service_count
                op_json = get_benchmark_json(log_command, **benchmark_args)
                if args.append_to_list:
                    json_list.append(op_json)
            if service_count == services_deploying:
                break
            time.sleep(10)
            service_count = get_current_service_count()
    else:
        wait_to_query = int(args.wait_to_query)
        t1 = datetime.now()
        while (datetime.now() - t1).seconds <= int(args.minutes_to_monitor) * 60:
            op_json = get_benchmark_json(log_command, **benchmark_args)
            if args.append_to_list:
                json_list.append(op_json)
            time.sleep(wait_to_query)

    if args.append_to_list:
        with open("consolidated_%s.json" % time.strftime("%Y%m%d%H%M%S"), "w") as fd:
            fd.write(json.dumps([json.loads(open(json_file).read()) for json_file in json_list]))
