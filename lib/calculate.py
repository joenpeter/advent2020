

# Figures out the number of valid combinations for *list* of ints,
# where you have to jump from start to end using at least *minimum* jump
# and at least *maximum* jump for each step
# TODO: Implement better handling of min/max, use min at all
def valid_jump_combinations(list, minimum, maximum):
   if len(list) < 3:
      # End case; we're at the last adapter jump
      return 1
   elif (list[0] - list[2]) <= maximum:
      # Case: We have 2 possibilities
      result = valid_jump_combinations(list[1:], minimum, maximum) + valid_jump_combinations(list[2:], minimum, maximum)
      return result
   else:
      # Case: Only 1 way forward
      return valid_jump_combinations(list[1:], minimum, maximum)

def valid_jump_combinations_faster(list):
   combinations = [0] * (max(list) + 1)
   combinations[0] = 1
   for item in list:
      if item < 3:
         # Special case for start of run
         if item == 2:
            c1 = combinations[item-1]
            c2 = combinations[item-2]
            combinations[item] = c1 + c2
         else:
            combinations[item] = 1      

      c1 = combinations[item-1]
      c2 = combinations[item-2]
      c3 = combinations[item-3]
      combinations[item] = c1 + c2 + c3

   return combinations[-1]


# Count the number of times number occurs in list
def number_of_elements(number, list):
   occurances = 0
   for n in list:
      if n == number:
         occurances += 1
   return occurances

# Difference between 2 elements (int) in the list, returned as a list of ints
# where each int is the diff beteen 2 elements in the provided list
def list_diff_size(list):
   previous = 0
   result = []
   for n in list:
      current = n - previous
      previous = n
      result.append(current)
   return result

def find_number_pair(numbers, expected_sum):
   numbers.sort()
   for base in numbers:
      found, addition = find_sum(numbers, expected_sum, base)
      if found:
         return base, addition

def find_number_threesome(numbers, expected_sum):
   numbers.sort()
   for first_base in numbers:
      for second_base in numbers:
         found, addition = find_sum(numbers, expected_sum, first_base + second_base)
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
