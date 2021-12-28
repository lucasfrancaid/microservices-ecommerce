import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from src.adapters.http.fastapi.controllers.sign_up import sign_up_router
from src.infrastructure.config.settings import static_settings
from src.infrastructure.orm.sqlalchemy.database import Base, engine

app = FastAPI(
    title='Authentication',
    description='Service to Authentication Management',
    version='0.0.1',
)
app.include_router(sign_up_router)


@app.on_event('startup')
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


@app.get('/health-check', tags=['Default'], response_class=JSONResponse)
async def health_check():
    return {'message': 'Is alive!'}


if __name__ == '__main__':
    uvicorn.run(
        'src.adapters.http.fastapi.main:app',
        host=static_settings.APP_HOST,
        port=static_settings.APP_PORT,
        reload=False,
        debug=static_settings.DEBUG,
        log_level='info'
    )
