import argparse

class readArgs:
  def __init__(self):
    self.parser = ""

  def createArgumentParser(self):
    self.parser = argparse.ArgumentParser(description='Parse input files')
    self.parser.add_argument('-k', required=True, metavar='PATH_TO_KISSPLICE_FILE',
                             help='input kissplice .fa file')
    self.parser.add_argument('-b', required=True, metavar='PATH_TO_BLAT_FILE',
                             help='input blat .psl file')
    self.parser.add_argument('-o', required=False, metavar='PATH_TO_CORRECTED_BLAT_FILE',
                             help='output corrected blat .psl file. By default, create a file with the name of the input blat file with _corrected.')

  def getKisspliceFilePath(self, commandLine=None):
    if commandLine is not None:
      arguments = self.parser.parse_args(commandLine)
    else:
      arguments = self.parser.parse_args()

    return arguments.k

  def getBlatFilePath(self, commandLine=None):
    if commandLine is not None:
      arguments = self.parser.parse_args(commandLine)
    else:
      arguments = self.parser.parse_args()

    return arguments.b

  def getOutputFilePath(self, commandLine=None):
    if commandLine is not None:
      arguments = self.parser.parse_args(commandLine)
    else:
      arguments = self.parser.parse_args()

    if arguments.o is not None:
      return arguments.o
    else:
      fileName = str(os.getcwd()) + "_mainOutput" + str(time.time()) + ".psl"
      return fileName
