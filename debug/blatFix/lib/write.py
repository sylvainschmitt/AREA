from errno import EACCES, EPERM

class writeFile:
  def __init__(self):
      pass

  def blatLinesToString(self, blatTable):
    newTable = []
    for element in blatTable:
      elementString = ""
      for i in range(0, len(element) - 1):
        elementString += str(element[i]) + "\t"
      elementString += str(element[len(element) - 1])
      newTable.append(elementString)
    return newTable

  def blatTableToString(self, blatTable):
    elementString = ""
    for element in blatTable:
      elementString += str(element + ",\n")
    return elementString

  def openBlatFile(self, filePath):
    try:
      blatFile = open(filePath, 'a')
      return blatFile
    except (IOError, OSError) as e:
      if e.errno==EACCES or e.errno==EPERM:
        raise OSError("Wrong argument : " + filePath + ". Permission denied.")
      raise IOError("Wrong argument : " + filePath + ". May not be a file.")

  def writeBlatFile(self, filePath, blatTable):
    blatFile = self.openBlatFile(filePath)
    header = open("./lib/header.psl", 'r')
    header = header.readlines()
    headerString = ""
    for element in header:
      headerString += str(element)
    headerString += "\n"
    blatFile.write(str(headerString))
    blatTable = self.blatLinesToString(blatTable)
    blatString = self.blatTableToString(blatTable)
    blatFile.write(blatString)
    blatFile.close()
