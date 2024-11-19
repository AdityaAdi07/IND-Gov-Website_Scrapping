import json
import subprocess
import os
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        state = request.form['state']

 
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

        highlighted_data = []
        normal_data = []

        for item in data:
            description = item.get('DESCRIPTION', '').lower()

     
            if state.lower() in description:
                item['highlight_state'] = True

                if str(age) in description:
                    item['highlight_age'] = True 
                highlighted_data.append(item)
            else:
                normal_data.append(item)

 
        data = highlighted_data + normal_data

        return render_template('index.html', data=data)

    return render_template('index.html', data=None)



if __name__ == '__main__':
    app.run(debug=True)
