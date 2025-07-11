import re
from typing import Callable
def generator_numbers(text: str):
    patern=r'\b\d+\.\d+\b'# отут я признаюь попросив чата щоб він мені допоміг з цим 
    regularuti=re.findall(patern,text)
    for num in regularuti:
        yield float(num)
def sum_profit(text: str, func: Callable):
    total= 0.0
    for num in func(text):
        total = num + total
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
print("Загальний дохід:",sum_profit(text, generator_numbers))
