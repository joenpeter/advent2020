
# One number per line, return a list with int
def number_per_line(filepath):
   return list_to_int(entry_per_line(filepath)) 


# Each line represents a list, split by a specific sequence
def list_per_line(filepath, delimiter):
   return split_strings_in_list(entry_per_line(filepath), delimiter)

def split_strings_in_list(list, delimiter):
   return [s.split(delimiter) for s in list]

def list_to_int(list):
   return [int(i) for i in list] 

def entry_per_line(filepath):
   calc_file = open(filepath)
   inputs = []
   for line in calc_file:
      inputs.append(line)
   return inputs
