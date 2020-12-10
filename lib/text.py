import lib.inputs

# Check if password is valid for pattern
def chk_pass_valid(passwd, pattern):
   parts = pattern.split(" ")
   num = character_in_string(passwd, parts[1])
   limits = lib.inputs.list_to_int(parts[0].split("-"))
   if num < limits[0] or num > limits[1]:
      return False
   else:
      return True

# Check if password is valid for pattern
def chk_pass_valid_new(passwd, pattern):
   parts = pattern.split(" ")
   positions = lib.inputs.list_to_int(parts[0].split("-"))
   if passwd[positions[0]-1] == parts[1] or passwd[positions[1]-1] == parts[1]:
      if passwd[positions[0]-1] == parts[1] and passwd[positions[1]-1] == parts[1]:
         return False
      else:
         return True
   else:
      return False



# Count number of occurances of a character in a string
def character_in_string(string, character):
   count = 0
   
   for s in string: 
      if s == character: 
         count += 1

   return count
