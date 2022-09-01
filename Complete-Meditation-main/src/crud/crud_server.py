from flask import Flask, jsonify, request
import crud
from db_and_table import create_table


# using JSON for data communication
app = Flask(__name__) # making a flask app


# GET(http method) and Read(CRUD)
@app.route('/files', methods=["GET"])
def get_files():
    # Presents the data inside the columns of the table in the database as json    
    files = crud.get_files()    
    # Makes json objects which are easily parseable by browsers
    return jsonify(files)


# POST(http method) and Create(CRUD)
@app.route('/file', methods=["POST"])
def insert_file():
    # request.get_json(): parses the incoming json data and returns it
    file_details = request.get_json()
    name = file_details["name"]
    format = file_details["format"]
    subject = file_details["subject"]
    result = crud.insert_file(name, format,subject)
    return jsonify(result)


# PUT(http method) and Update(CRUD)
@app.route('/file', methods=["PUT"])
def update_file():
    file_details = request.get_json()
    id = file_details["id"]
    name = file_details["name"]
    format = file_details["format"]
    subject = file_details["subject"]
    result = crud.update_file(id, name, format,subject)
    return jsonify(result)


# DELETE(http method) and Delete(CRUD)
@app.route('/file/<id>', methods=["DELETE"])
def delete_file(id):
    result = crud.delete_file(id)
    return jsonify(result)



@app.route('/file/<id>', methods=["GET"])
def get_file_by_id(id):
    file = crud.get_file_by_id(id)
    return jsonify(file)


if __name__ == "__main__":
    create_table()
    app.run()

