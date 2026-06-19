import yaml


class ConfigReader:

    def __init__(self):

        self.config = (
            self.load(
                "config/config.yaml"
            )
        )

    def load(
        self,
        path
    ):

        with open(
            path,
            "r"
        ) as file:

            return yaml.safe_load(
                file
            )

    def get(
        self,
        key,
        default=None
    ):

        return self.config.get(
            key,
            default
        )


config = (
    ConfigReader()
)