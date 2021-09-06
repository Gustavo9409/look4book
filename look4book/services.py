import os
import http.client
import json

# This function use the open library api (Book API) through an html connection
# ident_strings: Concatenate string of each book id (I chose lccn id)
# Returns an array with specific information of each search
def get_books_by_id(ident_strings):
    valid_info = ["title", "authors", "publish_date", "number_of_pages", "identifiers"]
    conn = http.client.HTTPConnection("openlibrary.org")

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    conn.request("GET", "/api/books?bibkeys="+ident_strings+"&jscmd=data&format=json", headers=headers)

    res = conn.getresponse()
    data = res.read()
    final_data = data.decode("utf-8")
    books = json.loads(final_data)

    books_list = []
    for element in books: 
        data = {}   
        for attr in books[element]:
            if attr in valid_info:               
                if attr == "identifiers":
                    val = books[element][attr]["openlibrary"]
                    attr = "identifier_OL"
                elif attr == "authors":
                    tmp_obj = books[element][attr]
                    auth_arr = []
                    for obj in tmp_obj:
                        auth_arr.append(obj["name"])
                    val = auth_arr
                else:
                    val = books[element][attr]
                data[attr] = val
        books_list.append(data)        
    
    return books_list

# This function use the open library api (Search API) through an html connection
# book_title: String of book's titles separated by pipe '|'
# author_name: String of author's separated by pipe '|'
# Returns a string of each book LCCN id
def get_books_by_param(book_title, author_name):
    
    lccn_arr = []
    conn = http.client.HTTPConnection("openlibrary.org")

    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache"
        }

    titles_arr = book_title.split("|")
    for tle in titles_arr:
        api_title = tle.replace(" ", "+")
        conn.request("GET", "/search.json?title="+api_title, headers=headers)

        res = conn.getresponse()
        data = res.read()
        final_data = data.decode("utf-8")
        books_info = json.loads(final_data)
        
        if len(books_info) > 0:
            for element in books_info:
                if element == "docs":
                    for doc in books_info[element]:
                        if "lccn" in doc:
                            for ident in doc["lccn"]:
                                lccn_arr.append("LCCN:"+ident)
                                
    authors_arr = author_name.split("|")     
    for auth in authors_arr:
        api_auth = auth.replace(" ", "+")
        conn.request("GET", "/search.json?author="+api_auth, headers=headers)

        res = conn.getresponse()
        data = res.read()
        final_data = data.decode("utf-8")
        books_info = json.loads(final_data)
        
        if len(books_info) > 0:
            for element in books_info:
                if element == "docs":
                    for doc in books_info[element]:
                        if "lccn" in doc:
                            for ident in doc["lccn"]:
                                lccn_arr.append("LCCN:"+ident)          
    
    lccn_strings = ','.join(lccn_arr)
    data = get_books_by_id(lccn_strings)
    return data