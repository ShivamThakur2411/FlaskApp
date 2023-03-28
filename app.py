from flask import Flask, jsonify, request

app = Flask(__name__)


contacts=[
    {
        "id":1,
        "contact":9987644456,
        "name":u"Raju",
        "done":False
    },
    {
        "id":2,
        "contact":9876543222,
        "name":u"Rahul",
        "done":False
    }
]

@app.route("/get-list")

def see_contacts():
    return jsonify({
        "list":contacts
    })

@app.route("/add-list", methods=["POST"])

def add_contacts():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        })

    contact={
        'id':contacts[-1]['id']+1,
        'contact':request.json['contact'],
        'name':request.json.get('description',""),
        'done':False
    }
    contacts.append(contact)
    return jsonify({
        "status":"success",
        "message":"message added successfully"
    })

if (__name__=='__main__'):
    app.run(debug=True)