from bson.objectid import ObjectId

import configurations.base_db as db
from configurations.base_db import DatabaseConfiguration, start_db


class Database(DatabaseConfiguration):
    @start_db()
    async def get_list(self):
        query = db.client.MY_COLLECTION.find()
        items = []
        async for item in query:
            item["_id"] = str(item["_id"])
            items.append(item)
        return items

    @start_db()
    async def get_one(self, id):
        query = await db.client.MY_COLLECTION.find_one({"_id": ObjectId(id)})
        query["_id"] = str(query["_id"])
        return query

    @start_db()
    async def create_one(self, item: dict):
        query = await db.client.MY_COLLECTION.insert_one(item)
        return str(query.inserted_id)

    @start_db()
    async def update_one(self, id, item: dict):
        query = await db.client.MY_COLLECTION.update_one(
            {"_id": ObjectId(id)}, {"$set": item}
        )
        return query.modified_count

    @start_db()
    async def delete_one(self, id):
        query = await db.client.MY_COLLECTION.delete_one({"_id": ObjectId(id)})
        return query.deleted_count
