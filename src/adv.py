from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
p1 = Player("John Snow", room["outside"])

def confirm_quit(confirm):
    if (confirm == "y"):
        print("Thanks for playing. Bye!")
        exit()
    elif confirm == "N":
        pass
    elif len(confirm) == 0:
        pass
    else:
        print("Choices are [y] or [N]. Please try again\n")

def player_move(player, direction):
    next_room = getattr(player.current_room, f"{direction}_to")
    if next_room is not None:
        player.current_room = next_room
        print("You're on to the next room, Good luck")
    else:
        print("Oh no, you hit a dead-end. Try again!")

while True:
    print(f"Your current room: {p1.current_room.name}")
    print(f"Room description: {p1.current_room.description}")
    cmd = input("[n] North [e] East [s] South [w] West [q] Quit\n")
    if cmd == "q":
        confirm = input("Are you sure you want to quit? [yN]\n")
        confirm_quit(confirm)
    if cmd in ["n", "e", "s", "w"]:
        player_move(p1, cmd)
