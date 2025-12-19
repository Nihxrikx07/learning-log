print("Helloo Welcome to the Mood Checker...")
name = input("What is your name? ")
print(f"Hey {name}, Glad you are here!")
valid_moods = ["happy","sad","angry","tired"]
while True:
    mood = input("How are you feeling today? : ").strip().lower()
    if not mood:
        print("It looks like you didn't type anything. That's Okay - take your time...")
    elif not mood.isalpha():
        print("That doesn't look like a feeling word.")
        print("If you'd like, you can try words like : happy, sad, tired, angry")
    elif mood in valid_moods:
        if mood == "happy":
            print("That's Beautiful.. Keep Enjoying the moment!!")
        elif mood == "sad":
            print("It is okay to feel sad sometimes, take things gentle today..")
        elif mood == "tired":
            print("Rest is productive too, Be gentle to yourself")
        elif mood == "angry":
            print("Take a deep breath. This feeling will pass.")
    else:
         print("Thank you for sharing. Whatever you feel is valid")
    again = input("Do you want to chech another mood? (yes/no) ").strip().lower()
    if again != "yes":
        print("Thankyou for checking in with yourself today.")
        break