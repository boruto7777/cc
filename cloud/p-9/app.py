from flask import Flask,request,jsonify
app=Flask("PaaS")
platform_sw=[]
@app.route("/create_app",methods=["POST"])
def create_app():
    try:
        data=request.get_json()
        provider="dee coding"
        name=data.get("appname")
        types=data.get("types")
        if not all([name,types]):
            raise ValueError("name & type must be given")
        vm_sw={
            "provider": provider,
            "software name": name,
            "types of software":types
        }

        platform_sw.append(vm_sw)
        return jsonify({"msg":"succesfully craeted software","details":vm_sw})
    
    except Exception as e:
        return jsonify({"error":str(e)}),400
@app.route('/lists',methods=['GET'])
def lists_app():
    return jsonify(platform_sw)
if __name__=="__main__":
    app.run(debug=True,port=4545)