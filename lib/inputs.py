
# One number per line, return a list with int
def number_per_line(filepath):
   return list_to_int(entry_per_line(filepath)) 

   

def list_to_int(list):
   return [int(i) for i in list] 

def entry_per_line(filepath):
   calc_file = open(filepath)
   inputs = []
   for line in calc_file:
      inputs.append(int(line))
   return inputs
