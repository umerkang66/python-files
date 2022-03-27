from random import randint
import sys


def check_answer(ans, rand_start, rand_end):
    print(ans)
    while True:
        try:
            guess = int(input(f"guess a number {rand_start}~{rand_end}\n"))
            if rand_start - 1 < guess < rand_end + 1:
                if guess == ans:
                    print("You win")
                    break
                else:
                    continue
        except ValueError:
            print('please enter a number')
            continue


def start_game():
    random_start = int(sys.argv[1])
    random_end = int(sys.argv[2])
    answer = randint(random_start, random_end)
    check_answer(answer, random_start, random_end)


