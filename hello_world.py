from contextlib import redirect_stdout

with open("output.txt", "w") as f, redirect_stdout(f):
    print("hello world")