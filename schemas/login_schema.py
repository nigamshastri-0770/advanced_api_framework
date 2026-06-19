# File: schemas/login_schema.py

LOGIN_SCHEMA = {

    "type": "object",

    "properties": {

        "token": {
            "type": "string"
        },

        "_meta": {

            "type": "object",

            "properties": {

                "powered_by": {
                    "type": "string"
                },

                "docs_url": {
                    "type": "string"
                },

                "message": {
                    "type": "string"
                }

            }
        }
    },

    "required": [
        "token"
    ]
}