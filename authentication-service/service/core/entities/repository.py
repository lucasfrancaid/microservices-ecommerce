from typing import Optional

from pydantic import BaseModel


class RepositoryConfigurationEntity(BaseModel):
    name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    use_ssl: Optional[bool] = False
    ssl_certfile: Optional[str] = None
