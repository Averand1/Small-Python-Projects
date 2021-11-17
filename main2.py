import time, random, sys

TIME = 0.085
Rows = [
  #123456789
  '         ##',
  '        #{}-{}#',
  '       #{}---{}#',
  '      #{}-----{}#',
  '     #{}------{}#',
  '    #{}-------{}#',
  '    #{}------{}#',
  '     #{}----{}#',
  '      #{}---{}#',
  '       #{}-{}#',
  '         ##',
  '        #{}-{}#',
  '       #{}---{}#',
  '      #{}-----{}#',
  '     #{}-------{}#',
  '    #{}-------{}#',
  '    #{}------{}#',
  '     #{}----{}#',
  '      #{}---{}#',
  '       #{}-{}#',
  #123456789
] 
try:
  print("DNA Sequence")
  print("Press ctrl C to exit")
  time.sleep(2)
  rowIndex = 0

  while True:
    #increment to draw the next row
    rowIndex = rowIndex + 1
    if rowIndex == len(Rows):
        rowIndex = 0

    #Row index 0 and 10 doesnt have --
    if rowIndex == 0 or rowIndex == 10:
      print(Rows[rowIndex])
      continue

    #ATGC randomized
    randomSelection = random.randint(1,4)
    if randomSelection == 1:
      leftNucleotide, rightNucleotide = "A", "T"
    elif randomSelection == 2:
      leftNucleotide, rightNucleotide = 'G', "C"
    elif randomSelection ==3:
      leftNucleotide, rightNucleotide = "T", "A"
    elif randomSelection == 4:
      leftNucleotide, rightNucleotide = "C", "G"
    
    print(Rows[rowIndex].format(leftNucleotide,rightNucleotide))
    time.sleep(TIME)
except KeyboardInterrupt:
  sys.exit()