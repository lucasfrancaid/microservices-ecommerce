import uvicorn
from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get('/health-check', response_class=JSONResponse)
def health_check(request: Request):
    return {'message': 'Is alive!'}
