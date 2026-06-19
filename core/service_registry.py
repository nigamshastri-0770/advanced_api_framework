class ServiceRegistry:

    SERVICES = {
        "auth": "/auth",
        "user": "/users",
        "order": "/orders",
        "payment": "/payments"
    }

    @classmethod
    def get(cls, service):
        return cls.SERVICES[service]