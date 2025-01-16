count = int(input())

array = []
for i in range(count):
    array.append(list(map(int, input().split(' '))))

white_paper = [[0 for col in range(100)] for row in range(100)]

for black in array:
    for j in range(black[1], black[1] + 10):
        for k in range(black[0], black[0] + 10):
            if (white_paper[j][k] != 1):
                white_paper[j][k] = 1

result = 0
for i in range(100):
    result += sum(white_paper[i])
print(result)
