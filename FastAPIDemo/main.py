from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

# We keep static files in the directory declared below.
app.mount("/static", StaticFiles(directory="static"), name="static")

# We keep Jinja2Templates in the directory declared below.
templates = Jinja2Templates(directory="templates")


class Numbers(BaseModel):
    """
    A model representing two numbers.
    """

    num1: float
    num2: float


class Result(BaseModel):
    """
    A model representing the result of an operation on two numbers.
    """

    result: float


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    """
    Serve the main HTML page.
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/add", response_model=Result)
async def add_numbers(numbers: Numbers) -> Result:
    """
    Add two numbers and return the result.
    """
    return Result(result=numbers.num1 + numbers.num2)


@app.post("/subtract", response_model=Result)
async def subtract_numbers(numbers: Numbers) -> Result:
    """
    Subtract two numbers and return the result.
    """
    return Result(result=numbers.num1 - numbers.num2)


@app.post("/multiply", response_model=Result)
async def multiply_numbers(numbers: Numbers) -> Result:
    """
    Multiply two numbers and return the result.
    """
    return Result(result=numbers.num1 * numbers.num2)


@app.post("/divide", response_model=Result)
async def divide_numbers(numbers: Numbers) -> Result:
    """
    Divide two numbers and return the result.
    """
    # Ensure division by zero is handled or avoided.
    if numbers.num2 == 0:
        return Result(
            result=float("inf")
        )  # Consider how you want to handle division by zero.
    return Result(result=numbers.num1 / numbers.num2)
