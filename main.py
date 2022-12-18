
"""from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app=FastAPI()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
class userout(BaseModel):
    username:str
    email:EmailStr
    full_name:Union[str,None]=None
    
class UserInDB(BaseModel):
    username:str
    hashed_password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
def fake_password_hasher(raw_password:str):
    return "supersecret" +raw_password


def fake_save_user(user_in:UserIn):
    hashed_password=fake_password_hasher(user_in.password)
    user_in_db=UserInDB(**user_in.dict(),hashed_password=hashed_password)
    print("user saved!..not really")
    return user_in_db     """
    
    
    
    
    
 #       ****reduce duplication***
        


"""from  typing import Union
from fastapi import FastAPI
from  pydantic import BaseModel,EmailStr

app=FastAPI


class UserBase(BaseModel):
    username:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
class UserIn(UserBase):

    password:str
    
    
class Userout(UserBase):
    pass        
     

class UserInDB(UserBase):
    hashed_password:str
    
    
    
def fake_password_hasher(raw_password:str):
    return"supersecret"+raw_password
    

def fake_save_user(user_in:UserIn):
    hashed_password+fake_password_hasher(user_in.password)
    user_in_db=UserInDB(**user_in.dict(),hashed_password=hashed_password)
    print("user saved!..not really")
    return user_in_db   """                
    
    
    
    
    
    
    #  ....union or anyOf....
    
"""from typing import Union
from  fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()


class BaseItem(BaseModel):
    description:str
    type:str
    
class carItem(BaseModel):
    type="car"
    
    
class PlaneItem(BaseModel):
    type="plane"
    size:int        
         

items ={
    "item1":{"description":"All my friends drive a low rider","type": "car"},
     "item2":{
         "description":"music is my aeroplane,it's my aeroplane",
         "type":"plane",
         "size":5,
     },        
             
}         
         
@app.get("/items/{item_id}",response_model=Union[PlaneItem,carItem])
async def read_item(item_id:str):
  return items[item-id]     """
  
  
  
  #...list of models....
  


"""from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Item (BaseModel):
    name:str
    description:str
    
    
    
items = [
    
    {"name":"foo","description":"there comes my hero"},
    {"name":"Red","description":"it's my aeroplane"},
    
]      
  
@app.get("/items/",response_model=list[Item])
async def read_items():
    return items  """
    
    
    #....response statas code...
    
    
    
"""from fastapi import FastAPI

app = FastAPI()

@app.post("/items/",status_code=201)
async def create_item(name:str):
    return {"name":name}"""
    
    
    
    #...short to remember the names
    
"""from fastapi import FastAPI
app = FastAPI()

@app.post ("/items/",status_code=201)
async def  create_item(name:str):
    return{"name":name}"""
    
#.... import form....

"""from fastapi import FastAPI,Form

app = FastAPI()

@app.post("/login/")
async def login(username:str = Form(), password:str =Form()):
    return {"username:username"}"""
    
    #....Request files
    
#....import file.....



"""from fastapi import FastAPI,File,UploadFile

app = FastAPI()

@app.post("/files/")
async def create_file(file:bytes = File()):
    return{"file_size":len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return{"filename":file.filename}"""
    
    
    #...define File parameters...
    
    
"""from fastapi import FastAPI,File,UploadFile
app = FastAPI()
@app.post ("/files/")
async def create_file(file:bytes =File()):
    return {"file_size":len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return{"filename":file.filename} """
    


#..file parameter with uploadfile..


"""from fastapi import FastAPI,File,UploadFile
app = FastAPI()

@app.post("/files/")
async def create_file(file:bytes = File()):
    return {"file_size":len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file:UploadFile):
    return{"filename":file.filename}    """   
    
   
   #...OPTIONAL file upload...
   
   
   
"""from typing import Union
from fastapi import FastAPI,File,UploadFile

app = FastAPI()

@app.post ("/files/")
async def create_file(file:Union[bytes,None]=File(default=None)):
    if not file:
        return{"message":"NO file sent"}
    else:
        return{"file_size":len(file)}
    
@app.post("/uploadfile/")
async def create_upload_file(file:Union[UploadFile,None]=None):
    if not file:
        return{"message":"no upload file sent"}
    else:
        return{"filename":file.filename}  """ 
    

        
    
#...uploadfile with additional metadata..

"""from fastapi import FastAPI,File,UploadFile

app =FastAPI()

@app.post("/files/")
async def create_file(file:bytes = file(description="a file read as bytes")):
    return{"file_size":len (file)}

@app.post ("/uploadfile/")
async def create_upload_file(
    file:UploadFile = File(description= "A file read as uploadfile"),
    
):
    return {"filename":file.filename}"""
    
    
    
    #....multiple file uploads...



"""from fastapi import FastAPI,File,UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.post("/files/")
async def create_files(files:list[bytes]= File()):
    return{"file_sizes":[len(file)for file in files]}


@app.post("/uploadfiles/")
async def create_upload_files(files:list[UploadFile]):
    return{"filenames":[file.filename for file in files]}

@app.get("/")
async def main():
    return HTMLResponse(content=content) """
    
    
   #...multiple file uploads with additional metadata... 
   

"""from fastapi import FastAPI,File,UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.post ("/files/")
async def create_files(
    files:list[bytes] =File(description="multiple files as bytes"),
    
):
    return{"filenames":[file.filename for file in files]}
content =""


@app.get("/")
async def main():
    return HTMLResponse(content=content)  """
    
    
   
      
         
         
         
         
         
         
         
         