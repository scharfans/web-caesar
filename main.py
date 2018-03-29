from flask import Flask, request, redirect
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px    
            }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
        <label> Rotate by:
        <input id="Rotate by" name="rot" type="text"/>
        </label>
        <label> 
        <textarea name="text" >{0}</textarea>
        </label>
        <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form.format("")


@app.route("/encrypt", methods=['POST'])
def encrypt():
    rot1 = int(request.form['rot'])
    text1 = request.form['text']
    encrypted_message = rotate_string(text1, rot1)
    return "<h1>" + form.format(encrypted_message) + "</h1>"
    
app.run()