score = int(input(' Enter the score, score = '))
bon = 0
res = 0
if score < 100:
    bon = 5
elif score < 1001:
    bon = score * 0.2
elif score > 1000:
    bon = score * 0.1

if score % 2 == 0:
    bon = bon + 1
    res = score + bon
elif (score / 5 ) % 2 == 1:
    bon = bon + 2
    res = score + bon
else:
    bon = bon + 0
    res = score + bon
print(str(bon) + '\n' + str(res))
