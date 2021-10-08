from typing import Optional
from dataclasses import dataclass


@dataclass
class RepositoryConfigurationEntity:
    name: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    username: Optional[str] = None
    password: Optional[str] = None
    use_ssl: Optional[bool] = False
    ssl_certfile: Optional[str] = None
