from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home():
    return {"Greeting": "Hello World from FastAPI"}


# Health check endpoint
@app.get('/health')
async def healthcheck():
    return Response(content="OK", status_code=status.HTTP_200_OK)


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
