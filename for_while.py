my_list = [1, 2, 3, 4, 5, 6, 7, 100, 110, 21, 33, 32, 2, 4]

even = []
not_even = []
outlier =[]

for n in my_list:
    if n > 90:
        outlier.append(n)

    elif n%2 == 0:
        even.append(n)

    else:
        not_even.append(n)

print('Even numbers', even)
print('Odd_numbers', not_even )
print('outliers', outlier)