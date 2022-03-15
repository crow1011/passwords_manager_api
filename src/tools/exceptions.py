class NotFoundException(RuntimeError):
    """ Not Found Exception """
    def __init__(self, ):
        super().__init__("ID some-id not found.")


class ConflictException(RuntimeError):
    """ Conflict Exception """
    def __init__(self, ):
        super().__init__("Conflict error")