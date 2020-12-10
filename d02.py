import lib.text
import lib.inputs

passlist = lib.inputs.list_per_line("02.txt", ": ")

nr_valid = 0
for passwd in passlist:
   if lib.text.chk_pass_valid(passwd[1], passwd[0]):
      nr_valid += 1

print(nr_valid)

nr_valid = 0
for passwd in passlist:
   if lib.text.chk_pass_valid_new(passwd[1], passwd[0]):
      nr_valid += 1

print(nr_valid)
