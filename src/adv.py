from room import Room
from player import Player
from item import Item

# Declare all the rooms

item = {
    "screwdriver":  Item("Screwdriver", "This might come in handy"),
    "rope":         Item("Rope", "Looks sturdy enough"),
    "knife":        Item("Rusty Knife", "It's still sharp"),
    "canteen":      Item("Canteen", "Damn, it's empty!"),
    "torch":        Item("Torch", "Hope you have matches"),
    "map":          Item("Map", "Has a red X marked on it"),
    "key":          Item("Key", "I might need this later"),
    "matches":      Item("Matches", "Only three left in the box"),
    "fedora":       Item("Well Worn Fedora", "Indiana Jones may have dropped his hat")
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["fedora"].name]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["screwdriver"].name, item["torch"].name]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["matches"].name, item["rope"].name]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["map"].name, item["key"].name]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["key"].name, item["canteen"].name]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# player object
player = Player(input("Enter name --> "), room["outside"], [])

def confirm_quit(confirm):
    if (confirm == "y"):
        print("Thanks for the adventure. Bye!")
        exit()
    elif confirm == "N":
        pass
    elif len(confirm) == 0:
        pass
    else:
        print("Choices are [y] or [N]. Please try again\n")

while True:
    cmd = input("[n] North [e] East [s] South [w] West [q] Quit\n")
    direction = cmd[0]
    if cmd == "q":
        confirm = input("Are you sure you want to quit? [yN]\n")
        confirm_quit(confirm)
    elif direction in ("n", "e", "s", "w"):
        player.travel(direction)
    
