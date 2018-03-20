import re

class correct:
  def __init__(self):
    pass

  def correctBlat(self, kisspliceDictionary, blatTable):
    correctedBlatTable = []

    for element in blatTable:
      snpIdTable = element[9].split("|")
      snpKey = snpIdTable[0] + "|" + snpIdTable[1] + "|" + snpIdTable[2] + "|" + snpIdTable[3]
      element[9] = kisspliceDictionary[snpKey]
      correctedBlatTable.append(element)

    return correctedBlatTable    
