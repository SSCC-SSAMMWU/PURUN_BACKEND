from fastapi import HTTPException


def ERROR_CANT_ACCESS_MOUDLE():
    # return 400, "cant access module error"
    raise HTTPException(status_code=400, detail="Item not found")

# def SUCCESS_INSERT_DATA():
