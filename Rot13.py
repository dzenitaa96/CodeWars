def rot13(message):
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char.isupper():
            result += chr((ord(char) + 13 - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + 13 - 97) % 26 + 97)
        else:
            result += char
    return result

message = 'Test'
print(rot13(message))