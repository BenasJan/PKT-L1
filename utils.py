from friend import Friend

def doesFriendExist(friends: [Friend], friendToCheck: Friend) -> bool:
    for friend in friends:
        if friend.name == friendToCheck.name:
            return True

    return False