
calc_file = open("inputs.txt")

def find_number_pair(numbers, expected_sum):
   numbers.sort()
   for base in numbers:
      found, addition = find_sum(inputs, expected_sum, base)
      if found:
         return base, addition

def find_number_threesome(numbers, expected_sum):
   numbers.sort()
   for first_base in numbers:
      for second_base in numbers:
         found, addition = find_sum(inputs, expected_sum, first_base + second_base)
         if found:
            return first_base, second_base, addition

def find_sum(numbers, expected_sum, base):
   for addition in numbers:
      res = base + addition
      if res == expected_sum:
         # We found the correct combination
         return True, addition
      if res > expected_sum:
         # We have passed the point where we would have found
         # the correct combination
         return False, 0

inputs = []
for line in calc_file:
   inputs.append(int(line))

first, second = find_number_pair(inputs, 2020)
result = first * second
print(result)

first, second, third = find_number_threesome(inputs, 2020)
result = first * second * third
print(result)
