size = float(input())
inUnit = input()
outUnit = input()

res = 0

meterInMM = 1000
meterInCM = 100
meterInMi = 0.0006213
meterInInc = 39.3700
meterInKm = 0.001
meterInFt = 3.2808
meterInYd = 1.0936

MMinCM = meterInCM/meterInMM
MMinMI = meterInMi/meterInMM
MMinInc = meterInInc/meterInMM
MMinKM = meterInKm/meterInMM
MMinFt = meterInFt/meterInMM
MMinYd = meterInYd/meterInMM

CMinMi = meterInMi/meterInCM
CMinInc = meterInInc/meterInCM
CMinKm = meterInKm/meterInCM
CMinFt = meterInFt/meterInCM
CMinYd = meterInYd/meterInCM

MiInInc = meterInInc/meterInMi
MiInKm = meterInKm/meterInMi
MiInFt = meterInFt/meterInMi
MiInYd = meterInYd/meterInMi

IncInKm = meterInKm/meterInInc
IncInFt = meterInFt/meterInInc
IncInYd = meterInYd/meterInInc

KMInFt = meterInFt/meterInKm
KMInYd = meterInYd/meterInKm

FtInYd = meterInYd/meterInFt

if inUnit == 'm':
    if outUnit == 'mm':
        res = size * meterInMM
    elif outUnit == 'cm':
        res = size * meterInCM
    elif outUnit == 'mi':
        res = size * meterInMi
    elif outUnit == 'in':
        res = size * meterInInc
    elif outUnit == 'km':
        res = size * meterInKm
    elif outUnit == 'ft':
        res = size * meterInFt
    elif outUnit == 'yd':
        res = size * meterInYd
elif inUnit == 'mm':
    if outUnit == 'm':
        res = size / meterInMM
    elif outUnit == 'cm':
        res = size * MMinCM
    elif outUnit == 'mi':
        res = size * MMinMI
    elif outUnit == 'in':
        res = size * MMinInc
    elif outUnit == 'km':
        res = size * MMinKM
    elif outUnit == 'ft':
        res = size * MMinFt
    elif outUnit == 'yd':
        res = size * MMinYd
elif inUnit == 'cm':
    if outUnit == 'm':
        res = size / meterInCM
    elif outUnit == 'cm':
        res = size
    elif outUnit == 'mi':
        res = size * CMinMi
    elif outUnit == 'in':
        res = size * CMinInc
    elif outUnit == 'km':
        res = size * CMinKm
    elif outUnit == 'ft':
        res = size * CMinFt
    elif outUnit == 'yd':
        res = size * CMinYd
elif inUnit == 'mi':
    if outUnit == 'm':
        res = size * meterInMi
    elif outUnit == 'cm':
        res = size / CMinMi
    elif outUnit == 'mi':
        res = size
    elif outUnit == 'in':
        res = size * MiInInc
    elif outUnit == 'km':
        res = size / MiInKm
    elif outUnit == 'ft':
        res = size / MiInFt
    elif outUnit == 'yd':
        res = size / MiInYd
elif inUnit == 'in':
    if outUnit == 'm':
        res = size * meterInInc
    elif outUnit == 'cm':
        res = size * CMinInc
    elif outUnit == 'mi':
        res = size * MiInInc
    elif outUnit == 'in':
        res = size
    elif outUnit == 'km':
        res = size / IncInKm
    elif outUnit == 'ft':
        res = size / IncInFt
    elif outUnit == 'yd':
        res = size / IncInYd
elif inUnit == 'km':
    if outUnit == 'm':
        res = size * meterInKm
    elif outUnit == 'cm':
        res = size * CMinKm
    elif outUnit == 'mi':
        res = size * MiInKm
    elif outUnit == 'in':
        res = size * IncInKm
    elif outUnit == 'km':
        res = size
    elif outUnit == 'ft':
        res = size * KMInFt
    elif outUnit == 'yd':
        res = size / KMInYd
elif inUnit == 'ft':
    if outUnit == 'm':
        res = size * meterInFt
    elif outUnit == 'cm':
        res = size * CMinFt
    elif outUnit == 'mi':
        res = size * MiInFt
    elif outUnit == 'in':
        res = size * IncInFt
    elif outUnit == 'km':
        res = size * KMInFt
    elif outUnit == 'ft':
        res = size
    elif outUnit == 'yd':
        res = size / FtInYd
elif inUnit == 'yd':
    if outUnit == 'm':
        res = size * meterInYd
    elif outUnit == 'cm':
        res = size * CMinYd
    elif outUnit == 'mi':
        res = size * MiInYd
    elif outUnit == 'in':
        res = size * IncInYd
    elif outUnit == 'km':
        res = size / KMInYd
    elif outUnit == 'ft':
        res = size * FtInYd
    elif outUnit == 'yd':
        res = size
print(str(res) + ' ' + outUnit)