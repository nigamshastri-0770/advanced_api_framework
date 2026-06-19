import jsonschema


class DBValidator:

    @staticmethod
    def compare(api, db):
        assert api == db