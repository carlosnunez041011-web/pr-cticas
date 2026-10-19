

def number():
    print("Patricia Núñez Patiño\n19/10/26")
    secret_number = 5
    guess_number = int(input("Guess number between 1 and 10: "))
    if guess_number == 5:
        print("Well done! You guessed the number!")
    else:
        print("Sorry, that's not the right number!")


print(number())


