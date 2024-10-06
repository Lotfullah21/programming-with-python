# It creates an infinite loop
while True:
    text = input("Enter a text: ")
    if text.lower() == "exit":
        print("Exiting the loop")
        # Break out of the loop and execute the code after the loop if there is any.
        break
    print("Your text:",text)
        