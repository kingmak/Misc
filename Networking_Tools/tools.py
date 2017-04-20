###################################################################################
## TODO:
##  - update current list in the comment below
##  - fix tests section, print test name too
###################################################################################

###################################################################################
## A set of tools for computer networking & computer architecture
##
## Current List:
##
##
## Author: KingMak
###################################################################################

__Author__ = 'KingMak'
__Version__ = '0.1'

###################################################################################
## Integer to Binary & Binary to Integer
###################################################################################

def binToInt(binary):
    return int(binary, 2) # binary has to be string, so no conv to str

def intToBin(integer):
    if isinstance(integer, int):
        return bin(integer)
    return bin(int(integer))

###################################################################################
## Integer to Hex & Hex to Integer
###################################################################################

def intToHex(integer):
    if isinstance(integer, int):
        return hex(integer)
    return hex(int(integer))

def hexToInt(hexstr):
    return int(hexstr, 16)

###################################################################################
## String to Hex & Hex to String
###################################################################################

def strToHex(string):
    return ('0x' + ''.join([hex(ord(char))[2:] for char in string])) # adding 0x to so i know its hex

def hexToStr(hexstr):
    if len(hexstr) % 2 != 0:
        raise 'string must be of even length'

    if '0x' in hexstr:
        hexstr = hexstr[2:]

    string = ''
    index = 0

    while index < len(hexstr):
        string += (chr(hexToInt(hexstr[index] + hexstr[index + 1])))
        index += 2

    return string

###################################################################################
## IP address to Binary form & Binary form to Ip address
###################################################################################

def ipToBin(ip, pad = 8):
    fixed = []
    octets = ip.split('.')

    for octet in octets:
        binary = intToBin(octet)[2:]

        if len(binary) != pad:
            fixed.append(('0' * (pad - (len(binary)))) + binary)
        else:
            fixed.append(binary)

    return ' '.join([octet for octet in fixed])

def binToIp(binaryIp):
    fixed = []
    octets = binaryIp.split(' ')

    for octet in octets:
        fixed.append(int(octet, 2))

    return '.'.join([str(octet) for octet in fixed])

###################################################################################
## Tests
###################################################################################

print strToHex('abcdef')
print hexToStr(strToHex('abcdef'))
print intToBin(1)
print intToBin('1')
print binToInt('1')
print binToInt('0b1')

print '\n\n\n'
print ipToBin('1.1.1.1')
print binToIp(ipToBin('1.1.1.1'))
print intToHex(97)
print intToHex('97')
print hexToInt('0x61')
