print('How many cats do you have')
numCats = input()
try:
    if int(numCats) >= 4:
        print('That is a lot of cats.')
    elif int(numCats) < 0:
        print('You can not enter a neg. number of cats')
    elif int(numCats)> 0 and int(numCats)< 4:
        print ('That is not that many cats.')
except ValueError:
    print('You need to enter a number. Example 1, 2, 3, 4, or 5')
