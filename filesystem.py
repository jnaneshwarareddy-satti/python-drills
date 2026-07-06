from pathlib import Path
import sys

try:
    pt = sys.argv[1]

except IndexError:
    print("please enter path ")

else:
    folder = Path(pt)
    notebook = {}
    # fill notebook with name and its size

    try:
        for item in folder.iterdir():
            if item.is_file():
                notebook[item.name] = item.stat().st_size
    except FileNotFoundError:
        print("path not found..")
    else:

        # sorting notebook
        sorted_notebook = dict(sorted(notebook.items(), key=lambda item: item[1]))
        # printing sorted notebook , 1kb=1024 bytes , xbytes=x/1024 kb
        for file in sorted_notebook.items():
            print(f"{file[0]} = {(file[1]/1024):.2f}kb", end=" | ")
