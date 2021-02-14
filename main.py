from friend import Friend
from utils import printAllFriends
from utils import getFriendsCountInFriendNetwork

allFriends = []
inputFile = open('./data/friends3.txt', 'r')

allLines = inputFile.read().splitlines()

for line in allLines:
    names = line.split(' ')
    firstFriend = Friend(names[0])
    secondFriend = Friend(names[1])

    firstFriendIndex = next((i for i, friend in enumerate(allFriends) if friend.name == firstFriend.name), -1)
    secondFriendIndex = next((i for i, friend in enumerate(allFriends) if friend.name == secondFriend.name), -1)

    if firstFriendIndex > -1:
        if secondFriendIndex > -1:
            allFriends[firstFriendIndex].addFriend(allFriends[secondFriendIndex])
            allFriends[secondFriendIndex].addFriend(allFriends[firstFriendIndex])
        else:
            secondFriend.addFriend(allFriends[firstFriendIndex])
            allFriends[firstFriendIndex].addFriend(secondFriend)
            allFriends.append(secondFriend)
    else:
        if secondFriendIndex > -1:
            firstFriend.addFriend(allFriends[secondFriendIndex])
            allFriends[secondFriendIndex].addFriend(firstFriend)
            allFriends.append(firstFriend)
        else:
            firstFriend.addFriend(secondFriend)
            secondFriend.addFriend(firstFriend)
            allFriends.append(firstFriend)
            allFriends.append(secondFriend)

    if firstFriendIndex > -1:
        count = getFriendsCountInFriendNetwork([allFriends[firstFriendIndex]])
    elif secondFriendIndex > -1:
        count = getFriendsCountInFriendNetwork([allFriends[secondFriendIndex]])
    else:
        firstFriendIndex = next((i for i, friend in enumerate(allFriends) if friend.name == firstFriend.name), -1)
        count = getFriendsCountInFriendNetwork([allFriends[firstFriendIndex]])
    
    print(count)

# printAllFriends(allFriends)
inputFile.close()
