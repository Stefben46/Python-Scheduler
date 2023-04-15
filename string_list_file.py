import os
class StringListFile:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.isfile(filename):
            with open(filename, 'w') as f:
                pass

    def create(self, data):
        with open(self.filename, 'w') as f:
            for item in data:
                f.write(','.join(item) + '\n')

    def read(self):
        with open(self.filename, 'r') as f:
            data = [line.strip().split(',') for line in f]
        return data

    def add(self, item):
        with open(self.filename, 'a') as f:
            f.write(','.join(item) + '\n')

    def delete(self, first_string):
        data = self.read()
        new_data = [item for item in data if item[0] != first_string]
        if len(new_data) < len(data):
            with open(self.filename, 'w') as f:
                for item in new_data:
                    f.write(','.join(item) + '\n')
            return True
        else:
            return False
        
    def update(self, key, value):
        data = self.read()
        
        with open(self.filename, 'w') as f:
            for item in data:
                if item[0] == key:
                    item[2] = value
                f.write(','.join(item) + '\n')