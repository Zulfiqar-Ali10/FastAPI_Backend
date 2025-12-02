from fastapi import status
from fastapi.responses import JSONResponse


def success_response(
    data: dict, message: str = "Success", status_code: int = status.HTTP_200_OK
):
    """
    Standard success response
    """
    return JSONResponse(
        status_code=status_code,
        content={"status": "success", "message": message, "data": data},
    )


def created_response(data: dict, message: str = "Created successfully"):
    """
    Standard response for POST
    """
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": message, "data": data},
    )
