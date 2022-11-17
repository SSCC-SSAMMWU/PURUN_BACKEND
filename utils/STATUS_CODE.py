from fastapi import HTTPException


def ERROR_CANT_ACCESS_MOUDLE():
    # return 400, "cant access module error"
    raise HTTPException(status_code=400, detail="Item not found")


def MODULES_ACCESS():
    raise HTTPException(status_code=200, detail="Item not found")


def MODULES_DENIED():
    raise HTTPException(status_code=400, detail="Item not found")
