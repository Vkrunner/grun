from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import os 

app = Flask(__name__)

history = []

@app.route('/compute', methods=['POST'])
def compute_sums():
    data = request.get_json()
    spreadsheet = data.get('spreadsheet', [])
    row_sums = [sum(row) for row in spreadsheet]
    response = ({'row_sums': row_sums})

    history.append({
        'time':datetime.now().strftime('%Y-%M-%D %H:%M:%S'),
        'request': json.dumps(data, indent=4),
        'response': json.dumps(response, indent=4)
    })


    return jsonify(response)


@app.route('/')
def show_history():
    return render_template('history.html', history=history)




# if __name__ == '__main__':
#     app.run('0.0.0.0', debug=True, port=5000)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))