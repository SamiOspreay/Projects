
The_Animal = "Tiger"
The_number = "5"
guess_animal = ""
guess_number = ""
guess_count = 0
guess_limit = 5
guess_limit_ends = False
score = 0

while guess_animal != The_Animal and not(guess_limit_ends):
     if   guess_count < guess_limit :
      guess_animal = input("Guess the Animal: ")
      
      guess_count += 1 
     
     else:  
      guess_limit_ends = True  
      
while guess_number != The_number and not(guess_limit_ends):
     if   guess_count < guess_limit :
      guess_number = input("Guess the Number: ")
      
      guess_count += 1
      
     else:  
      guess_limit_ends = True
if guess_animal == The_Animal:
    score = score + 5
if guess_number == The_number:
    score = score + 5
if guess_limit_ends:
    print("You lost")
    print("Your score is:",score)
else:
    print("Congratulations You Win")
    print("Your score is:",score)
    