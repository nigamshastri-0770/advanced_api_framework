import os
import yaml

class ConfigReader:
    _cache = None

    @classmethod
    def load(cls):

        if cls._cache:
            return cls._cache

        env = os.getenv(
            "ENV",
            "dev"
        )

        config = {}

        try:

            if os.path.exists(
                "config/config.yaml"
            ):

                with open(
                    "config/config.yaml",
                    "r"
                ) as f:

                    loaded = yaml.safe_load(f)

                    if loaded:
                        config.update(
                            loaded
                        )

        except Exception:
            pass


        env_file = (
            f"config/{env}.yaml"
        )

        try:

            if os.path.exists(
                env_file
            ):

                with open(
                    env_file,
                    "r"
                ) as f:

                    loaded = yaml.safe_load(f)

                    if loaded:
                        config.update(
                            loaded
                        )

        except Exception:
            pass


        cls._cache = config

        return config

    @classmethod
    def get(
        cls,
        key,
        default=None
    ):

        return (
            cls
            .load()
            .get(
                key,
                default
            )
        )

