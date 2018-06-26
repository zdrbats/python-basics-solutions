time1 = int(input())
time2 = int(input())
time3 = int(input())

sum = time1 + time2 + time3
sek = 0
min = 0

if sum <= 59 and sum >= 0:
    min = 0
    sek = sum
    if sek < 10:
        print(str(min) + ':0' + str(sek))
    else:
        print(str(min) + ':' + str(sek))
elif sum >=60 and sum <= 119:
    min = 1
    sek = sum - 60
    if sek < 10:
        print(str(min) + ':0' + str(sek))
    else:
        print(str(min) + ':' + str(sek))
elif sum >=120 and sum <=179:
    min = 2
    sek = sum - 120
    if sek < 10:
        print(str(min) + ':0' + str(sek))
    else:
        print(str(min) + ':' + str(sek))
