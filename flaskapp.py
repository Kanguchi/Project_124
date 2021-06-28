from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "Contact":"9191032849",
        "Name":"Cari",
        "done": False,
        "id": 1
    },
    {
        "Contact":"3475921390",
        "Name":"Thomas",
        "done": False,
        "id": 2
    }
]

@app.route('/add-data', methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "plz provide data"
        }, 400)
    contact = {
        'id': contacts[-1]['id']+1,
        'Name': request.json['Name'],
        'Contact': request.json.get('Contact', ""),
        'done': False
    }
    contacts.append(contact)
    return jsonify({
        "status": "Success",
        "message": "Contact Successfully Added!"
    })

@app.route('/get-data', methods=['GET'])
def get_task():
    return jsonify({
        'data': contacts
    })

if (__name__ == "__main__"):
    app.run(debug=True)