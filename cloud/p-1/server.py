from wsgiref.simple_server import make_server
from spyne.application import Application
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.decorator import rpc
from spyne.model.primitive import Integer

class Calculation(ServiceBase):
    @rpc(Integer,Integer,_returns=Integer)
    def add_numbers(ctx,num1,num2):
        return num1+num2
    
    @rpc(Integer,Integer,_returns=Integer)
    def sub_numbers(ctx,num1,num2):
        return num1-num2
    
    @rpc(Integer,Integer,_returns=Integer)
    def mul_numbers(ctx,num1,num2):
        return num1*num2
    
soap_app=Application(
    [Calculation],tns="exmaple.soap",
    in_protocol=Soap11(validator="lxml"),out_protocol=Soap11())

wsgi_app=WsgiApplication(soap_app)
host="127.0.0.1"
port=7567
server=make_server(host,port,wsgi_app)
print(f"soap server is running on http://{host}:{port}")
server.serve_forever()
    


