#This program that determines the award a person competing in a triathlon will receive

#Colour and features to add to the output messages
PINK = '\033[95m'
BLUE = '\033[94m'
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

#Welcoming message
print(f"Welcomea all merry men, women and gender diverse humans to the {BOLD}{UNDERLINE}Nottingham Annual {GREEN}Robin Hood {WHITE}{BOLD}{UNDERLINE}Triathlon!")

#Getting input from the user
print(F"{WHITE}Can you give us the times in minutes for all three events please?")
swimming = float(input("Swimming: "))
cycling = float(input("Cycling: "))
running = float(input("Running: "))

#Calculating the total time taken to complete the triathlon
triathlon = swimming + cycling + running

#Displaying the total time of the triathlon
print(f"It took you just {round(triathlon, 2)} min to complete the triathlon my good fellow! {BOLD}{YELLOW}Just about right {WHITE}and")

#Determining award for the participant and printing the output message
qualifying_time = 100
if triathlon <= qualifying_time:
    print(f"{BLUE}{BOLD}CONGRATULATIONS!!! {WHITE}You {RED}{BOLD}WON {GREEN}{UNDERLINE}Provincial {UNDERLINE}{CYAN}C{UNDERLINE}{BLUE}O{UNDERLINE}{PINK}L{UNDERLINE}{RED}O{UNDERLINE}{YELLOW}U{UNDERLINE}{GREEN}R{UNDERLINE}{BLUE}S{UNDERLINE}{CYAN}!")
elif triathlon <= (qualifying_time + 5):
    print(f"{BLUE}{BOLD}Well done! {WHITE}You {RED}{BOLD}WON {GREEN}{UNDERLINE}Provincial Half {UNDERLINE}{CYAN}COLO{UNDERLINE}{YELLOW}URS!")
elif triathlon <= (qualifying_time + 10):
    print(f"{BLUE}{BOLD}Nice effort! {WHITE}You {RED}{BOLD}WON {BOLD}{UNDERLINE}{GREEN}Provincial Scroll")
else:
    print(f"{WHITE}Sorry, better luck next time!")
