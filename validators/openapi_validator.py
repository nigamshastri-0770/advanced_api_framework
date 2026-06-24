import jsonschema


class OpenAPIValidator:

    @staticmethod
    def validate(response_json, schema):

        try:

            jsonschema.validate(
                instance=response_json,
                schema=schema
            )

            return True

        except jsonschema.ValidationError as e:

            raise AssertionError(
                f"""
Schema validation failed

Error:
{e.message}

Path:
{list(e.absolute_path)}
"""
            )