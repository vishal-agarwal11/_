import requests
import time

def with_retries(attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(attempts):
                print("Calling %s, attempt %s" % (func.__name__, i))
                try:
                    return func(*args, **kwargs)
                except Exception as exc:
                    print("Failed with exception %s" % exc)
                time.sleep(delay)
            print("Failed to execute in %s attempts!" % attempts)
        return wrapper
    return decorator


@with_retries()
def get_api(api):
    res = requests.get(api)
    return res.status_code
    


resp = get_api("sds")
print(resp)