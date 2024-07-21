ROWS = 26
for i in range(1,27):
    # print(i, end=" ")
    # stars = ["*"] * i
    # print(''.join(stars), end="")
    # s = [chr(i + 96)] * i
    # print(''.join(s))
    print(f'{i} {"".join(["*"]*i)}{"".join([chr(i+96)]*i)}')