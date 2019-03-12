import random
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
        return (len(self.queue))

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        

        # Add users
        # create users
        for i in range(numUsers):
            self.addUser(f' User #{i+1}')

        friendships = []
        friends_left = numUsers*avgFriendships
        total_friends = numUsers*avgFriendships


        # generate num of friendships for each user
        for i in range(numUsers):
            if friends_left > 0:
                friends = round(random.random()*(avgFriendships*2))
                friends_left -= friends
                friendships.append(friends)
            elif friends <= 0:
                friendships.append(0)

        while sum(friendships) < total_friends:
            print('adding more')
            for i in range(len(friendships)):
                if friends_left:
                    friendships[i] += 1
                    friends_left -= 1

        while sum(friendships) > total_friends:
            print('adding more')
            for j in range(len(friendships)):
                if friends_left:
                    friendships[j] -= 1
                    friends_left += 1

        # Create friendships
        for user in self.users:
            if len(friendships) > user-1:
                if friendships[user-1]:
                    for new_friend_index in range(len(friendships)):
                        if friendships[new_friend_index] == friendships[user-1]:
                            pass
                        elif friendships[new_friend_index] and friendships[user-1]:
                            self.addFriendship(user, new_friend_index)
                            friendships[new_friend_index] -= 1
                            friendships[user-1] -= 1
                            

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        '''
        for each user find path to userID
        use a shortest path algo on each user
        '''
        for u in self.users:
            # print(u)
            path = self.bfs(u, userID)
            if path:
                visited[u] = path
        return visited

    def bfs(self, starting_vertex_id, target=None):

        q = Queue()
        # create an empty list (set) of visted vertices
        # visted = set()

        # list that will record the path taken
        paths = []
        subpath = []
        prev = None
        # put the starting vertex in our Queue
        q.enqueue([starting_vertex_id])
        counter = 0
        depth = 0
        while q.size() > 0:
            # dequeue the first subpath from the queue
            v = q.dequeue()
  
            depth += 1
            # mark it as visted 
            # visted.add(v)
            # print(v)
            # then put all of its neighbors into the queue
            for neighbor in self.friendships[v[-1]]:
                subpath = []
                subpath = v.copy()
                if neighbor not in subpath:
                    subpath.append(neighbor)
                    if subpath[-1] == target:
                        # print(f'shortest path: {subpath}')
                        return subpath
                    # path.append(v)
                    q.enqueue(subpath)
            # prev = v
            # counter += 1
            
        # print(paths)
        return None

if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)
