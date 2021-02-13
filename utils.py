def getFriendsCountInFriendNetwork(network: [], alreadyAddedFriendNames: list = [], shouldReset=True) -> int:
    if shouldReset: alreadyAddedFriendNames = []

    allFriendsFromNetWork: list = getFriendsOfFriends(network)
    allSubFriendsDeeper: list = getFriendsOfFriends(allFriendsFromNetWork)

    alreadyAddedFriendNames += map(lambda fr: fr.name, network)
    alreadyAddedFriendNames += map(lambda fr: fr.name, allFriendsFromNetWork)
    alreadyAddedFriendNames = list(set([name for name in alreadyAddedFriendNames]))

    for alreadyAddedFriendName in alreadyAddedFriendNames:
        allSubFriendsDeeper = list(filter(lambda fr: fr.name != alreadyAddedFriendName, allSubFriendsDeeper))

    count = len(list(alreadyAddedFriendNames))

    if len(allSubFriendsDeeper) > 0:
        return getFriendsCountInFriendNetwork(allFriendsFromNetWork, alreadyAddedFriendNames, False)
    else:
        return count


def getFriendsOfFriends(friends: []) -> list:
    friendsOfFriends: list = []

    for friend in friends:
        friendsOfFriends += friend.friends
    
    return friendsOfFriends


def printAllFriends(friends: []):
    for friend in friends:
        print('%s has these friends:' % friend.name)
        friendsOfFriend = friend.friends
        for friendOfFriend in friendsOfFriend:
            print('%s' % friendOfFriend.name)