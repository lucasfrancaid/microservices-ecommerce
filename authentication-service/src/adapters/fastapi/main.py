from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.infrastructure.http.fastapi.controllers.sign_up import sign_up_router

app = FastAPI(
    title='Authentication',
    description='Service to Authentication Management',
    version='0.0.1',
)

app.include_router(sign_up_router)


@app.get('/health-check', tags=['Default'], response_class=JSONResponse)
def health_check():
    return {'message': 'Is alive!'}
