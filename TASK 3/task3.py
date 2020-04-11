"""
TASK 3
1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
3. Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, on successful guess, user will get a "Well guessed!" message, and the program will exit.
4. Write a Python program to check the validity of password input by users. Validation.
5. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20
NOTE: VCS Must be Integrated in the Task. Hint: Use GitHub, ensure you create repo called TASK 3. Direct Copy and paste from the internet will disqualify you. Good Luck

#30daysofcodingwithpython
"""

##1
lis = []
for i in range(1500,2701):
    if (i%7 == 0 and i%5 == 0) == True:
        lis.append(i)

##2
def convert_temp(fc,change_to="c"):
    """
    fc -- either the celsius or fahrenheit value that is being converted
    change_to -- takes in a string c or f as the metric that the value fc is to be cnverted to.
    Ex: Convert 34 deg Fah to Cel
        convert_temp(34,change_to="c")
    """
    if change_to=="c":
        temp=5/9*(fc-32)
    if change_to=="f":
        temp=(9/5) * fc + 32
    return temp

##3
import random
input_pass = str(input("Type in Password: "))
validate_pass = str(input("Retype Password: "))
count = 1
while (input_pass != validate_pass) and (count <5):
    print("Incorrect Password")
    validate_pass = str(input("Validate Password: "))
    if input_pass == validate_pass:
        print("Correct")
        break
    count+=1
    if count == 5:
        print('Try again after 5mins')


##4
import random
hidden = random.randint(1,10)
users_guess = int(input("Guess a number between 1 and 9: "))
while users_guess != hidden:
    print("Guessed wrong, try again.")
    users_guess = int(input("Guess a number between 1 and 9: "))
    if users_guess == hidden:
        print("Well guessed!!")
        break

##5
def sum_two(x,y):
    #x and y must be integers
    sum_ = x+y
    if sum_ >= 15 and sum_ <= 20:
        sum_ = 20
    return sum_