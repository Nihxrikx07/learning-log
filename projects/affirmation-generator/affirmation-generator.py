import random
affirmations = ["You are doing better that you think","Small steps still move you forward.","You are allowed to grow at your own pace.", "Your effort matters today","You are becoming stronger everyday.", "You don't need to have it all figured out.",
"Consistency is already changing you.",
"You are allowed to start small.","You are an amazing human being","Be kind to yourself","You have all the Power "]
def give_affirmationns(name):
    message=random.choice(affirmations)
    print(f"\n {name},{message}")
def affirmation_app():
    print("Welcome to the Affirmation Generator")
    name=input("What is your name? ").strip()
    while True:
        input("\n Press Enter to receive affirmation...")
        give_affirmationns(name)
        again = input("\n Would you like another one? (yes/no) : ")
        if again != "yes":
            print("Have an excellent day!!!")
            break
affirmation_app()