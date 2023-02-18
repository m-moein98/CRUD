from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from configurations.base_router import BaseRouter

from .db import Database

router = InferringRouter()
db_client = Database()


@cbv(router)
class TheAppRouter(BaseRouter):
    @router.get("/")
    async def get_list(self):
        return await db_client.get_list()

    @router.get("/{id}")
    async def get_one(self, id):
        return await db_client.get_one(id)

    @router.post("/")
    async def create_one(self, item: dict):
        return await db_client.create_one(item)

    @router.patch("/{id}")
    async def update_one(self, id, item: dict):
        return await db_client.update_one(id, item)

    @router.delete("/{id}")
    async def delete_one(self, id):
        return await db_client.delete_one(id)
