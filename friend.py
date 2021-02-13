class Friend:
    def __init__(self, name):
        self.name = name
        self.friends = [Friend]

    def addFriend(self, friend):
        self.friends.append(friend)