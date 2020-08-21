#imports
import math
from flask import Flask, render_template 


app = Flask(__name__)




# linking to the webpages
@app.route('/')
def index():
    return render_template('index.html')






# Website running

if __name__ == '__main__':
    app.run(debug = True )
