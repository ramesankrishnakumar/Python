# search python3 module index

import random

members = ['John', 'Mary', 'Bob', 'Mosh']

for i in range(3):
    print(random.choice(members))


class Dice:

    def roll(self):
        return random.randint(1, 6), random.randint(1, 6)


game = Dice()
print(game.roll())
