import requests
import xml.etree.ElementTree as ET
url="https://www.w3schools.com/xml/tempconvert.asmx"
temp=float(input("enter a temp in celcius:"))
SOAPEnvelop=f"""<?xml version="1.0" encoding="utf-8"?> <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CelsiusToFahrenheit xmlns="https://www.w3schools.com/xml/">
      <Celsius> {temp} </Celsius>
    </CelsiusToFahrenheit>
  </soap:Body>
  </soap:Envelope>""" 

Headers={
     "Content-Type": "text/xml; charset=utf-8",
     "SOAPAction": "https://www.w3schools.com/xml/CelsiusToFahrenheit"
}

response=requests.post(url=url,data=SOAPEnvelop,headers=Headers)
root=ET.fromstring(response.text)
for child in root.iter("{https://www.w3schools.com/xml/}CelsiusToFahrenheitResult"):
    c2f=child.text
    print(f"{temp}c is equal to {c2f}F")
