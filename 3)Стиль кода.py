MyList = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# i = 0
# while MyList[i] >= 0:
#    if MyList[i] == 0:
#        i += 1
#        if i == len(MyList):
#          break
#    else:
#       print(MyList[i])
#       i += 1
#       if i == len(MyList):
#           break

i = -1
while (i+1) < len(MyList):
    i += 1
    if MyList[i] < 0:
        break
    elif MyList[i] > 0:
        print(MyList[i])
    else:
        continue

# Я написал два кода, тк я не понял смысла использования continue
# Обьясните пожалуйста, зачем он здесь, если без него все прекрасно работает
# Да и впринципе я не выкупил смысла его существования