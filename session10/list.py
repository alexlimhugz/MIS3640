AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
numbers = [42, 123]
empty = []
# print(AFC_east, numbers, empty)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'],
    ['Adam', 'Bart', 'Lisa']
    
]

# print(L[1][2][1])

# for team in AFC_east:
#     print(team)


# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

# numbers = [2, 0, 1, 6, 9]

# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
    
# print(numbers)

# my_list = ['spam', 1, ['New England Patriots', \
#                        'Buffalo Bills', 'Miami Dolphins', \
#                        'New York Giants'], \
#            [1, 2, 3]]
# print(len(my_list))

# a = [1, 2, 3]
# a.sort()

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

print(only_upper('Babson College'))