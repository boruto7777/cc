from flask import Flask,request,jsonify,Response
import xml.etree.ElementTree as ET
app=Flask("Books app")
books=[
    {"id":1,"title":"cc","author":"aparna mam"},
    {"id":2,"title":"wsn","author":"gyaneshwari mam"}
]

#get all books in json
@app.route("/books",methods=["GET"])
def get_books():
    if len(books)!=0:
        return jsonify({"Result":books})
    else:
        return jsonify({"error":"books not found"}),400
    
#get all books in xml
@app.route('/all_books',methods=['GET'])
def get_all_books():
    root=ET.Element("books")
    for book in books:
        xml_book=ET.SubElement(root,'book')
        xml_book.set('id',str(book['id']))
        b_title=ET.SubElement(xml_book,'title')
        b_title.text=book['title']
        b_author=ET.SubElement(xml_book,'author')
        b_author.text=book['author']
    xml_string=ET.tostring(root)
    return Response(xml_string,mimetype='text/xml')

#get a apecific book by id 
@app.route('/book/<int:b_id>',methods=['GET'])
def get_a_book(b_id):
    book=next((b for b in books if b['id']==b_id),None)
    if book: 
        return jsonify(book)
    else:
        return jsonify({"error":f"book not found with id={b_id}"}),404
    
#update a book by id 
@app.route("/book/edit/<int:b_id>",methods=['PUT'])
def update_book(b_id):
    book=next((b for b in books if b["id"]==b_id),None)
    if book:
        data=request.get_json()
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"error":f"book not found with id={b_id}"}),404
    
#adda a new book
@app.route("/book/add",methods=["POST"])
def add_book():
    data=request.get_json()
    new_book={"id":len(books)+1,"title":data["title"],"author":data["author"]}
    books.append(new_book)
    return jsonify({"new added book":new_book,"All books":books})


#remove a book by id 
@app.route("/book/remove/<int:bid>",methods=['DELETE'])
def remove_book(bid):
    book=next((b for b in books if b["id"]==bid),None)
    if book:
        books.remove(book)
        return jsonify({"msg":f"book removed succesfully with id:{bid}"})
    else:
        return jsonify({"error":f"book not found with id={bid}"}),404
    
if __name__=="__main__":
    app.run(debug=True,port=5643)

    
