import re


class kissplice():
  def __init__(self):
    self.Table = []
    self.Dictionary = {}

  def initializeTable(self, fileContent):
    self.Table = fileContent.readlines()

  def isFilled(self):
    if len(self.Table) > 0:
      return True
    else:
      return False

  def formatTable(self):
    self.Table = [element.strip('>').split('\n') for element in self.Table]

    temporaryTable = []
    rowNumber = -1
    for element in self.Table:
      if re.match("^bcc.*$", element[0]):
        rowNumber += 1
        temporaryTable.append(element)
      else:
        temporaryTable[rowNumber][1] = temporaryTable[rowNumber][1] + element[0]
    self.Table = temporaryTable

  def createDictionary(self):
    for element in self.Table:
      snpIdTable = element[0].split("|")
      snpKey = snpIdTable[0] + "|" + snpIdTable[1] + "|" + snpIdTable[2] + "|" + snpIdTable[3]
      self.Dictionary[snpKey] = element[0]