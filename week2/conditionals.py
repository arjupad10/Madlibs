RED = '\33[31m'
GREEN = '\33[32m'
BLUE = '\33[34m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\33[37m'
BOLD = '\33[1m'
RESET = '\33[0m'

age = 15
if age >=10 and age <=15:
    print(BOLD + 'You can buy a helicopter')
else:
    print(RED +'You cannot buy a helicopter')

if age==15:
    print(RESET+'You can buy a GREEN helicopter')