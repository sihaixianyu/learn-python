import sys

if __name__ == "__main__":
    for line in sys.stdin:
        if "exit" == line.rstrip():
            break

        print(line, end="")
