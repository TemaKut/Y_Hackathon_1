from pydantic import BaseModel


class TokenData(BaseModel):
    """ Необходимая информация о токене """

    token: str
