def solution():
    file1 = open("input", "r")
    content = file1.readlines()
    file1.close()
    larger = 0
    old = int(content[0])
    for num in content[1:]:
        num = int(num)
        if num > old:
            larger += 1
        old = num
    print(larger)


if __name__ == "__main__":
    solution()
