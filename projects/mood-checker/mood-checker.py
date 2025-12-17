name = input("What is your name? ")
print(f"Hey {name}, Glad you are here!")
mood = input("How are you feeling today? (Happy,Sad,Tired,Okay) : ").lower()
if mood == "happy":
    print("That's Beautiful.. Keep Enjoying the moment!!")
elif mood == "sad":
    print("It is okay to feel sad sometimes, take things gentle today..")
elif mood == "tired":
    print("Rest is productive too, Be gentle to yourself")
elif mood == "okay":
    print("Sometimes Okay is enough")
else:
    print("Thank you for sharing. Whatever you feel is valid")