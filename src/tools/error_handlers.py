def conflict_handler(error):
    """ conflict handler """
    return {
        "detail": "conflict error",
        "status": 409,
        "title": "Conflict Error",
    }, 409



def not_found_handler(error):
    """ Not found handler """
    return {
        "detail": str(error),
        "status": 404,
        "title": "Not Found",
    }, 404