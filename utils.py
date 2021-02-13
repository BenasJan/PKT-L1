from friend import Friend

def getFriendsCountInFriendNetwork(network: [], alreadyAddedFriendNames: list = [], shouldReset = True) -> int:
    if shouldReset:
        alreadyAddedFriendNames = []

    allSubfriendsFromNetWork: list = []
    for friend in network:
        allSubfriendsFromNetWork += friend.friends

    alreadyAddedFriendNames += map(lambda fr: fr.name, network)
    alreadyAddedFriendNames += map(lambda fr: fr.name, allSubfriendsFromNetWork)
    alreadyAddedFriendNames = list(set([name for name in alreadyAddedFriendNames]))

    allSubfriendsDeeper: list = []
    for friend in allSubfriendsFromNetWork:
        allSubfriendsDeeper += friend.friends

    for aafn in alreadyAddedFriendNames:
        allSubfriendsDeeper = list(filter(lambda fr : fr.name != aafn, allSubfriendsDeeper))

    count = len(list(alreadyAddedFriendNames))

    if len(allSubfriendsDeeper) > 0:
        return getFriendsCountInFriendNetwork(allSubfriendsFromNetWork, alreadyAddedFriendNames, False)
    else:
        return count

def printAllFriends(friends: []):
    for friend in friends:
        print('%s has these friends:' %(friend.name))
        friendsOfFriend = friend.friends
        for friendOfFriend in friendsOfFriend:
            print('%s' %(friendOfFriend.name))