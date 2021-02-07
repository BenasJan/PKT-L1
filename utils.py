from friend import Friend

def doesFriendExist(friends, friendToCheck):
    for friend in friends:
        if friend.name == friendToCheck.name:
            return True

    return False