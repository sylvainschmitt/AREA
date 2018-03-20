# Imports

from lib.arguments import readArgs
from lib.read import readFile
from lib.kissplice import kissplice
from lib.blat import blat
from lib.correct import correct
from lib.write import writeFile

# Methods

readArgs = readArgs()
read = readFile()
kiss = kissplice()
blat = blat()
correct = correct()
write = writeFile()

# Arguments

readArgs.createArgumentParser()
kissPath = readArgs.getKisspliceFilePath()
blatPath = readArgs.getBlatFilePath()
outputPath = readArgs.getOutputFilePath()

# Kissplice opening

print("# Openning Kissplice fa file #")

if read.isKissplice(kissPath) is not True:
  print("An error occurred, Kissplice table is not in fa format.")
  exit()

kissFile = read.openFile(kissPath)
kiss.initializeTable(kissFile)
if kiss.isFilled() is not True:
  print("An error occurred, Kissplice table seems to be empty.")
  exit()

kiss.formatTable()
kiss.createDictionary()

# Blat opening

print("# Openning Blat psl file #")

if read.isBlat(blatPath) is not True:
  print("An error occurred, Blat table is not in psl format.")
  exit()

blatFile = read.openFile(blatPath)
blat.initializeTable(blatFile)
if blat.isFilled() is not True:
  print("An error occurred, Blat table seems to be empty.")
  exit()

blat.stripHeader()
blat.formatTable()
blat.createDictionary() 

# Blat correction

print("# Correcting Blat psl file #")

correctedBlat = correct.correctBlat(kiss.Dictionary, blat.Table)

# Blat writting

print("# Writting corrected Blat psl file #")

write.openBlatFile(outputPath)
correctedBlat = write.writeBlatFile(outputPath, correctedBlat)

print("# DONE ! #")
