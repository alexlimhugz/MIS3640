#Two roads diverged ina wood, and I took the less traveled one.
#if T(A) < T(B):
# Return A
# else:
#return B

age = input('What is Your Age?')
age = int(age)
if age >= 18:
    print('your age is {}.'. format(age))
    print('Adult')

elif age >= 6:
    print('kid')

else:
    print('Your age is {}.'.format(age))
    print('Teenager')

