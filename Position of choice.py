print("Welcome to  The  GAME!")
x=" position of choice "
print(x)
name=input("what is your name ?")

age=input("what is your age?")
health=99
print("you are starting with",health,"health")
is_older= int (age) >=18
print(is_older) 
if int(age)>=18:
  print("you are eligible") 
   
  wants_to_play=input ("do you want to play")
  if wants_to_play=="yes":
     print("lets play")
  
  up_or_down=input("first choice...... up or down(up/down)?")     
  if up_or_down == "down":
      ans=input("you have chosen the soccer team would you like to be the striker or midfielder(striker/left winger)?")
      if ans=="striker":
        print("you are in the center ")
      elif ans=="left winger" :
       print("you are on the left side ") 
  ans=input("you have the choice to shoot the ball to the top or bottom(top/bottom)?")
  if  ans=="top":
              print("you have chose to shoot the ball to the top and have missed the opportunity ")
              health-=99
              if health<=0:
                    print("you have lost the game") 
              else: 
                print("you  have won the game ")       

  
                                                  
                     
else:
  print("you do not meet the requirement") 
