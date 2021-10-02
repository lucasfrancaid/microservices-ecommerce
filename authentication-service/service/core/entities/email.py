from typing import Dict, List, Optional, Union

from pydantic import BaseModel


class EmailConfigurationEntity(BaseModel):
    host: str
    port: int
    username: str
    password: str
    timeout: Optional[int] = 60
    use_tls: Optional[bool] = False
    use_ssl: Optional[bool] = False
    ssl_certfile: Optional[str] = None


class SendEmailEntity(BaseModel):
    subject: str
    email_from: str
    email_to: List[str]
    body: Union[Dict, str]
