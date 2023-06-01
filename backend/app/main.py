from fastapi import FastAPI

from app.settings import DEBUG


app = FastAPI(
    debug=DEBUG,
    title='Super backend :)',
)


# @app.get('/')
# async def test():

#     return 1
