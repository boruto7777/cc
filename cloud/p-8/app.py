from flask import Flask,request,jsonify
app=Flask("IaaS")
virtual_servers=[]
storage={
    "used":0,
    "total":100
}

@app.route('/create_server',methods=['POST'])
def create_server():
    global storage
    try:
        data=request.get_json()
        name=data.get('server_name')
        cpu=data.get('cpu')
        ram=data.get('ram')
        if not all([name,cpu,ram]):
            raise ValueError("Something is missing")
        cpu=int(cpu)
        ram=int(ram)
        if cpu<0 and ram<0:
            raise ValueError("cpu and ram must be +ve number")
        if cpu>10 and ram>1000:
            raise ValueError("errro overflow")
        if storage['used']+(cpu*ram)>storage['total']:
            raise ValueError("not enough resources avaible")
        vm_server={
            "server_name":name,
            "cpu":cpu,
            "ram":ram
        }
        virtual_servers.append(vm_server)
        storage['used']+=cpu*ram
        return jsonify({"msg":"new server created successfully",
                        "server":vm_server,
                        "used_resources":storage['used']})
    
    except Exception as e:
        return jsonify({"msg error created succesfully":str(e)})
    
@app.route('/status',methods=['GET'])
def storage_status():
    global storage
    return jsonify(storage)

if __name__=="__main__":
    app.run(port=9087,debug=True)