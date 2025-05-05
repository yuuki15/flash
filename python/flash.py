"""Flash Add Game - Add 10 flashing numbers!"""

import random
import time

correct_answer: int = 0

# Displays 10 random numbers.
for _ in range(10):
    number: int = random.randint(1, 9)

    # Prints number with beep.
    print(f"\r\a{number}", end="")
    time.sleep(0.5)

    # Clears number.
    print("\r ", end="")
    time.sleep(0.1)

    correct_answer += number

# Gets user's answer.
try:
    user_answer: str = input("\rSum?\n")

    if int(user_answer) == correct_answer:
        print("Correct")
    else:
        print(correct_answer)
except (EOFError, KeyboardInterrupt, ValueError):
    print(correct_answer)
