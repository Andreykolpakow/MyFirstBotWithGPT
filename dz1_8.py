import random

def generate_random_number(start, end):
    random_number = random.randint(start, end)
    return random_number

start_range = 1
end_range = 100

random_number = generate_random_number(start_range, end_range)
print(random_number)