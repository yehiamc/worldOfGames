import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    str1 = "Please guess a number between 1 and {}\n".format(str(difficulty))
    guess = int(input(str1))
    return guess


def compare_results(guess_number, secret_number):
    if secret_number == guess_number:
        return True
    else:
        return False


def play(difficulty):
    answer = False
    rand_num = generate_number(difficulty)
    guess_num = get_guess_from_user(difficulty)
    return compare_results(rand_num, guess_num)
