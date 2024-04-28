import json


class JsonFile:
    def __init__(self, filename):
        self.filename = filename


    def save(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)# dump:graba datos a un archivo json
      
      
    def read(self):
        try:
            with open(self.filename,'r') as file:
                data = json.load(file)# load:carga datos desde un archivo json
        except FileNotFoundError:
            data = []
        return data
     
     
    def find(self,atributo,buscado):
        try:
            with open(self.filename,'r') as file:
                datas = json.load(file)
                data = [item for item in datas if item[atributo] == buscado ]
        except FileNotFoundError:
            data = []
        return data
    
    
    def update(self, attribute, value, new_values):
        data = self.read()
        for item in data:
            if item.get(attribute) == value:
                for key, new_value in new_values.items():
                    item[key] = new_value
                break
        self.save(data)

