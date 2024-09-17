#!/usr/bin/env python3
import random
import time

correct_answer = 0

for i in range(10):
    number = random.randint(1, 9)

    print(f"\r\a{number}", end="")
    time.sleep(0.3)

    print("\r", end="")
    time.sleep(0.2)

    correct_answer += number

print("\rSum?")

answer = input()

if int(answer) == correct_answer:
    print("Correct")
else:
    print(correct_answer)
