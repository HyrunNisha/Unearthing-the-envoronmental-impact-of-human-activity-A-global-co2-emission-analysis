import numpy as np
from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET'])
def index():
    return render_template('tableau.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)

