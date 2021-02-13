def getFriendsCountInFriendNetwork(network: [], alreadyAddedFriendNames: list = [], shouldReset=True) -> int:
    if shouldReset:
        alreadyAddedFriendNames = []

    allSubFriendsFromNetWork: list = []
    for friend in network:
        allSubFriendsFromNetWork += friend.friends

    alreadyAddedFriendNames += map(lambda fr: fr.name, network)
    alreadyAddedFriendNames += map(lambda fr: fr.name, allSubFriendsFromNetWork)
    alreadyAddedFriendNames = list(set([name for name in alreadyAddedFriendNames]))

    allSubFriendsDeeper: list = []
    for friend in allSubFriendsFromNetWork:
        allSubFriendsDeeper += friend.friends

    for alreadyAddedFriendName in alreadyAddedFriendNames:
        allSubFriendsDeeper = list(filter(lambda fr: fr.name != alreadyAddedFriendName, allSubFriendsDeeper))

    count = len(list(alreadyAddedFriendNames))

    if len(allSubFriendsDeeper) > 0:
        return getFriendsCountInFriendNetwork(allSubFriendsFromNetWork, alreadyAddedFriendNames, False)
    else:
        return count


def printAllFriends(friends: []):
    for friend in friends:
        print('%s has these friends:' % friend.name)
        friendsOfFriend = friend.friends
        for friendOfFriend in friendsOfFriend:
            print('%s' % friendOfFriend.name)
