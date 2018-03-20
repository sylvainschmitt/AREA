import re


class blat:
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

  def stripHeader(self):
    while re.match("^[0-9]+.*$", self.Table[0]) is None:
      self.Table.remove(self.Table[0])

  def formatTable(self):
    self.Table = [element.strip('\n').strip(',').split('\t') for element in self.Table]

  def createDictionary(self):
    for element in self.Table:
      snpDictionaryValue = []
      for i in range(0, len(element)):
        if i == 13: # Gene
          compIdTable = element[i].split("_")
          trunkedCompId = "_".join(compIdTable[0:-1])
          snpDictionaryValue.append(trunkedCompId)
          snpDictionaryValue.append(compIdTable[-1])
        else:
          if i == 9: # SNP to be changed
            snpIdTable = element[i].split("|")
            snpKey = snpIdTable[0] + "|" + snpIdTable[1] + "|" + snpIdTable[2] + "|" + snpIdTable[3]
          snpDictionaryValue.append(element[i])
          
      if snpKey in self.Dictionary:
        self.Dictionary[snpKey].append(snpDictionaryValue)
      else:
        self.Dictionary[snpKey] = [snpDictionaryValue]