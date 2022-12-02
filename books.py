from fastapi import FastAPI

app = FastAPI()


# creating a new HTTP Route in FastAPI
@app.get("/")
async def first_api():
    return {"message": "Hello Jiarui!"}

