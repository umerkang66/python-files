from random import randint
import sys


def check_answer(ans, rand_start, rand_end):
    print(ans)
    tries = 0
    while True:
        try:
            tries += 1
            guess = int(input(f"guess a number {rand_start}~{rand_end}\n"))
            if rand_start - 1 < guess < rand_end + 1:
                if guess == ans:
                    print(f"You win in {tries} tries")
                    break
                else:
                    if ans < guess:
                        rand_end = guess
                    else:
                        rand_start = guess
                    continue
        except ValueError:
            print("please enter a number")
            continue


def start_game():
    random_start = int(sys.argv[1])
    random_end = int(sys.argv[2])
    answer = randint(random_start, random_end)
    check_answer(answer, random_start, random_end)


start_game()
