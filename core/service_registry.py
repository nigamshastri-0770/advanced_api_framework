from core.config_reader import (
ConfigReader
)

class ServiceRegistry:

    @classmethod
    def get_url(
        cls,
        service
    ):

        config = (
            ConfigReader.load()
        )

        urls = (
            config.get(
                "base_urls",
                {}
            )
        )

        url = (
            urls.get(
                service
            )
        )

        if not url:

            raise ValueError(
                f"No URL configured for {service}"
            )

        return url.rstrip("/")

