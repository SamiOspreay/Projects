
The_Animal = "Tiger"
guess = ""
guess_count = 0
guess_limit = 2
guess_limit_ends = False

while guess != The_Animal and not(guess_limit_ends):
     if   guess_count < guess_limit :
      guess = input("Guess the Animal: ")
      guess_count += 1 
     else:  
      guess_limit_ends = True  
if guess_limit_ends:
    print("You lost")
else:
    print("Congratulations You Win")
