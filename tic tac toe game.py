import numpy as np
import sys
print("Menu:")
print("1.Start\n2.Exit\n")
print("enter choice")
choice=int(input( ))
if choice==1:
    print("player vs player")
    game=np.zeros((3,3)).astype(int)
    name1=input("enter name1:")
    print("player 1 is "+name1)
    print()
    name2=input("enter name2:")
    print("player 2 is "+name2)
    print()
    print("Enter values between 0 and 2 for the position coordinates\n")
   
    def move(char):
      if char=='1':
         name=name1
      elif char=='5':
         name=name2
      print("{}'s turn".format(name))
      m=int(input( ))
      n=int(input( ))
      if game[m, n]==0:
           game[m, n]=char
           print(game)
           if win(char):
              print("Congratulations!!!{} won".format(name))
              sys.exit()
              
           elif draw():
               print("Draw match")
               sys.exit()
      else:
         print("Already taken! Enter a different number")
         move(char)
    
    def win(char):
        if any(np.sum(game, 1)==3) or any(np.sum(game, 0)==3) or sum(np.diag(game))==3 or sum(np.diag(game[::-1]))==3:
           return True
        if any(np.sum(game, 1)==15) or any(np.sum(game, 0)==15) or sum(np.diag(game))==15 or sum(np.diag(game[::-1]))==15:
           return True
        return False
    
    def draw():
       if 0 not in game:
          return True
       else:
          return False

    while True:
        move("1")
        move("5")
              
else:
    print("exited game")
    sys.exit()














