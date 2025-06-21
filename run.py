from app import create_app  #To start the Flask app

#Creating flask app
app = create_app()

#Starting the server when this file directly run
if __name__ == "__main__":
    app.run(debug=True)