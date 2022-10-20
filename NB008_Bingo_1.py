import sys


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.

    x = lines[1:]

    for i in range(int(lines[0])):
        check = 1
        for j in range(int(lines[0])):
            if x[i][j] == "x":
                check = 0
        if check == 1:
            return "Yes"

    for i in range(int(lines[0])):
        check = 1
        for j in range(int(lines[0])):
            if x[j][i] == "x":
                check = 0
        if check == 1:
            return "Yes"

    check = 1
    for i in range(int(lines[0])):
        if x[i][i] == "x":
            check = 0
    if check == 1:
        return "Yes"

    check = 1
    for i in range(int(lines[0])):
        if x[int(lines[0])-i-1][i] == "x":
            check = 0
    if check == 1:
        return "Yes"

    return "No"


if __name__ == '__main__':

    #lines = []
    # for l in sys.stdin:
    #    lines.append(l.rstrip('\r\n'))

    lines = "3\nxox\noxx\nxxo"
    lines = lines.split()
    print(main(lines))
