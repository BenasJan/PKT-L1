from friend import Friend
from utils import doesFriendExist
from utils import printAllFriends

allFriends = []
inputFile = open('./friends.txt', 'r')

allLines = inputFile.read().splitlines()

for line in allLines:
    names = line.split(' ')
    firstFriend = Friend(names[0])
    secondFriend = Friend(names[1])

    firstFriend.addFriend(secondFriend)
    secondFriend.addFriend(firstFriend)

    if doesFriendExist(allFriends, firstFriend) == False:
        allFriends.append(firstFriend)
    else:
        index = next((i for i, friend in enumerate(allFriends) if friend.name == firstFriend.name), -1)
        if index > -1:
            allFriends[index].addFriend(secondFriend) 

    if doesFriendExist(allFriends, secondFriend) == False:
        allFriends.append(secondFriend)
    else:
        index = next((i for i, friend in enumerate(allFriends) if friend.name == secondFriend.name), -1)
        if index > -1:
            allFriends[index].addFriend(firstFriend)

printAllFriends(allFriends)




# from human import Human

# ageSum = 0
# humans = []
# peopleFile = open('./people.txt', 'r')

# allLines = peopleFile.readlines()
# for line in allLines:
#     humans.append(Human(line))

# for human in humans:
#     print(human.name)
#     print(human.surname)
#     print(human.age)
#     print('')
#     ageSum += human.age

# print('Total age: %s' %(ageSum))

# peopleFile.close()

