import random
import art
import data

print(art.logo)
score = 0
isPlaying = True
choiceB = random.choice(data.data)

def decision(guess, a_followers, b_followers):
    if guess == "A" and a_followers >= b_followers:
        return True
    elif guess == "A" and a_followers <= b_followers:
        return False
    elif guess == "B" and a_followers >= b_followers:
        return False
    else:
        return True

def format_data(choice):
    choice_name = choice["name"]
    choice_description = choice["description"]
    choice_country = choice["country"]
    return f"{choice_name}, a {choice_description}, from {choice_country}."

while isPlaying:
    choiceA = choiceB
    choiceB = random.choice(data.data)
    while choiceA == choiceB:
        choiceB = random.choice(data.data)

    print(f"Compare A: {format_data(choiceA)}")
    print(art.vs)
    print(f"Against B: {format_data(choiceB)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    choiceA_follower_count = choiceA['follower_count']
    choiceB_follower_count = choiceB['follower_count']
    is_Correct = decision(guess, choiceA_follower_count, choiceB_follower_count)

    if is_Correct:
        score += 1
        print(f"Your Right! Current Score: {score}.")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        isPlaying = False
