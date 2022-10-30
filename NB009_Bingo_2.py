def bingo(lines):

    n, x = int(lines[0]), lines[1:]

    check_d1 = check_d2 = 1
    for i in range(n):
        check_row = check_col = 1

        for j in range(n):
            if x[i][j] == "x":
                check_row = 0
            if x[j][i] == "x":
                check_col = 0

        if check_row or check_col:
            return "Yes"

        if x[i][i] == "x":
            check_d1 = 0
        if x[n-i-1][i] == "x":
            check_d2 = 0

    if check_d1 or check_d2:
        return "Yes"

    return "No"


if __name__ == '__main__':

    lines = "3\nxox\noxx\nxxo"
    lines = lines.split()
    print(bingo(lines))
