from flask import Flask,request,send_from_directory
import os
app=Flask(__name__)
UPLOAD_FOLDER="uploads"
os.makedirs(UPLOAD_FOLDER,exist_ok=True)
@app.route('/upload',methods=['POST'])
def upload_file():
    file=request.files.get('file')
    if file:
        file_path=os.path.join(UPLOAD_FOLDER,file.filename)
        file.save(file_path)
        return{"message":f"file '{file.filename}' uploaded sucessfully"},200
    return {"error":"no file uploaded"},404

@app.route("/download/<filename>",methods=['GET'])
def download_file(filename):
    try:
        return send_from_directory(UPLOAD_FOLDER,filename,as_attachment=True)
    except FileNotFoundError:
        return {"error":"file not found"},404

if __name__=="__main__":
    app.run(debug=True)
