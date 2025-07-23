#this is how you can nest for loops, one inside the other! These loop through all the colors, 
# and then through all the characters in the color string
colors = ['red','orange','green','lime green','blue','cyan','indigo','magenta','purple','black','white']

for color in colors:
#for all the colors:
    print(color)
    for c in color:
        print(" - " + c) #log each letter. Remember, a string is also an array of characters.


RED = '\33[31m'
GREEN = '\33[32m'
BLUE = '\33[34m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\33[37m'
BOLD = '\33[1m'
RESET = '\33[0m'


for i in range(1,10):
    
    print(RED+"I love tomato")
    print(GREEN+"I love broccoli")
    print(BLUE   +" I love men")
    print(RESET+ ";)")
    

    
    