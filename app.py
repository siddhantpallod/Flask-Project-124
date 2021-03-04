from flask import Flask, jsonify, request

app = Flask(__name__)

List = [
    {
        'id': 1,
        'name': 'Raju',
        'contact': '8493583924',
        'done': False
    },

    {
        'id': 2,
        'name': 'Rahul',
        'contact': '9087238097',
        'done': False
    }
]

@app.route('/')
def hellWorld():
    return 'Hello World!!'

@app.route('/add-data', methods = ['POST'])
def addTask():
    if not request.json:
        return jsonify({
            'status': 'error',
            'message': 'Please Provide Data'
        })
    
    contact = {
        'id': List[-1]['id'] + 1,
        'name': request.json['name'],
        'contact': request.json.get('contact', ""),
        'done': False
    }

    List.append(contact)

    return jsonify({
        'status': 'success',
        'message': 'Contact Added Successfully'
    })

@app.route('/get-data')
def getTask():
    return jsonify({
        'data': List    
    })

if(__name__ == '__main__'):
    app.run(debug = True)
