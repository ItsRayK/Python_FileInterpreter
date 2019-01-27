from FileInterpreter import FileInt

if __name__ == '__main__':
    print("########## TEST_FILE_INTERPRETER ##########")
    print("##########    Key Value Test     ##########")
    myFile = FileInt("testfile.txt")
    print("Created FileInterpreter with:")
    print(myFile.dict)
    print(myFile.getString('testString'))
    myFile.load_dict("=")
    print("Loaded files key and value pairs:")
    print(myFile.dict)
    print(myFile.getString('testString'))
    print(myFile.getBoolean('testTrue'))
    print(myFile.getBoolean('testFalse'))
    print(myFile.getBoolean('testOther'))
    print(myFile.getInteger('testInteger'))
    print(myFile.getFloat('testFloat'))

    print("##########      List Test        ##########")
    myListFile = FileInt("testlist.txt")
    print("Created FileInterpreter with:")
    print(myListFile.list)
    myListFile.load_list()
    print(myListFile.list)