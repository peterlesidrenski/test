list1 = [int(x) for x in input().split('-')]
#1
print(list1)
#2
for i in list1:
    if i % 2 == 0:
        list1.insert(1, i)
        break
print(list1)
#3
a = len(list1)
list1.insert(0, a)
print(list1)
#4
copy_list1 = reversed(list1)
list1.extend(copy_list1)
print(list1)
#5
print(list1[:: - 1])
print(list1)
#6
print(max(list1))
print(list1)
#7
b = len(list1)
list1.append(b)
print(list1)
#8
list1.sort(reverse=True)
print(list1)
#9
print(min(list1))
print(list1)
#10
c = list1.count(500)
list1.insert(6, c)
print(list1)
#11
for p in list1:
    if p % 2 == 0:
        list1.insert(2, p)
        break
print(list1)
#12
d = min(list1)
list1.insert(1, d)
print(list1)
#13
e = list1.count(10)
list1.insert(4, e)
print(list1)
#14
f = list1.pop(7)
print(f)
print(list1)
#15
for m in list1:
    if m % 2 == 1:
        list1.insert(9, m)
        break
print(list1)
#16
g = min(list1)
list1.append(g)
print(list1)
#17
for n in list1:
    if n % 2 == 1:
        list1.insert(4, n)
        break
print(list1)
#18
for t in list1:
    if t % 10 == 2:
        list1.insert(4, t)
        break
print(list1)
#19
h = list1.pop(5)
print(h)
print(list1)
#20
print(" ".join(str(x) for x in list1))
