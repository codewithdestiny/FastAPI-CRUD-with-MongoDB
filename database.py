from models import TodoBase

from motor.motor_asyncio import AsyncIOMotorClient

client = AsyncIOMotorClient('mongodb://localhost:27017')

db = client.TodoList #create database called TodoList

collection = db.todo # create table called todo


async def fetch_one_todo(title):
    document = await collection.find_one({"title": title})
    return document



async def fetch_all_todo():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(TodoBase(**document))
    return todos

async def create_todo(todo):
    new_todo = await collection.insert_one(todo)
    return new_todo



async def update_todo(title, des):
    result = await collection.update_one({"title": title}, {"$set"})