from fastapi import FastAPI,UploadFile
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"message" : "This is home route of api."}

@app.get("/videos")
def all_videos():
    return {"message":"All the videos will be listed on this route."}

@app.post("/upload")
def upload_link(files:list[UploadFile]):
    print(files)
    return {"message":"File uploaded successfully."}


uvicorn.run(app)