try:
    import pyperclip
except ImportError:
    pass

symbols = 'abcdefghijklmnopqrstuvwxyz'
print('''Caesar Cipher
      The Caesar Cipher encrypts letters by shifting them over by a
      key number. For example, a key of 2 means the letter A is
      encrypted into C, the letter B encrypted into D, and so on.\n''')

while True:
    response = input('Do you want to (e)ncrypt or (d)ecrypt? >>> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print('Please enter the letter e or d.')

while True:
    maxKey = len(symbols) - 1
    response = input('Pleae enter the key (0 to {}) to use. >>> '.format(maxKey)).lower()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

message = input('Enter the message to {}. >>> '.format(mode))
message = message.lower
translated = ''
for symbol in message:
    if symbol in symbols:
        num = symbols.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)
        translated = translated + symbols[num]
    else:
        translated = translated + symbol
print(translated)
try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass