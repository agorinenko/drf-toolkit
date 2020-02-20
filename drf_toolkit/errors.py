class ApiViewError(Exception):
    """
    Api view error
    """

    def __init__(self, message, status=500):
        super().__init__(message)
        self.__status = status

    @property
    def status(self):
        return self.__status


class DjangoModelError(Exception):
    """
    Django model error
    """
