from pyairtable import Api, Base, Table
from python_scripts.convert_airtable_json import AirtableToJsonConfig
from python_scripts.save_data_to_config import SaveToConfig
from python_scripts.parametre import *



#filename = os.path.abspath('config.json')
filename = "../monitoror/config.json"

# all parametre nécessaire pour initialiser la airtable
airtable_column_groupe_key = "group_name"
airtable_column_type_key = "monitor_type"
airtable_column_label_key = "device_label"
airtable_column_hostname_key = "hostname"

# nombre de colonne pour affichage
monitoror_columns_number = 8



def main():
    
    # Recuperer les données à partir de airtable
    airtable = Table('keysoMHiR5OdPaLtk', 'appGMo05NrFZVKB15', 'supervision')
    airtable_data = airtable.all(sort=['group_name'])

    # Changer les données importer depuis le airtable en format json
    # L'ordre de parametre de la classe AirtableToJsonConfig (airtable_data, group, type_key, label, hostname, col)
    convert_to_json = AirtableToJsonConfig(airtable_data, airtable_column_groupe_key, airtable_column_type_key, airtable_column_label_key, airtable_column_hostname_key, monitoror_columns_number)
    data_to_save = convert_to_json.airtable_to_json_dict()


    # Sauvegarder les données dans le fichier json
    Save_to_json = SaveToConfig(filename, data_to_save)
    Save_to_json.Save_data_to_json()










