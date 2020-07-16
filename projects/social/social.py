import random

# MY CODE added queue class

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)


class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users
        # MY CODE 
        for i in range(0, num_users):
            self.add_user(f"User {i}")

        # Create friendships
        # MY CODE
        possible_friendships = []
        # MY CODE
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id +1):
                possible_friendships.append((user_id, friend_id))
        #MY CODE
        #shuffle possible friendships
        random.shuffle(possible_friendships)

        #create friendships
        #divive by 2 since each add friendships creates 2 friends.(friends with each other)
        for i in range(num_users * avg_friendships //2):
                                # index location
            friendship = possible_friendships[i]
                                #first, second
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        
        #MY CODE
        
        # make a queue
        q = Queue()
        # enqueue our starting node
        q.enqueue([user_id])
       

        # while our queue is not empty
        while q.size() > 0:
            # dequeue whatever is at the front of our line, this is our current_node
            current_path = q.dequeue()
            current_user = current_path[-1]

            if current_user not in visited:

                visited[current_user] = current_path

                for i in self.friendships[current_user]:
                    if i not in visited:
                        new_node = list(current_path)
                        new_node.append(i)
                        q.enqueue(new_node)

        return visited

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)

    #sg.populate_graph(10, 2)
# waht percentage of tatl users are in our extended social network?
# how many people we know, divided by how many people there are

#print(f'{len(connections)-1 / 1000 * 100}%)

# total_lengths = 0
# for friend in connections:
#     total_length += len(connections[friend])

#print(f'Average degree of seperation: {total_lengths / len(connections)}')

# what is the average degree of speration between a user and those in his/her extended network?
