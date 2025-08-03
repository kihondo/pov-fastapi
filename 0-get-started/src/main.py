from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Define a simple GET endpoint
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Define another endpoint with path parameter
@app.get("/hello/{name}")
def read_hello(name: str):
    return {"message": f"Hello {name}"}

# Define endpoint with query parameter
@app.get("/greet")
def greet(name: str = "World"):
    return {"greeting": f"Hello {name}!"}