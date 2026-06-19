# File: tests/test_retry.py


from utils.retry_helper import RetryHelper

counter = {"calls": 0}


def flaky():
    counter["calls"] += 1

    class Response:
        def __init__(self, status_code):
            self.status_code = status_code

    status = 500 if counter["calls"] < 3 else 200
    return Response(status)


def test_retry():
    response = RetryHelper.execute(flaky, attempts=5, wait=1)
    assert response.status_code == 200
