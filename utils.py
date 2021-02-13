from friend import Friend

def doesFriendExist(friends: [Friend], friendToCheck: Friend) -> bool:
    for friend in friends:
        if friend.name == friendToCheck.name:
            return True

    return False

def getUniqueFriends(friends: [Friend]) -> [Friend]:
    uniqueFriends = [Friend]
    
    for friend in friends:
        if doesFriendExist(uniqueFriends, friend) == False:
            uniqueFriends.append(friend)

    return uniqueFriends

def getFriendsCountInFriendNetwork(friend1: Friend, frined2: Friend) -> int:
    allFriends = []
    allFriends += friend1.friends
    allFriends += frined2.friends

    uniqueFriends = getUniqueFriends(allFriends)

    return uniqueFriends.count()

def printAllFriends(friends: [Friend]):
    for friend in friends:
        print('%s has these friends:' %(friend.name))
        friendsOfFriend = friend.friends
        for friendOfFriend in friendsOfFriend:
            print('%s' %(friendOfFriend.name))