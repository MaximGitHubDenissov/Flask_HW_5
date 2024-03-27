from fastapi import FastAPI
from models import Task

tasks = []
app = FastAPI()
for i in range(1, 6):
    task_test = Task(task_id=i, title=f'Title_{i}', content=f'some_text_{i}')
    tasks.append(task_test)


@app.get('/')
async def root():
    return {'message': "Hello world"}


@app.get('/tasks')
async def get_tasks():
    return {'tasks': tasks}


@app.post('/tasks')
async def add_task(task: Task):
    tasks.append(task)


@app.get('/tasks/{task_id}')
async def get_task_by_id(task_id: int):
    for task in tasks:
        if task.task_id == task_id:
            return task
    return {'message': 'Not found'}


@app.put('/tasks/{task_id}')
async def update_task(task_id: int, task: Task):
    for j, item in enumerate(tasks):
        if item.task_id == task_id:
            tasks[j] = task
            return task

    return {'message': 'Not found'}


@app.delete('/tasks/{task_id}')
async def delete_task(task_id: int):
    for j, item in enumerate(tasks):
        if item.task_id == task_id:
            del tasks[j]
            return item

    return {'message': 'Not found'}
