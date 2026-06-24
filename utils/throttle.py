import time
import threading


class GlobalThrottle:

    _lock = threading.Lock()
    _last_call = 0

    @staticmethod
    def wait(min_interval=1.0):

        with GlobalThrottle._lock:

            now = time.time()

            diff = now - GlobalThrottle._last_call

            if diff < min_interval:

                time.sleep(min_interval - diff)

            GlobalThrottle._last_call = time.time()