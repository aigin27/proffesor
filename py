import random

def main():

    math_problems = generate_math_problems()

    score = 0

    for problem in math_problems:
        answer_attempts = 0
        while answer_attempts < 3:
            user_answer = input(f"{problem} ")
            try:
                user_answer = int(user_answer)
                if user_answer == eval(problem[:-1]):
                    score += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            except Exception:
                print("EEE")
            answer_attempts += 1
        else:
            print(f"The correct answer is {eval(problem[:-1])}")
            break

    print(f"Your score: {score} out of {len(math_problems)}")

def get_level():
    while True:
        try:
            input_level = int(input("Level: "))
            if input_level in (1, 2, 3):
                return input_level
        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        level = 9
    elif level == 2:
        level = 99
    elif level == 3:
        level = 999

    random_num = random.randint(1, level)
    return random_num

def generate_math_problems():
    chosen_level = get_level()
    math_problems = []
    for _ in range(10):
        x = generate_integer(chosen_level)
        y = generate_integer(chosen_level)
        problem = f"{x} + {y} ="
        math_problems.append(problem)
    return math_problems

if __name__ == "__main__":
    main()
