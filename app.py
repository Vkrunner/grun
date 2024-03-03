from flask import Flask, request, jsonify, render_template
from datetime import datetime
import json
import os 

app = Flask(__name__)

history = []

@app.route('/compute', methods=['POST'])

def compute_sums():
    data            = request.get_json()
    spreadsheet     = data.get('spreadsheet', [])
    row_sums        = [sum(row) for row in spreadsheet]
    response        = ({'row_sums': row_sums})
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    history.append({
        'time'      :  now,
        'request'   :  json.dumps(data, indent=4),
        'response'  :  json.dumps(response, indent=4)
    })

    return jsonify(response)


@app.route('/')
def show_history():
    return render_template('history.html', history=history)


if __name__ == "__main__":
    port = os.environ.get('PORT', 5000)
    app.run(debug=True, host="0.0.0.0", port=port)