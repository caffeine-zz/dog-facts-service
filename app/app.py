from flask import Flask
import requests
import random
import json
app = Flask(__name__)

@app.route("/")
def hello():
    r = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all')
    list = json.loads(r.content)
    item = random.choice(list)
    fact = item['fact']
    return '{} {}'.format(str("Random dog fact:"), fact)

if __name__ == "__main__":
    app.run()
