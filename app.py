# from flask import Flask
# from datetime import datetime
# import re

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# @app.route("/<name>")
# def changeBackground( name):
#     # now = datetime.now()
#     # formatted_now = now.strftime("%A, %d %B, %Y at %X")

#     # # Filter the name argument to letters only using regular expressions. URL arguments
#     # # can contain arbitrary text, so we restrict to safe characters only.
#     # match_object = re.match("[a-zA-Z]+", name)

#     # if match_object:
#     #     clean_name = match_object.group(0)
#     # else:
#     #     clean_name = "Friend"

#     content = "Hello there, " + name + "!"
 
#     return  content 


from flask import Flask, request, render_template
import re
app = Flask(__name__)

@app.route("/",methods=['GET', 'POST'] )
def main():
    colour = "FFFFFF"
    new_colour = request.form.get('colour', '')
    if re.search(r'^[0-9A-F]{6}$', new_colour):
        colour = new_colour

    return render_template('main.html', colour = colour)
  
  