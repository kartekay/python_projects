import random

def higher_lower_game():
    celebrities = []
    for i in range(1, 1001):
        celebrities.append({"name": f"Celebrity {i}", "followers": random.randint(1, 1000)})
    score = 100
    current_celebrity = random.choice(celebrities)
    print(f"Starting celebrity: {current_celebrity['name']} with {current_celebrity['followers']}M followers")
    while True:
        user_input = input("Will the next celebrity have 'higher' or 'lower' followers? (type 'quit' to exit): ").strip().lower()
        if user_input == 'quit':
            print(f"Thanks for playing! Your final score is {score}.")
            break
        if user_input not in ['higher', 'lower']:
            print("Invalid input. Please type 'higher', 'lower', or 'quit'.")
            continue
        next_celebrity = random.choice(celebrities)
        while next_celebrity == current_celebrity:
            next_celebrity = random.choice(celebrities)
        print(f"Next celebrity: {next_celebrity['name']} with {next_celebrity['followers']}M followers")
        if (user_input == 'higher' and next_celebrity['followers'] > current_celebrity['followers']) or (user_input == 'lower' and next_celebrity['followers'] < current_celebrity['followers']):
            score += 10
            print("Correct guess! +10 points.")
        else:
            score -= 10
            print("Wrong guess. -10 points.")
        print(f"Your current score: {score}")
        if score <= 0:
            print("Game over! You have 0 points left.")
            break
        current_celebrity = next_celebrity
higher_lower_game()
