hour = int(input())
minets = int(input())

addMinets = minets + 15
addHour = hour
if addMinets > 59:
    addHour = hour + 1
    addMinets = addMinets - 60
    if addHour >= 24:
        addHour = addHour - 24
if addMinets < 10:
    print(str(addHour) + ':0' + str(addMinets))
else:
    print(str(addHour) + ':' + str(addMinets))