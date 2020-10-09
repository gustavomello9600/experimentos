import sys
from dis import dis

filename = sys.argv[1]

with open(filename + ".py") as input_file:
    code = input_file.read()

with open(filename + ".txt", "w") as output_file:
    dis(code, file=output_file)
