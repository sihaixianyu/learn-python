if __name__ == "__main__":
    tmp = open("text.txt")
    for i in range(3):
        line = tmp.readline().strip()
        print(line)
