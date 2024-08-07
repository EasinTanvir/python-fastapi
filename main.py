from fastapi import FastAPI

app = FastAPI()


# '@' path operation decorator, 'get' is the operation and '/' is the path

@app.get("/")

# path operation function
def test() :
    return "hello"