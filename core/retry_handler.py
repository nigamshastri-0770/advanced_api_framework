import requests
import time

from core.logger import logger


def safe_request(
    method,
    url,
    **kwargs
):

    retries = 3

    wait = 2

    response = None

    last_exception = None

    timeout = kwargs.pop(
        "timeout",
        10
    )

    for attempt in range(
        retries
    ):

        try:

            response = requests.request(
                method=method,
                url=url,
                timeout=timeout,
                **kwargs
            )

            logger.info(
                f"{method} "
                f"{url} "
                f"→ "
                f"{response.status_code}"
            )

            if response.status_code < 500:

                return response

            logger.warning(
                f"Attempt "
                f"{attempt+1} "
                f"returned "
                f"{response.status_code}"
            )

        except requests.exceptions.RequestException as e:

            last_exception = e

            logger.error(
                f"Attempt "
                f"{attempt+1}: "
                f"{str(e)}"
            )

        if attempt < retries - 1:

            time.sleep(
                wait
            )

            wait *= 2

    if last_exception:

        raise last_exception

    return response