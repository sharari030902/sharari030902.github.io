#With the help of the youtube video and my uncle I wrote this program which asks
#the user if they want to encrypt or decrypt and returns an appropriate response

def ScrambleEncrypt(plainText):

    evenChars = ''
    oddChars = ''

    charCount = 0
    for ch in plainText:
        if(charCount %2 == 0):
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch 

        charCount = charCount + 1

    cipherText = evenChars + oddChars

    return cipherText


def decryptMessage(cipherText):
    
    halfLength = len(cipherText) // 2
    evenChars = cipherText[:halfLength]
    oddChars = cipherText[halfLength:]

    plainText = ''

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars) > len(oddChars):
        plainText = plainText + evenChars[-1]
        
        
    return plainText


print('Would you like to encrypt (e) or decrypt (d) text:')
encryptDecryptQuestion = input().lower()
if encryptDecryptQuestion == 'e':
    print('Please enter the text you would like to Encrypt:')
    plainText = input()
    encryptedText = ScrambleEncrypt(plainText)
    print(encryptedText) 
elif encryptDecryptQuestion == 'd':
    print('Please enter the text you would like to Decrypt:')
    encryptedText = input()
    msg = decryptMessage(encryptedText)
    print(msg)
else:
    print('The input you entered was not valid')



