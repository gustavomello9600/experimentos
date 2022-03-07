import sys
from dis import dis
from pathlib import Path

filename = sys.argv[1]
output_path = (Path(__file__).resolve().parent
               / "disassembled_scripts"
               / filename)
output_path.mkdir(parents=True, exist_ok=True)

pdf = False
if len(sys.argv) >= 3:
    pdf = True

with open(filename + ".py") as input_file:
    code = input_file.read()

with open(output_path / (filename + ".txt"), "w") as output_file:
    dis(code, file=output_file)

if pdf:
    import os

    with open(output_path / (filename + ".txt")) as output_file:
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

    os.system(f"pandoc {filename + '.md'} -o {output_path / (filename + '.pdf')} -V fontsize=12pt && rm {filename + '.md'}")
