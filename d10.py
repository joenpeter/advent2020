import lib.inputs
import lib.calculate


adapters = lib.inputs.number_per_line("10.txt")

adapters.sort()
end_adapter = adapters[-1] + 3
adapters.append(end_adapter)

differences = lib.calculate.list_diff_size(adapters)

ones = lib.calculate.number_of_elements(1, differences)
threes = lib.calculate.number_of_elements(3, differences)

result = ones * threes

print("Differences multiplied: ", result)

combs = lib.calculate.valid_jump_combinations_faster(adapters)

print("Combinations: ", combs)
