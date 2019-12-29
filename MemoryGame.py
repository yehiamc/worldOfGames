import time
import random
import Utils


def generate_sequence(difficulty):
    arr = []
    for i in range(1,difficulty+1):
        rand_num = random.randint(1, 101)
        arr.append(rand_num)
        print(arr)
        time.sleep(700 / 1000)

        Utils.screen_cleaner()
        return arr


def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.\n")
    arr = []
    for i in range(1, difficulty+1):
        in_num = str(input())
        arr.append(in_num)
    return arr


def is_list_equal(list_a, list_b):
    if list_a == list_b:
        return True
    else:
        return False


def play(difficulty):
    generated_list = generate_sequence(difficulty)
    guessed_list = get_list_from_user(difficulty)

    return is_list_equal(generated_list, guessed_list)