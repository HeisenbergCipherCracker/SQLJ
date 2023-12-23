import csv
import os
import random
import string

class Export(object):
    def __init__(self,datas):
        self.directory = "SQLJcap"
        self.datas = datas

    def _mk_dir(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def export(self, filename):
        self._mk_dir()
        with open(os.path.join(self.directory, filename), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(self.datas)

# obj = Export(datas="ali")
# obj.export("myfile.csv")
            
def exporter(data:str):
    obj = Export(datas=data)
    obj.export(f"{random.choice(string.ascii_letters)+random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)}.csv")

exporter("hello")