# Write a program to check if the given number is a palindrome number

# Given
given = ['121', '125']

for i in given:

    reverse = i[::-1]

    if( i == reverse ):
        print('The original number is ', i)
        print('The given number is a palindrome')
        print('\n')

    else:
        print('The original number is ', i)
        print('The given number is not a palindrome')