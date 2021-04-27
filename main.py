import struct
import math 

getBin = lambda x: x > 0 and str(bin(x))[2:] or "-" + str(bin(x))[3:]

def floatToBinary64(value):
    val = struct.unpack('Q', struct.pack('d', value))[0]
    return getBin(val)

def binaryToFloat(value):
    hx = hex(int(value, 2))   
    return struct.unpack("d", struct.pack("q", int(hx, 16)))[0]

def fixBinStr(binstr):
    qntZero = 64 - len(binstr)

    newBinstr = ''

    for i in range(qntZero):
        newBinstr += '0'

    for i in binstr:
        newBinstr += i

    return newBinstr

def printValues(S, E, M):
    print('S: is the bit value of the signal = ', S)
    print('E: is the value, in decimal, of the exponent =', E)
    print('M: is the value, in decimal, of the sum of the bits of the mantissa = ', M)

def calculateValueE(E):
    eResult = 0
    j = 0

    for i in range(10, -1, -1):
        eResult += int(E[j]) * pow(2, i)
        j += 1

    print('Calculated E = ', eResult)
    return eResult

def calculateValueM(M):
    j = 0
    mResult = 0
    for i in range(51, -1, -1):
        mResult += int(M[j]) * pow(2, i)
        j += 1

    print('Calculated M = ', mResult)
    return mResult

def main():
    number = float(input('Enter any floating number you want to convert\n'))
    binstr = floatToBinary64(number)
    print('Binary equivalent:')
    print(binstr + '\n')

    binstr = fixBinStr(binstr)

    S = int(binstr[0])
    E = binstr[1:12]
    M = binstr[12:]

    printValues(S, E, M)
    eResult = calculateValueE(E)
    mResult = calculateValueM(M)

    y = mResult / pow(2, 52)

    print('Y is:', y)

    e = eResult - 1023

    finalResult = 0

    if(e % 2 == 0):
        finalResult = pow(2, (e/2)) * math.sqrt((1 + y))
    else:
        finalResult = pow(2, ((e+1)/2)) * (math.sqrt((1+y)) / 1.41421356237309504880168872420969807856967187537694807317667973799)

    print(number, 'in the IEEE754 standard is:', finalResult)


if __name__ == "__main__":
    main()
