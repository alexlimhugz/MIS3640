# team = 'New England Patriots'
# for letter in team:
#     print(letter)


# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
#     if letter =='O' or letter == 'Q':
#         print (letter + 'u' + suffix)

#     else:
#         print(letter + suffix)

# team = 'New England Patriots'
# new_team = team[:3] + ' ' + 'Mexico'
# print(new_team[:])

team = 'New England Patriots'
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1

print(find(team, 'E'))