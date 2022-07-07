#!/home/user/Final_Project/venv/bin/python3

from pyairtable import Api, Base, Table
from python_scripts.convert_airtable_json import AirtableToJsonConfig
from python_scripts.save_data_to_config import SaveToConfig



# all parametre nécessaire pour initialiser la airtable
airtable_column_groupe_key = "group_name"
airtable_column_type_key = "monitor_type"
airtable_column_label_key = "device_label"
airtable_column_hostname_key = "hostname"

# nombre de colonne pour affichage
monitoror_columns_number = 8


# Airtable API parametre
airtable_api_key = "keysoMHiR5OdPaLtk"
airtable_base_id = "appGMo05NrFZVKB15"


# Chemin où les fichier de configuration d'écran se trouve
screens_path = '../monitoror/'

# Dictionaire qui a tous les parametres nécessaire d'un SCREEN
screen_dict = {
    'default': {
        'screen_name': 'config.json',
        'airtable_table_name': 'supervision'
    },
    'screen1' :{
        'screen_name': 'screen1.json',
        'airtable_table_name': 'screen1'
    },
    'screen2' :{
        'screen_name': 'screen2.json',
        'airtable_table_name': 'screen2'
    },
    'screen3' :{
        'screen_name': 'screen3.json',
        'airtable_table_name': 'screen3'
    },
}



# Fonction qui renvoie les params d'un screen
def screen_params(screen_name, screen_dict):
    # On utilise cette fonction pour recuperer tous les parametres d'un screen
    if screen_name in screen_dict :
        return screen_dict[screen_name]
    else:
        return False



# On passe le nom de fichier à sync
def main(filename):

    # Recup les parametre d'un SCREEN
    params = screen_params(filename, screen_dict)
    
    # Recuperer les données à partir de airtable
    airtable = Table(airtable_api_key, airtable_base_id, params['airtable_table_name'])
    airtable_data = airtable.all(sort=[airtable_column_groupe_key])


    # Changer les données importer depuis le airtable en format json
    # L'ordre de parametre de la classe AirtableToJsonConfig (airtable_data, group, type_key, label, hostname, col)
    convert_to_json = AirtableToJsonConfig(airtable_data, airtable_column_groupe_key, airtable_column_type_key, airtable_column_label_key, airtable_column_hostname_key, monitoror_columns_number)
    data_to_save = convert_to_json.airtable_to_json_dict()

    # Sauvegarder les données dans le fichier json
    Save_to_json = SaveToConfig(screens_path + params['screen_name'], data_to_save)
    Save_to_json.Save_data_to_json()

