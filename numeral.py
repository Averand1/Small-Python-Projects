print('Numeric Counter')
while True:
  result = input('Enter the starting number: ')
  if result == '':
    result = '0'
    break
  if result.isdecimal():
    break
  print('Please Enter a greater number than or equal to 0')
start = int(result)

while True:
  result = input('Enter how many numbers to display: ')
  if result == '':
    result = '1000'
    break
  if result.isdecimal():
    break
  print('Please enter a number')
amount = int(result)

for number in range(start, start+amount):
  hexNumber = hex(number)[2:].upper()
  binNumber = bin(number)[2:]

  print('DEC:', number, '   HEX:', hexNumber, '   BIN:', binNumber)