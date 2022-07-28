num = [1, 2, 3]
num.sort()
while i < len(num):
    if i > 0:
        s = num[i]+num[i+1]
        print(s)
        num.remove(num[i])
        num.remove(num[i+1])
        num.append(s)
        i = 0
    i += 1
print(num)
