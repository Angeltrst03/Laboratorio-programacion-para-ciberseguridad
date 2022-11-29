import requests
import base64
from requests import Response
#Jorge Angel Valdez Tristam
#1957496
if __name__ =="__main__":
    url="https://i.imgur.com/ecrc7Hn.jpeg"

    Response: Response= requests.get(url, stream=True)
    with open("cat.jpg","wb") as file_down:
        for chunk in Response.iter_content():
             file_down.write(chunk)
    Response.close()



with open ("cat.jpg", "rb") as binary_file:
    binary_file_data = binary_file.read()
    base64_encoded_data = base64.b64encode (binary_file_data)
    base64_message = base64_encoded_data.decode ("utf8")

print(base64_message)
