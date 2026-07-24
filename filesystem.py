from pathlib import Path
import sys

pt = sys.argv[1]
folder = Path(pt)
notebook = dict()

for item in folder.iterdir():
    if item.is_file():
        notebook[item] = format(item.stat().st_size / 1024, ".2f")

sorted_notebook = dict(sorted(notebook.items(), key=lambda item: item[1]))

print(sorted_notebook)
