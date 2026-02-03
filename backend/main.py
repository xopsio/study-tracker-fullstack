from fastapi import FastAPI

app = FastAPI(title='Study Tracker')

@app.get('/')
async def read_root():
    return {'message': 'Study Tracker backend running'}
