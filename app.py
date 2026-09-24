from flask import Flask
app = Flask(__name__)
import random
@app.route("/")
def hello():
   return("The code got edited :/")
