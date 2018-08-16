def makeSuccessResponse(result):
    objSucess = {
        "code": 200,
        "status": "Success",
        "results": result
    }
    return objSucess



def makeFailResponse(result):
    objFail = {
        "code": 400,
        "status": "Bad Request",
        "results": result
    }
    return objFail