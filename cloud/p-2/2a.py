from flask import Flask,Response
import xml.etree.ElementTree as ET
app=Flask(__name__)
@app.route('/',methods=['GET'])
def welcome():
    return "welcome to python web service"
if __name__=="__main__":
    app.run()
