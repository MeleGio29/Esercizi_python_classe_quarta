import random

alice = random.randint(1, 6)
bob = random.randint(1, 6)

if(alice > bob):
    print(f"Ha vinto alice")
else:
    print(f"Ha vinto bob")