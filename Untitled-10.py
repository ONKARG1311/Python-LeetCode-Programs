import sys


def main(lines):
    n = eval(lines[0])
    lst = lines[1:]

    for i in range(n):
        flag = 1
        for j in range(n):
            if lst[i][j] == "x":
                flag = 0
        if flag == 1:
            return "Yes"

    for i in range(n):
        flag = 1
        for j in range(n):
            if lst[j][i] == "x":
                flag = 0
        if flag == 1:
            return "Yes"

    return "No"


if __name__ == '__main__':

    # lines = []
    # for z in sys.stdin:
    #     lines.append(z.rstrip('\r\n'))

    lines = "3\nxox\noxx\nxxo"
    lines = lines.split()

    print(main(lines))
