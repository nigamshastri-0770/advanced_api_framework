# File: utils/retry_helper.py

import time

class RetryHelper:
    @staticmethod
    def execute(func, attempts=3, wait=2):
        """Execute func with retries.

        Retries the callable `func` up to `attempts` times, waiting `wait`
        seconds between attempts. If the result has a `status_code` and it
        is less than 500 it is returned early. Any exception raised by
        func is re-raised after retries are exhausted.
        """

        last_error = None

        for _ in range(attempts):
            try:
                result = func()

                if hasattr(result, "status_code") and result.status_code < 500:
                    return result

            except Exception as e:
                last_error = e

            time.sleep(wait)

        if last_error:
            raise last_error

        raise Exception("Retry exhausted")
