def get_mood_response(mood):
    mood_response = {"happy" : "That's Beautiful.. Keep Enjoying the moment!", "sad":"It is okay to feel sad sometimes, take things gentle today..", "tired":"Rest is productive too, Be gentle to yourself",
    "angry":"Take a deep breath. This feeling will pass."}
    if not mood: 
        return "You didn't type anything and that's okey, take your time.."
    if not mood.isalpha():
        return "That doesn't look like a feeling word.\n"
        "Whatever you're feeling is still valid."
    return mood_response.get(mood,"Whatever you are feeling is still valid!")

def mood_checker():
    print("Helloo Welcome to the Mood Checker...")
    name = input("What is your name? ")
    print(f"Hey {name}, Glad you are here!")
    while True:
        mood = input("How are you feeling today? (type 'quit' to exit) : ")
        if mood in ["exit","quit"]:
            print("\n Thankyou for checking in with yourself today ")
            break

        response = get_mood_response(mood)
        print(response)
        print("-"*40)


def main():
    mood_checker()



if __name__ == "__main__":
    main()