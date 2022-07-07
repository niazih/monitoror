

class AirtableToJsonConfig:

    # clé pour chercher les columns de l'airtable
    #airtable_column_groupe_key = "group_name"
    #airtable_column_type_key = "monitor_type"
    #airtable_column_label_key = "device_label"
    #airtable_column_hostname_key = "hostname"

    def __init__(self, airtable_data, group, type_key, label, hostname, col):
        self.airtable_data = airtable_data
        #self.local_data = local_data
        self.airtable_column_groupe_key = group
        self.airtable_column_type_key = type_key
        self.airtable_column_label_key = label
        self.airtable_column_hostname_key = hostname
        self.local_data_variable = { "version": "2.0", "columns": col, "tiles": [ ] }


    def __str__ (self):
        return self.local_data_variable


    # Fonction pour checker si le clé s"existe dans une list
    def key_existe(self, key, data_list):
        # on utilise cette fonction pour checker le nom de group existe dans le fichier json
        if key in data_list:
            return True
        return False


    # Trouvre le position (index) d'un clé dans une liste
    def find_value_position_json(self, key, value, data):
        # On utilise cette fonction pour trouver le position de group et les ligne des group (row)
        result = -1
        
        for i in range(0, len(data)) :
            if value == data[i][key] :
                result = i
        return result



    def airtable_to_json_dict(self):

        #loop trough all airtable data
        for i in range(0, len(self.airtable_data)):

            row = self.airtable_data[i]['fields']

            # variable pour stocker les données d'un ligne de airtable  
            monitoror_type = row[self.airtable_column_type_key]
            monitoror_type_label = row[self.airtable_column_label_key]
            monitoror_type_hostname = row[self.airtable_column_hostname_key]


            # template for type data like PING, PORT ...
            # this is just for PING type if we have aother types also, we have to put the if conditions or switch method  
            type_data_template = { "type": monitoror_type, "label": monitoror_type_label, "params": { "hostname": monitoror_type_hostname }, "configVariant": "default" }
                

            #airtable_data_group_name = self.airtable_data[i]['fields']
            # check if group existe and get group index to insert new data
            if self.key_existe(self.airtable_column_groupe_key, row):

                airtable_group_name = row[self.airtable_column_groupe_key]
                group_data_template = { "type": "GROUP", "label": airtable_group_name, "tiles": [ ] }

                # check if airtable_group_name existe in local data
                index = self.find_value_position_json('label', airtable_group_name, self.local_data_variable['tiles'])


                if (index != -1 ):
                    self.local_data_variable['tiles'][index]['tiles'].append(type_data_template)
                else:
                    self.local_data_variable['tiles'].append(group_data_template)
                    self.local_data_variable['tiles'][index]['tiles'].append(type_data_template)
                
            else:
                # if airtable group_name columns is empty so we are in this area
                self.local_data_variable['tiles'].append(type_data_template)
        
        return self.local_data_variable


