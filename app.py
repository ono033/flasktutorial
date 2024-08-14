# Flask initialized
from flask import Flask
from views import views
app = Flask(__name__)

app.register_blueprint(views, url_prefix="/views")    #accesses urls when/
# # one way to do roots

#@app.route("/")
#def home():
#    return "This is ono's home page"


if __name__ == '__main__':
    app.run(debug=True, port=8000)  # debug means the server will be refreshed

