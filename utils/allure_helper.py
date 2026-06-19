# File: utils/allure_helper.py

import json
import allure

class AllureHelper:
    @staticmethod
    def attach_request(endpoint, payload):
        allure.attach(
            json.dumps(
                payload,
                indent=2
            ),
            name=f"REQUEST → {endpoint}",
            attachment_type=allure.attachment_type.JSON
        )

    @staticmethod
    def attach_response(response):
        try:
            body = response.json()
        except Exception:
            body = response.text

        allure.attach(
            json.dumps(
                body,
                indent=2
            ),
            name="RESPONSE",
            attachment_type=allure.attachment_type.JSON
        )
