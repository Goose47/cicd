from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


async def validate_post_data(data: dict) -> bool:
    if not isinstance(data, dict):
        return False
    if not data.get('name') or not isinstance(data['name'], str):
        return False
    if data.get('age') and not isinstance(data['age'], int):
        return False
    return True


@app.get('/')
async def hello():
    return 'Hello World!'


@app.get('/api')
async def get_api():
    return JSONResponse(content={'status': 'test'}, status_code=200)


@app.post('/api')
async def post_api(request: Request):
    json = await request.json()
    if await validate_post_data(json):
        return JSONResponse(content={'status': 'OK'}, status_code=200)
    else:
        return JSONResponse(content={'status': 'bad input'}, status_code=422)
