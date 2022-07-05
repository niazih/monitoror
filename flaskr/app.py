from flask import Flask, render_template, request

import python_scripts.main  as sync_btn


app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        message = "Data hase sync successfuly !"
        #recreate_each_time.main()
        sync_btn.main()
        
        return render_template('index.html', message=message)
    if request.method == "GET":
        return render_template('index.html')


