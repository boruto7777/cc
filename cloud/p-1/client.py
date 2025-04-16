from zeep import Client
client=Client("http://127.0.0.1:7567/?wsdl")
result_add=client.service.add_numbers(21,32)
result_sub=client.service.sub_numbers(32,21)
result_mul=client.service.mul_numbers(2,3)
print(f"adding number:{result_add}")
print(f"subtracting number:{result_sub}")
print(f"multiplying number:{result_mul}")
