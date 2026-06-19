from jsonschema import validate

class SchemaValidator:
    @staticmethod
    def validate(
        response,
        schema
    ):

        validate(
            response.json(),
            schema
        )

        return True