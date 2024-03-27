from config import db
class  Contact(db.Model): 
    # Declaring the columns and fields for the databse 
    # Creating a Contact with id, first name, last name and email
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # Convert to json object to take it to the frontend
    def to_json(self):         
        return {
            "id": self.id, 
            "firstName": self.first_name,
            "lastName": self.last_name, 
            "email": self.email,
        }
  