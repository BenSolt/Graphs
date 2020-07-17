from room import Room
from player import Player
from world import World

import random
from ast import literal_eval



# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "./projects/adventure/maps/test_line.txt"
# map_file = "./projects/adventure/maps/test_cross.txt"
# map_file = "./projects/adventure/maps/test_loop.txt"
# map_file = "./projects/adventure/maps/test_loop_fork.txt"
map_file = "./projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk 
# traversal_path = ['n', 'n']
traversal_path = []
# MY CODE ====================================================

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

# directions N,S,W,E
# return opposite of current direction.(move)
# EXAMPLE - if move is "north" then return "south".

def backwords(move):
    if move == "n":
        return "s"
    if move == "s":
        return "n"
    if move == "w":
        return "e"
    if move == "e":
        return "w"

def dft_traversal(traversal_path):

    visited_rooms = set()
    s = Stack()
    s.push(0)

    #while length of rooms visited is less than length of total rooms.
    while len(visited_rooms) < len(room_graph):

        current_room = s.stack[-1]

        #add current room to set
        visited_rooms.add(current_room)
        
        next_room = room_graph[current_room][1]
        
        # empty array/list
        not_visited = []

        print(f"\033[1;34mCURRENT ROOM:\033[0m {current_room}")
        

        # move in direction of room in next_room
        for move, room in next_room.items():
            #if room is not in visited rooms
            if room not in visited_rooms:
                # add room and move 
                not_visited.append((room, move))
        #if length of not visited greater than 0
        if len(not_visited) > 0:
            #add not_visited onto stack, room, move
            s.push(not_visited[0][0])
            #attach not visited to traversal path, room. direction plus 1?
            traversal_path.append(not_visited[0][1])
        else:
            #remove from stack
            s.pop()
            
            for move, room in next_room.items():
                # if room value is equal to value of stack
                if room == s.stack[-1]:
                    # get traverasal and add direction
                    traversal_path.append(move)

    #remove from traveral
    traversal_path.pop()

dft_traversal(traversal_path)


# TRAVERSAL TEST========================================

visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



# #######
# # UNCOMMENT TO WALK AROUND
# #######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
