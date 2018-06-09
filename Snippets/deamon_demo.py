import daemon
import time


# the DeamonContext manager handle the deamon in a better way
# we need not to provide a '&' to start the process and run in
# background 'python deamon.py' is sufficient and the code will
# start executing and we will get the prompt

def do_something():
    while True:
        with open("/tmp/current_time.txt", "a") as f:
            f.write("The time is now " + time.ctime()+"\n")
        time.sleep(2)

def run():
    with daemon.DaemonContext():
        do_something()

if __name__ == "__main__":
    run()
