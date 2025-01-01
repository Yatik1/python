from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "This is home route of api."}

@app.get("/videos")
def all_videos():
    return {"message":"All the videos will be listed on this route."}

uvicorn.run(app)