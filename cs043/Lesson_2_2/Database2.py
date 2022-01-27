class Simpledb():
    def __init__(self, filename):
        self.filename = filename

    def __repr__(self):
        return "<" + self.__class__.__name__ + " file = " + "recipes.txt" + ">"

    def insert(self, key, value):
        f = open(self.filename,'a')
        f.write(key + '\t' + value + '\n')
        f.close()

    def select_one(self, key):
        f = open(self.filename, 'r')
        data = f.readlines()
        for row in data:
            (k, v) = row.split('\t', 1)
            if k == key:
                print("Number:",v[:-1])
                return v[:-1]
        for i in data:
            if i != key:
                print("NO name in list!")
                return "NOT FOUND"
        f.close()

    '''
    def delete(self, key):
        f = open(self.filename, 'r')
        result = open('results.txt', 'w')
        data = f.readlines()
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k != key:
                result.write(row)
        f.close()
        result.close()
        import os
        f = open(self.filename, 'w')
        os.replace('results.txt', self.filename)
        if key not in data:
            print("Name not Found")
    '''
    def delete(self, key):
        does_exist= False
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for row in f:
            row= row[:-1]
            (k, v) = row.split('\t',1)
        if k != key:
            result.write(row + '\n')
        else:       
            does_exist= True
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)
        return does_exist

    def update(self, key, value):
        f = open(self.filename, 'r')
        result = open('result.txt', 'w')
        for (row) in f:
            (k, v) = row.split('\t', 1)
            if k == key:
                result.write(key + '\t' + value + '\n')
                
            else:
                result.write(row)
        f.close()
        result.close()
        import os
        os.replace('result.txt', self.filename)
