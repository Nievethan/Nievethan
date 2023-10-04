print('Welcome to Cryptographic Techniques Program') # Header
print('____________________________________________')
print('')

def encryption_caesar(msg, shift): # Defining encryption function
    result = ''                                                                 
    for i in range(len(msg)):
        char = msg[i]                                                                                                                          
        result += chr((ord(char) + shift))

    return result

def decryption_caesar(msg, shift): # Defining decryption function
    result = ''                                                                      
    for i in range(len(msg)):
        char = msg[i]                                                                                                                        
        result += chr((ord(char) - shift))

    return result

while True:
    print('Please select an option: ' )
    print('**************************')
    print('1. Encrypt')
    print('2. Decrypt')
    select = int(input('Selection: ')) # Awaits user input as an integer
    print('')

    if select == 1: # If statements to make sure user chooses only the available options
        msg = input('Please enter a message: ')                                         
        shift = 3
        crypt = encryption_caesar(msg, shift)
        print('')
        print('Original: ' + msg)
        print('Encrypted: ' + crypt)
        break
    elif select == 2:
        msg = input('Please enter a message: ')                                         
        shift = 3
        crypt = decryption_caesar(msg, shift)
        print('')
        print('Original: ' + msg)
        print('Decrypted: ' + crypt)
        break
    else:
        print('Option not valid.')
        
