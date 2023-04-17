guessing_word = "zadek"
guess = ""
guess_couter = 0
max_guess = 3
out_of_guesses = False

while guess!= "zadek" and not(out_of_guesses):
    if guess_couter < max_guess:
        guess = input("Napiš hádané slovo:  ")
        guess_couter += 1
    else:
        out_of_guesses = True

if guess == guessing_word:
    print("Vyhrál jsi")
else:
    print("You loose")