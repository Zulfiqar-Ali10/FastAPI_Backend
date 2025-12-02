from fastapi import HTTPException, status


def raise_not_found(detail: str):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail={"status": "error", "message": detail},
    )


def raise_bad_request(detail: str):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={"status": "error", "message": detail},
    )


def raise_server_error(detail: str):
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail={"status": "error", "message": detail},
    )
