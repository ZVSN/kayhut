import json
import os

class JsonFile:
    def getData(currFile):
        data = JsonFile.openFile(currFile,'r')
        if data != False:
            items = json.load(data)
            JsonFile.closeFile(data)
            return items
        return False

    def openFile(currOpenFile,currMode):
        try:
            f = open(currOpenFile,mode=currMode)
            return f
        except (FileNotFoundError, IOError):
            print("\nFile '"+currOpenFile+"' not found\n")
            return False

    def closeFile(currCloseFile):
        try:
            currCloseFile.close()
        except (FileNotFoundError, IOError):
            print("\nCannot close '"+currCloseFile+"' file\n")
            return False