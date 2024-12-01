from fastapi import FastAPI

app = FastAPI()


@app.get("/test")
async def test_route():
    return {"message": "Fiona is about to be an All Star"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, port=8069)
