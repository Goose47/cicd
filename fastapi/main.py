from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()


async def validate_post_data(data: dict) -> bool:
    if not isinstance(data, dict):
        raise HTTPException(status_code=422, detail='No json is present')
    if not data.get('name') or not isinstance(data['name'], str):
        raise HTTPException(status_code=422, detail='name field is required and must be of type string')
    if data.get('age') and not isinstance(data['age'], int):
        raise HTTPException(status_code=422, detail='age field is required and must be of type int')
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
    await validate_post_data(json)
    return JSONResponse(content={'status': 'OK'}, status_code=200)
