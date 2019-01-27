class FileInt:
    def __init__(self, filepath):
        self.file = filepath
        self.dict = {}
        self.list = []

    def load_dict(self, split_character):
        try:
            with open(self.file) as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    elif line.startswith("#"):
                        continue
                    else:
                        stripped_line = line.strip()#(" \n")
                        key = stripped_line.split(split_character)[0].strip()
                        value = stripped_line.split(split_character)[1].strip()
                        self.dict[key]=value
        except FileNotFoundError:
            print("Failed to open file. '" + self.file + "not found.")

    def load_list(self):
        try:
            with open(self.file) as fp:
                for line in fp:
                    if not line.strip():
                        continue
                    elif line.startswith("#"):
                        continue
                    else:
                        stripped_line = line.rstrip()
                        item = stripped_line
                        print(item)
                        self.list.append(item)
        except FileNotFoundError:
            print("Failed to open file. '" + self.file + "not found.")

    def getString(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            print("Value '" + key + "' not found.")

    def getInteger(self, key):
        if key in self.dict:
            return int(self.dict[key])
        else:
            print("Value '" + key + "' not found.")

    def getBoolean(self, key):
        if key in self.dict:
            if self.dict[key] == "True":
                return True
            else:
                return False
        else:
            print("Value '" + key + "' not found.")

    def getFloat(self, key):
        if key in self.dict:
            return float(self.dict[key])
        else:
            print("Value '" + key + "' not found.")

