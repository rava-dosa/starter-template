from flask import Flask, request, send_from_directory, render_template
import json
from os import listdir
import os
# set the project root directory as the static folder, you can set others.
# app = Flask(__name__, static_url_path='/home/user/nlproject/web')
template_dir = os.path.abspath('../frontend/dist')
print(template_dir)
app = Flask(__name__, static_url_path='/home/user/miti-dashboard/frontend/dist',template_folder=template_dir)
@app.route('/')
def root():
    print("aayame")
    name="apoorva"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
