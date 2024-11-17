import json
import subprocess
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        name = request.form['name']
        age = request.form['age']

        
        result = subprocess.run(['scrapy', 'crawl', 'infospider', '-O', 'output.json'], capture_output=True, text=True)

        
        if result.returncode == 0:
        
            if os.path.exists('output.json') and os.path.getsize('output.json') > 0:
                
                with open('output.json', 'r') as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []
                        print("Error decoding JSON.")
            else:
                data = []
                print("Error: output.json is empty or does not exist.")
        else:
            data = []
            print("Scrapy command failed. Please check the spider.")

        return render_template('index.html', data=data)

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)
