#koshi
from math import sqrt
a,b = map(int,(input().split()))
if (a+b)/2 > sqrt(a*b):
    print(">")
elif (a+b)/2 < sqrt(a*b):
    print("<")
else:
    print("=")

#isfandiyor algebra darsida
n = int(input())
print(n**5 + 8 * n**4 - 5* n**3 + 3*n**2 + n - 12)


#gugurt
n = input()
s=0
number = {
    "0": 6,
    "1": 2,
    "2": 5,
    "3": 5,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 3,
    "8": 7,
    "9": 6
}
for i in n:
    s +=number[i]

print(s)


#uchburchak

    n = int(input())
    sides = list(map(int, input().split()))
    sides.sort()
    answer = "-1"
    p = 0


    for i in range(len(sides)):
        for j in range(i + 1, len(sides)):
            for k in range(j + 1, len(sides)):
                if sides[i] + sides[j] > sides[k] and sides[i] + sides[k] > sides[j] and sides[k] + sides[j] > sides[i]:
                    temp_p = sides[i] + sides[j] + sides[k]
                    if temp_p > p:
                        p = temp_p
                        answer = f"{sides[i]} {sides[j]} {sides[k]}"


    print(answer)
