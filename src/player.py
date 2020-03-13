# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room, inventory):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    # def __str__(self):
        # return f"Current room: {self.current_room}"
    def travel(self, direction):
        next_room = getattr(self.current_room, f"{direction}_to")
        if next_room is not None:
            self.current_room = next_room
            print("You're on to the next room, Good luck")
            print(f"Current room: {self.current_room}")
        else:
            print("Oh no, you hit a dead-end. Try again!")

