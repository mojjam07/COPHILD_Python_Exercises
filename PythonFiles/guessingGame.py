import data
print("Welcome on board!!")
print("*********************")
stake = int(input("Enter amount: $"))
word = input("Guess a fruit: ")

found = False
for fruit in data.fruits:
    if word.lower() == fruit:
        found = True
        break

if found and stake >= 10:
    print("*********************")
    print("There is a match,","you guessed", word,)
    print(f"You won ${stake*2}, congratulations")
else:
    print("*********************")
    print(f"You lost ${stake}")
    print("You guessed", word, "but it's not one of the fruits")