import json


class SaveToConfig:

    def __init__(self, filename, data):
        self.filename = filename
        self.data = data

    def __str__ (self):
        return f"ces données sont enregistrées dans le fichier de configuration: ==> {self.data}"


    def Save_data_to_json(self) :
        
        with open(self.filename, 'w') as myfile:
            json.dump(self.data, myfile)

        myfile.close()
        #print("Data has save successfuly !")






