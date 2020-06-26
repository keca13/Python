def printPicnic(itemsDict, leftWidth, rightWidth):
    print('NA PIKNIK'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'kanapki': 4, 'jabłka': 12, 'kubki': 4, 'ciastka': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
