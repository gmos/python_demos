from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

class Numbers(BaseModel):
    num1: float
    num2: float

class Result(BaseModel):
    result: float

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add", response_model=Result)
async def add_numbers(numbers: Numbers) -> Result:
    return Result(result=numbers.num1 + numbers.num2)

@app.post("/subtract", response_model=Result)
async def subtract_numbers(numbers: Numbers) -> Result:
    return Result(result=numbers.num1 - numbers.num2)

@app.post("/multiply", response_model=Result)
async def multiply_numbers(numbers: Numbers) -> Result:
    return Result(result=numbers.num1 * numbers.num2)

@app.post("/divide", response_model=Result)
async def divide_numbers(numbers: Numbers) -> Result:
    if numbers.num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return Result(result=numbers.num1 / numbers.num2)