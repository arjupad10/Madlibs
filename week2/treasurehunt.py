import random

print("🏴‍☠️ Welcome to the Treasure Hunt Adventure! 🏴‍☠️")
print("=" * 50)

# Get player's name
player_name = input("What's your name, brave adventurer? ")
print(f"Hello, {player_name}! Let's start your treasure hunt!")

# Create lists for game data
locations = [
    "Mysterious Cave", # <-- Notice the comma
    "Ancient Forest", 
    "Dragon's Lair", 
    'Crystal Cove',
    'Pleasant Park'
    ] # Add more if you wish!

treasures = [
    "Golden Coin",
    "Nothing here!",
    "Silver Sword",
    "1/1 Iced out LeBron",
    "Magic Jewel"
    ] # Add more/ if you wish!

# The treasure in index 0 corresponds to the location in index 0, and so on

# Optional:
# If you want multiple treasures in ONE room, use a list INSIDE the treasures list

# Optional: You may want a list of whether the user has visited that room yet
# The boolean in index 0 corresponds to the location in index 0, and so on
tracker = [False, False, False, False, False]

# Here's some inventory to keep track of the objects your player has gathered
player_inventory = []
pickup = ""
# You may want to start by printing out the locations and prompting
# the user for input...
while len(player_inventory) != len(locations):
    print('\n')
    for i in locations: print(i)
    locations_input = input("Choose a location to search: ")
    if locations_input not in locations: 
        print("Nuh uh uh! That is not a real place.")
    else:
        if tracker[locations.index(locations_input)]==False:
            pickup = random.choice(treasures)
            print("You found...\n" + pickup)
            player_inventory.append(pickup)
            
            tracker[locations.index(locations_input)]=True
        else:
            print("You already went there bruv.. Nothin to see here ;)")
    
    if len(player_inventory)==len(locations):
        print("Game Over.")
        break
# Think about the main loop for gameplay. Did you want a for-loop that
# explores each room in order? Did you want a while-loop that keeps looping
# until some condition is reached? Your choice...