from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins = ["https://localhost:3000",]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_methods = ["*"],
    allow_credentials = True,
    allow_headers = ["*"]
)

@app.get("/")
def read_root():
    return {
        "ping": "Pong "
    }

@app.get('/api/todo')
def get_todo():
    return 1

@app.get('/api/todo/{id}', summary="Get each todo by it's id")
def get_todo_by_id(id):
    return id

@app.post('/api/todo')
async def create_todo(todo):
    return 1


@app.put('/api/todo/{id}')
async def update_todo(id, todo):
    return 1

@app.delete('/api/todo/delete/{id}')
def delete_todo(id):
    return id

