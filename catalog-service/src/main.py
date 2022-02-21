import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.infrastructure.config.settings import static_settings

app = FastAPI(
    title='Catalog',
    description='Service to Catalog Management',
    version='0.0.1',
)


@app.get('/health-check', tags=['Default'], response_class=JSONResponse)
async def health_check():
    return {'message': 'Is alive!'}


if __name__ == '__main__':
    uvicorn.run(
        'src.main:app',
        host=static_settings.APP_HOST,
        port=static_settings.APP_PORT,
        reload=False,
        debug=static_settings.DEBUG,
        log_level='info'
    )
