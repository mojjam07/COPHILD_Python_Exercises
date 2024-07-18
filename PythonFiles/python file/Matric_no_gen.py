from random import randint as rand

guess = rand(100, 999)
guess1 = rand(1000, 9999)
guess2 = rand(10000, 99999)

guess = str(guess)
guess1 = str(guess1)
guess2 = str(guess2)
#print("01" + guess.replace(guess[-2:], '**'))

combo = guess + guess1 + guess2
list(combo)

for c in combo:
    print(c, end='');