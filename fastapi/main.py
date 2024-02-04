from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


class ValidationException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


async def validate_post_data(data: dict) -> bool:
    if not data.get('name') or not isinstance(data['name'], str):
        raise ValidationException('name field is required and must be of type string')
    if data.get('age') and not isinstance(data['age'], int):
        raise ValidationException('age field must be of type int')
    return True


@app.get('/')
async def hello():
    return 'Hello World!'


@app.get('/api')
async def get_api():
    return JSONResponse(content={'status': 'test'}, status_code=200)


@app.post('/api')
async def post_api(request: Request):
    try:
        json = await request.json()
        await validate_post_data(json)
    except ValidationException as e:
        return JSONResponse(content={'error': e.message}, status_code=422)
    except Exception as e:
        return JSONResponse(content={'error': 'JSON is not present'}, status_code=400)

    return JSONResponse(content={'status': 'OK'}, status_code=200)


def test():
    pass
