team = 'New England Patriots'

# letter = team[1]

# print(team[len(team)-1])

# index = 0
# for i in range (len(team)):
#     if team[i] != ' ':
#      print(team[i])

# for letter in team:
#     if letter.isalpha():
#      print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#    if letter =='O' or letter == 'Q':
#         print(letter+'u'+suffix)

#     else:
# print(letter + suffix)

# word = 'New England Patriots'
# count = 0
# for letter in word:
#         if letter == 'a':
#                     count = count + 1
                    
# print(count)
def count(word,letter):
    count = 0
    for letterx in word:
        if letterx == letter:
                count = count + 1
        return count
    
print(count(team, 'a'))

