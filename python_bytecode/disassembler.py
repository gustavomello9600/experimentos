import sys
from dis import dis

filename = sys.argv[1]

pdf = False
if len(sys.argv) >= 3:
    pdf = True

with open(filename + ".py") as input_file:
    code = input_file.read()

with open(filename + ".txt", "w") as output_file:
    dis(code, file=output_file)

if pdf:
    import os

    with open(filename + ".txt") as output_file:
        bytecode = output_file.read()
    markdown_output = f"""## Code
```{{.python .numberLines}}
{code}
```

## Bytecode
```{{.line-numbers}}
  line     byte opname                 arg argval
{bytecode}
```"""
    with open(filename + ".md", "w") as tmp:
        tmp.write(markdown_output)

    os.system(f"pandoc {filename + '.md'} -o {filename + '.pdf'} -V fontsize=12pt && rm {filename + '.md'}")
