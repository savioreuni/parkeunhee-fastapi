import uvicorn
from fastapi import FastAPI
from routes.users_routes import user_router
from routes.file_routes import file_router

app = FastAPI()

app.include_router( user_router , prefix="/users")
app.include_router( file_router , prefix="/file")


from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])



if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
    #http://localhost:8000/docs

    