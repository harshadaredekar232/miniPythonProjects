import random
import time

op = ["+", "-", "*"]


def generate_problem():
    left = random.randint(2, 15)
    right = random.randint(2, 15)
    operator = random.choice(op)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer


wrong = 0
input("Press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(10):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("----------------------")
print(f"Nice work! You finished in {total_time} seconds!")