from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from langchain_community import ChatModels
#raju gunde welcome to phython
app = Flask(__name__)

@app.route("/")
def home():
    return "Homepage"

@app.route("/home/<username>")
def home_page(username):
    return f"Welcome {username}"

@app.route("/age/<int:age_number>")
def age(age_number):
    return f"My age is {age_number}"


if __name__ == "__main__":
    app.run(debug=True)