Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
... # Available options
... options = ["Rock", "Paper", "Scissors"]
... 
... # User input
... user_choice = input("Choose Rock, Paper, or Scissors: ").lower()
... 
... # Computer selection
... computer_choice = random.choice(options)
... 
... # Print computer's choice
... print(f"Computer chose: {computer_choice}")
... 
... # Game logic
... if user_choice == computer_choice:
...         print("It's a tie!")
... elif (user_choice == "rock"
...  
... and computer_choice == "scissors") or \
...     (user_choice == "paper"
...  
... and computer_choice == "rock") or \
...     (user_choice == "scissors"
...  
... and computer_choice == "paper"):
...     print("You win!")
... else:
