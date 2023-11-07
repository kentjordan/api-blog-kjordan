import env  # this will load the .env files into process memory
import os
import uvicorn
from fastapi import FastAPI
from modules.users import users_router
from modules.blogs import blogs_router


api = FastAPI()

api.include_router(users_router.router)
api.include_router(blogs_router.router)

if __name__ == '__main__':

    API_HOST_ADDRESS = os.getenv('API_HOST_ADDRESS')
    API_HOST_PORT = os.getenv('API_HOST_PORT')

    try:
        uvicorn.run(app=api, host=API_HOST_ADDRESS,
                    port=int(API_HOST_PORT))
    except NameError as err:
        print(err)
        ...
