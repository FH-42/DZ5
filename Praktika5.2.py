def my_square(lst):
    return lst ** 2

n = int(input("n="))
a = list(range(0, n+1))
a[1] = 0
lst = []

i = 2
while i <= n:
    if a[i] != 0:
        lst.append(a[i])
        for j in range(i, n+1, i):
            a[j] = 0
    i += 1
print(lst)

squared_numbers = list(map(my_square, lst))

print(squared_numbers)