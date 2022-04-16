import os

class NameChanger():

    def __init__(self, access_path, new_name):
        self.access_path = access_path
        self.new_name = new_name
        self.list_file = os.listdir(self.access_path)
        
    def rename(self):
        number = 1
        for file in self.list_file:
            if file[:1] == '.':
                continue
            full_src = os.path.join(self.access_path, file)
            if os.path.isfile(full_src):
                dst = file.replace(file, f'{self.new_name}{number}')
                print(dst)
                if file != dst:
                    full_dst = os.path.join(self.access_path, dst)
                    os.rename(full_src, full_dst)
            number += 1