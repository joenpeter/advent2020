import lib.calculate as calc
import lib.inputs

DATE = "01"

numbers = lib.inputs.number_per_line(DATE + ".txt")

first, second = calc.find_number_pair(numbers, 2020)
result = first * second
print(result)

first, second, third = calc.find_number_threesome(numbers, 2020)
result = first * second * third
print(result)
