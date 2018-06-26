number = int(input())
digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
rounds = [ 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one-hundred']
tens = ['eleven', 'twelve', 'thirteen', 'fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

nummodten = number % 10
numdivten = int(number / 10)
moddivten = numdivten % 10
if number >=0 and number <= 10:
    print(digits[number])
elif number >=11 and number <=19:
    print(tens[number - 11])
elif number > 19 and number <=100:
    if nummodten == 0:
        print(rounds[numdivten-2])
    else:
        print( str( rounds[moddivten-2] + ' ' + str(digits[nummodten])))
else:
    print('invalid number')




