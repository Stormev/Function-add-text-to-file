def AddSym(path_copy, path_add):
    with open(path_copy, "r", encoding="utf-8") as file_read:
        text = file_read.read()
    with open(path_add, "r", encoding="utf-8") as file_check:
        text1 = file_check.read()[-1]
        print(text1)
    with open(path_add, "a", encoding="utf-8") as file_add:
        if text1 != ',':
            file_add.write(',' + text)
        else:
            file_add.write(text)
