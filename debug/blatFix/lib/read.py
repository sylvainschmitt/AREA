import re


class readFile:
  def __init__(self):
    pass

  def openFile(self, filePath):
    try:
      file = open(filePath, 'r')
      return file
    except IOError:
      raise IOError("Wrong argument : " + filePath + ". File may not exist.")

  def isBlat(self, filePath):
    blatMatch = re.match("^.*\.psl$", filePath)
    if blatMatch is not None:
      return True
    else:
      return False

  def isKissplice(self, filePath):
    kisspliceMatch = re.match("^.*\.fa$", filePath)
    if kisspliceMatch is not None:
      return True
    else:
      return False
