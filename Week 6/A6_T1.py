def readFile(FileName:str) -> str:
    Filehandler = open("Week 6/" + FileName, 'r', encoding='UTF-8')
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        Content += Row
        Row = Filehandler.readline()
    return Content

def main():
    print("Program starting.")
    print("This program can read a file.")
    FileName = input("Insert file name: ")
    FileContent = readFile(FileName)
    print(f"#### START {FileName} ####")
    print(FileContent)
    print(f"#### END {FileName} ####")
    print("Program ending.")
    return None
main()