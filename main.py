letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','@','#','$','%','^','&','*','(',')']

import random as rnd

questions = ["length","letters","numbers","symbols"]
value = [0,0,0,0]
i = 0
password = ""
for question in questions:
    if question == "length":
        value[i] = int(input("What should be the length of the password? (should be more than 8): "))
    else:
        value[i] = int(input(f"How many {question} should be in password:"))
    i += 1
i = 1

if value[0] == (value[1] + value[2] + value[3]):
    questions.remove("length")  # removes the "length"
    candidate = ""
    for val in range(0, ( value[1] + value[2] + value[3])):
        # removing expended data from list, so they won't be choosed randomly
        if value[1] == 0:
            questions.remove("letters")
            value[1] = 666
        if value[2] == 0:
            questions.remove("numbers")
            value[2] = 666
        if value[3] == 0:
            questions.remove("symbols")
            value[3] = 666
        select =rnd.choice(questions)
        if select == "letters":
            candidate = rnd.choice(letters)
            value[1] -= 1
        elif select == "numbers":
            candidate = rnd.choice(numbers)
            value[2] -= 1
        elif select == "symbols":
            candidate = rnd.choice(symbols)
            value[3] -= 1

        password += candidate
else:
    print("Invalid. ")
    exit(1)
print(f"Your password is: {password}")