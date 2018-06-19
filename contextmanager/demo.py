import subprocess
import threading
from contextlib import contextmanager
import time

ping_info = []
def worker(_url,event):
    print "starting continious ping to %s" %_url
    while not event.isSet():
        ping_output = subprocess.Popen(["ping", "-c10", "-q", _url], stdout=subprocess.PIPE).stdout.read()
        ping_info.append(ping_output)
        print ping_output

@contextmanager
def writterpinger(url):
    event = threading.Event()
    w = threading.Thread(target=worker, args=(url,event))
    w.start()
    yield

    event.set()
    w.join()


with writterpinger('www.google.com') as ping_res:
    print "\nsleeping for 20 seconds"
    time.sleep(20)
    # place any job in place of sleep, which
    # is required to be performed during ping.
    print "Done waiting 20 seconds"

print ping_info
