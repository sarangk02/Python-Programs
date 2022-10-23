
# Rock Beats Scissor
# Paper Beats Rock
# Scissor Beats Paper


import numpy as np
 
print("1 - Rock")
print("2 - Paper")
print("3 - Scissor")

p1 = int(input("Pick a number - "))

p2 =  np.random.randint(1,4)
if p2 == 1:
    print("Opponent choosed Rock")
elif p2 == 2:
    print("Opponent choosed Paper")
else :
    print("Opponent choosed Scissor") 


if (p1 == 1 and p2 == 3) or (p1 == 2 and p2 == 1) or ( p1 == 3 and p2 == 2):
    print("You win !!!")
elif p1 == p2:
    print("Oops! It's a draw.")
else :
    print("You lost :(")




