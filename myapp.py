from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return{
        "status":"SUCCESS",
        " data":{
            "regno": 24122038,
            "name":"sumit",
            "email":"sumit.desale@gmail.com",


        }
    }

if __name__ == "__main__":
    app.run(debug=True)
