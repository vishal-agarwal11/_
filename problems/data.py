import re
import json
import subprocess
import time 
import argparse

cmd = ("kubectl logs %s request-benchmark --tail=16 -n default")

def with_retries(retries=5, delay=0):
    def decor(f):
        def wrapper(*args):
            print("retires = {0}, delay ={1}".format(retries, delay))
            for i in range(retries):
                try: 
                    return f(*args)
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
    if isinstance(output,bytes):
        output = output.decode("utf-8")
    return output

def duration_in_ms(duration):
    if ":" in duration:
        duration = duration.split(":")[-1].strip()

    if "µs" in duration:
        duration = float(duration.strip("µs"))/1000
    else:
        duration = float(duration.strip("ms"))
    return duration

def get_min_max(durations):
    duration_ = duration_in_ms(durations[0]) 
    min = duration_
    max = duration_
    for duration in durations:
        duration = duration_in_ms(duration)

        if min > duration:
            min = duration

        if max < duration:
            max = duration

    return min,max

def get_current_service_count(**kwargs):
    svc_regexp = kwargs.get("svc_regexp", "target-svc")
    namespace = kwargs.get("namespace", "default")
    target_svc_count_cmd = f"kubectl get svc -n {namespace} | grep {svc_regexp} | wc -l"
    return int(get_cmd_output(target_svc_count_cmd))


def get_headers(headerdata):
    headers_data = {}
    regex_ = re.compile(r"(Connection:\[.*\])\s+"
                         "(Content-Length:\[\d*\])\s+"
                         "(Content-Type:\[.*\])\s+"
                         "(Date:\[.*\])\s+"
                         "(Server:\[.*\])\s+"
                         "(X-Mesh-Request-Id:\[.*\])")
    headers = regex_.search(headerdata)
    for i in range(1,7):
        data_ = headers.group(i)
        data_ = data_.split(":[")
        try:
            headers_data[data_[0]] = data_[1].strip("]")
        except:
            pass
    return headers_data 

@with_retries(retries=5, delay=1)
def get_latest_benchmark():
    latest_logs = get_cmd_output(cmd)
    output_list = latest_logs.split("\n")
    
    durations = output_list[:9]
    durations.append(output_list[-3])
    req_data = "".join(output_list[x] for x in range(9, 13))
    req_date, req_data = req_data.split("Body debug:")
    req_date = req_date.strip()
    req_data = req_data.strip()

    headers_data = get_headers(output_list[-4])

    all_durations = {"min":None,"max":None,"avg":None,'tot':None}
    temp = output_list[-2].split(" ")
    all_durations["avg"] = duration_in_ms(temp[1])
    all_durations["tot"] = duration_in_ms(temp[3])
    all_durations["min"], all_durations["max"] = get_min_max(durations)
    
    response_json = {}
    response_json['datetime'] = req_date
    response_json["req"] = json.loads(req_data)['req']
    response_json["headers"] = headers_data
    response_json["duration"] = durations
    response_json["stats"] = all_durations
    return response_json




if __name__ == "__main__":
    command_line = ''.join(
            sys.argv[i]+' ' for i in range(len(sys.argv)))

    parser = argparse.ArgumentParser(
            description=("Script to check pod logs."))

    parser.add_argument(
            '-pod',
            '--pod-name',
            help='Pod to check the log.',
            required=True)


    op_json = "response_%s.json" % time.strftime("%Y%m%d%H%M%S") 
    with open(op_json, "w") as fd:
        latest_benchmark_data = get_latest_benchmark()
        latest_benchmark_data["services"] = get_current_service_count()
        fd.write(json.dumps(latest_benchmark_data))

    service_count = get_current_service_count()
    while service_count < 500:
        if service_count % 99 == 0:
            latest_benchmark_data = get_latest_benchmark()
            latest_benchmark_data["services"] = service_count
            ts_now = time.strftime("%Y%m%d%H%M%S")
            with open(f"response_{ts_now}.json", "w") as fd:
                fd.write(json.dumps(latest_benchmark_data))
                 
        service_count = get_current_service_count()
