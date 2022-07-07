from flask import Flask, render_template, request

import python_scripts.main  as sync_btn


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":

        message = "Data hase sync successfuly !"
        
        screen_to_sync = request.form['selected_screen']
        sync_btn.main(screen_to_sync)

        return render_template('index.html', message=message)
    if request.method == "GET":
        return render_template('index.html')



# ImmutableMultiDict([('select_screen', 'default.json'), ('syncBtn', '')]) 