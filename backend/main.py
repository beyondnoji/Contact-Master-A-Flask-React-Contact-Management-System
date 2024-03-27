# Writing Routes and Endpoints
# CRUD - Create Read Update and Delete 

# Create (i.e., create a contact)
# - first_name 
# - last_name 
# - email
# Server is running API localhost:5000/home (the endpoint is 'home') 
# localhost:5000/create_contact --> create_contact endpoint
# POST request means you are trying to create something new, i.e. a contact 
# The frontend will send a request of a certain type to the server
# The back-end will return a Response, with a status (error 404)

from flask import request, jsonify # allows to return json data
from config import app, db 
from models import Contact 

@app.route("/contacts", methods=["GET"]) # decorator 
# the list contains the valid methods for the localhost:5000/contacts
def get_contacts():
  contacts = Contact.query.all() 
  # gives a list of all the Contact objects in the DB
  # cannot return Python objects from this code, need to make it json
  json_contacts = list(map(lambda x: x.to_json(), contacts))
  # Do to_json on contacts generated above; then convert the map to list
  return jsonify({"contacts": json_contacts})
  # return a json object that is equal to json_contacts; it is a Python dictionary


@app.route("/create_contact", methods=["POST"]) # POST means create 
def create_contact(): 
  # use the request library imported above to fetch the data
  first_name = request.json.get("firstName")
  last_name = request.json.get("lastName") 
  email = request.json.get("email") 

  if not first_name or not last_name or not email: # if missing 
    return (
      jsonify({"message": "You must include a first name, last name and email"}), 
      400, # error number
    )
  
  # if all data was found 
  # construct the Python contact class 
  new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
  # Object is created but has not yet been commited to the database
  try: 
    db.session.add(new_contact)
    # db.session.commit can cause errors sometimes so put it inside try catch block
    db.session.commit() 
  except Exception as e:
    return jsonify({"message": str(e)}), 400 
  return jsonify({"message": "User created!"}), 201 

# Updating the DB
@app.route("/update_contact/<int:user_id>", methods=["PATCH"]) # update the user's id 
def update_contact(user_id): # the arg to this function matches name in the route! 
  contact = Contact.query.get(user_id)

  if not contact:
    return jsonify({"message": "User not found"}), 404 
  
  # Else, update the user's info
  data = request.json # RETURNS A DICTIONARY 
  contact.first_name = data.get("firstName", contact.first_name) 
  # data.get looks for the pair with key "firstName" and if it doesn't find it, returns the 2nd arg (i.e., contact.first_name)
  # that is to say, contact.first_name = new name 
  contact.last_name = data.get("lastName", contact.last_name) 
  contact.email = data.get("email", contact.email) 
  db.session.commit() # commit the update to db
  return jsonify({"message": "User updated!"}), 200

@app.route("/delete_contact/<int:user_id>", methods=["DELETE"])
# the <int:user_id> part is path parameter to specify the input 
def delete_contact(user_id): 
  contact = Contact.query.get(user_id) # gets the contact with that user_id 
  if not contact:
    return jsonify({"message": "User not found"}), 404

  db.session.delete(contact) # deletes the contact from db
  db.session.commit() # commits the change 
  return jsonify({"message": "User deleted!"}), 200

if __name__ == "__main__": # run the Flask app
  # instantiate the database 
  with app.app_context():
    db.create_all() # creates all the modles in the database if it D.N.E
  app.run(debug=True)