# Views are roots, endpoint of url eg \home 
from flask import Blueprint, render_template, request, jsonify, redirect, url_for

#put filename = blueprint
views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html", name = "Tim") # can pass in variables = tim
    #return "home page"

    #new route

@views.route("/CV")
def CV():
    return render_template("CV.html")

@views.route("/Projects")
def Projects():
    return render_template("Projects.html")

@views.route("/GitHub")
def GitHub():
    return redirect ('https://github.com/ono033') 

@views.route("/Games")
def Games():
    return render_template("Games.html")


@views.route("/Contact")
def Contact():
    return render_template("Contact.html")





#@views.route("/profile/<username>")
#def profile(username):
#    #http://127.0.0.1:8000/views/profile/me
#    return render_template("index.html", name = username)

@views.route("/profile")
def profile():
    #
    args = request.args
    name = args.get('name')
    return render_template("index.html", name = name)


#returning json  object
@views.route("/json")
def get_json():
    return jsonify({'name':'tim','coolness':10})
#views/json

#if someone sends data in json format 
@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

#redirecting
@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home")) # since template name is views then . function name
