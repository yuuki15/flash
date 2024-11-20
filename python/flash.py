import random
import time

correct_answer = 0

for i in range(10):
    number = random.randint(1, 9)

    print(f"\r\a{number}", end="")
    time.sleep(0.5)

    print("\r ", end="")
    time.sleep(0.1)

    correct_answer += number

print("\rSum?")

answer = input()

if answer == str(correct_answer):
    print("Correct")
else:
    print(correct_answer)
