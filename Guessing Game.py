
The_Animal = "Tiger"
The_number = "5"
guess_animal = ""
guess_number = ""
guess_count = 0
guess_limit = 5
guess_limit_ends = False
score = 0
question_1 = "Apple"
Answer_1 = ""
question_2 = "Eye of the tiger"
Answer_2 = ""
question_3 = "1975"
Answer_3 = ""
question_4 = "300"
Answer_4 = ""
question_5= "780"
Answer_5 = ""
question_6= "a"
Answer_6 = ""


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

   
print ("Questions Part")
print ("What is the name of the company that iPhone belongs to?")
while Answer_1 != question_1 and not(guess_limit_ends):
     if   guess_count < guess_limit :
      Answer_1 = input("Answer: ")

print ("What is the signature song of Rocky 3?")
while Answer_2 != question_2 and not(guess_limit_ends):
     if   guess_count < guess_limit :
      Answer_2 = input("Answer: ")
      
      guess_count += 1
    
print ("When was Mcirosoft founded?")
while Answer_3 != question_3 and not(guess_limit_ends):
     if   guess_count < guess_limit :
      Answer_3 = input("Answer: ")
      
      guess_count += 1

print("Math Part")

print ("75*4")
while Answer_4 != question_4 and not(guess_limit_ends):
     if   guess_count < guess_limit :
      Answer_4 = input("Answer: ")

print ("(50*6) - (4*5)")
while Answer_5 != question_5 and not(guess_limit_ends):
     if   guess_count < guess_limit :
      Answer_5 = input("Answer: ")

print("close ended question")  

print ("(50*6) - (4*5)")

print ("Where is the capital city of France")    
print("a. Paris")
print("b. Marsielle")
print("c. Lyon")

Answer_6 = input("Answer: ")
if Answer_6 == question_6:
    score = score + 5
   
     
if Answer_1 == question_1:
    score = score + 5

if Answer_2 == question_2:
    score = score + 5

if Answer_3 == question_3:
    score = score + 5

if Answer_4 == question_4:
    score = score + 5

if Answer_5 == question_5:
    score = score + 5





if guess_limit_ends:
    print("You lost")
    print("Your score is:",score)
else:
    print("Congratulations You Win")
    print("Your score is:",score)
    