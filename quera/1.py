https://quera.org/problemset/66864?tab=description

n = int(input())
i = 0
len_n = 0
while True:
    i += 1
    len_n += len(str(i))
    if len_n >= n:
        s = str(i)[::-1]
        print(s[len_n - n])
        break


# next solution is better 

n = int(input())
ans = 0
m = 0
for i in range(1, 4001):
    if (9 * pow(10, i - 1) * i) + m>= n:
        ans = i
        break
    else:
        m += 9 * pow(10, i - 1) * i
number = int((n - m) / ans)
if number == 0:
    number += 1
number = pow(10, ans - 1) + number - 1
print(str(number)[int((n - m) % ans) - 1])


