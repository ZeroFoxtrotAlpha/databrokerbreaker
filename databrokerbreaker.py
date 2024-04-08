def encode():
    word = input("Enter a word (canopied or picayune): ")
    letter = input("Enter a lowercase Unicode letter: ")
    binary = format(ord(letter), '08b')
    result = ""
    for i in range(len(binary)):
        if binary[i] == '0':
            result += word[i]
        else:
            index = "acdeinopuxy".index(word[i])
            result += "асԁеіոорսху"[index]
    print(result)

def decode():
    word = input("Enter a word: ")
    binary = ""
    for letter in word:
        unicode_binary = format(ord(letter), '08b')
        if len(unicode_binary) == 8:
            binary += '0'
        else:
            binary += '1'
    result = chr(int(binary, 2))
    print(result)

choice = input("Choose a function (encode or decode): ")
if choice == "encode":
    encode()
elif choice == "decode":
    decode()
else:
    print("Invalid choice!")