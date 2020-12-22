def sum(number1: float, number2: float) -> float:
    if validate_float(number1) and validate_float(number2):
        return number1 + number2

def subtract(number1: float, number2: float) -> float:
    if validate_float(number1) and validate_float(number2):
        return number1 - number2

def multiply(number1: float, number2: float) -> float:
    if validate_float(number1) and validate_float(number2):
        return number1 * number2

def divide(number1: float, number2: float) -> float:
    try:
        if validate_float(number1) and validate_float(number2):
            return number1 / number2
    except ZeroDivisionError as zero_err:
        raise zero_err
    
def validate_float(number: float) -> bool:
    if isinstance(number, float):
        return True
    raise ValueError(f"Value {number} is not a number!")