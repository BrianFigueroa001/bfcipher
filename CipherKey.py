#cipherkey.py
# Example 2: class methods to store and retrieve properties
#Cipher Algorithm
# Encryption
# 1. Swap places of left-most index and right-most index.
# 2. Move both indices inward and swap their places.
# 3. Repeat until 'middle' index is reached.
# 4. Add +12 to each character.

class SymmetricKey():
    def encrypt(self, message):
        encryptedMessage = ""
        listMessage = []
        listMessage[:0] = message
        leftIndex = 0
        rightIndex = len(listMessage) - 1

        while leftIndex < rightIndex:
            temp = listMessage[leftIndex]
            listMessage[leftIndex] = listMessage[rightIndex]
            listMessage[rightIndex] = temp

            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1

        for i in range(len(listMessage)):
            charToInt = ord(listMessage[i])
            charToInt = charToInt + 12
            intToChar = chr(charToInt)
            listMessage[i] = intToChar

        encryptedMessage = encryptedMessage.join(listMessage)
        return encryptedMessage
        
    def decrypt(self, message):
        decryptedMessage = ""
        listMessage = []
        listMessage[:0] = message
        firstIndex = 0
        lastIndex = len(listMessage) - 1
        listMessageLen = len(listMessage)

        middleIndex = firstIndex + (lastIndex - firstIndex)//2
        leftIndex = middleIndex
        rightIndex = middleIndex + 1

        for i in range(len(listMessage)):
            charToInt = ord(listMessage[i])
            charToInt = charToInt - 12
            intToChar = chr(charToInt)
            listMessage[i] = intToChar

        if listMessageLen % 2 != 0:
             leftIndex = middleIndex - 1 

        while leftIndex >= 0 and rightIndex <= lastIndex:
            temp = listMessage[leftIndex]
            listMessage[leftIndex] = listMessage[rightIndex]
            listMessage[rightIndex] = temp

            leftIndex = leftIndex - 1
            rightIndex = rightIndex + 1

        decryptedMessage = decryptedMessage.join(listMessage)

        return decryptedMessage
