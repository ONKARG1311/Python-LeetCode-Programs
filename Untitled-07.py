str1 = "1C0C1C1A0B1"
str2 = str1.replace("A", '&').replace("B", '|').replace("C", '^')
sum = eval(str2[0])

for i in range(1, len(str2), 2):
    sum = eval(str(sum)+str2[i:i+2])
print(sum)
