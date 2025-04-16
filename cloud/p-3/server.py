from flask import Flask,request,jsonify
app=Flask("RS to $")
@app.route('/convert',methods=['POST'])
def convertion_rs():
    try:
        data=request.get_json()
        amt_rs=data['rs']
        rate=0.012
        dollar=amt_rs*rate
        return jsonify({"result":f"RS{amt_rs}==>${format(dollar,'.4f')}"})
    except Exception as e:
        return jsonify({"error":str(e)}),500
    
if __name__=="__main__":
    app.run(debug=True,port=8796)