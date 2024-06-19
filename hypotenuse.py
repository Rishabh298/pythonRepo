from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/findHypotanuse")
def calculate_triangle_hypotenuse(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# Example usage:
side1 = 3
side2 = 4
hypotenuse = calculate_triangle_hypotenuse(side1, side2)
print("Hypotenuse:", hypotenuse)