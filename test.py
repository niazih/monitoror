import os

screen_dict = {
    'default': {
        'screen_name': 'default.json',
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



user_screen = "screen2"




def screen_params(screen_name, screen_dict):
    
    if screen_name in screen_dict :
        return screen_dict[screen_name]
    else:
        return False

s =  screen_params(user_screen, screen_dict)

print(s['screen_name'])

print(screen_dict['screen1']['screen_name'])


base_dir = os.path.abspath('')
monitoror_dir = base_dir + '/monitoror/'

print(monitoror_dir)