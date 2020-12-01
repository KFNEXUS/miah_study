import random

rng = random.Random(123)
for elem in range(10):
    dice_throw = rng.randrange(1,7)   # Return an int, one of 1,2,3,4,5,6
    print(dice_throw)




cards = list(range(52))  # Generate ints [0 .. 51]
new = rng.shuffle(cards)
print(cards )
print(new )