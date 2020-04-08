from flask import Flask

UPLOAD_FOLDER = 'C:/Users/Aaryan/OneDrive/Desktop/From Beginning/uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "secret key"
