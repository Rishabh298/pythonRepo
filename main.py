from fastapi import FastAPI
import math

app = FastAPI()


@app.get("/")
def read_root():
    return {"data": ""}

@app.get("/hello")
def helloWorld():
    return {"data": "helloworld"}

@app.get("/findHypotenuse")
def calculate_triangle_hypotenuse(side1: str ='0', side2: str='0'):

 if (side1.isnumeric() and side2.isnumeric()):
    firstSide = float(side1)
    secondSide = float(side2)
    return {"hypotenuse": math.sqrt(math.pow(firstSide, 2) + math.pow(secondSide, 2))}
 else:
    return {"data": "given params are invalid"}

