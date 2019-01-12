import random

original = [3,4,5]
time = 0


while True:
    a = random.choice(original)
    b = random.choice(original)
    c = random.choice(original)
    d = (a*10+b)*c
    time += 1
    print("a multiple b is {}".format(d))
    if time == 100:
        break