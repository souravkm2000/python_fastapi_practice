"""from  typing import Union

from fastapi import FastAPI,Header

app = FastAPI()

@app.get("/items/")
async def read_items(user_agent:Union[str,None]=Header(default=None)):
    return {"user-agent:user_agent"}
    
    
from typing import Union 
from fastapi import FastAPI,Header

app = FastAPI()

@app.get("/items/")
async def read_items(
    strange_header:Union[str,None]=Header(default=None,convert_underscores=False)
):
    return {"strange_header":strange_header}  
    
    
from typing import Union 

from fastapi import FastAPI,Header

app = FastAPI()

@app.get("/items/")
async def read_items(x_token:Union[list[str],None]=Header(default=None)):
    return {"x-token values":x_token} 
    
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()
 
 
class Item (BaseModel):
    name:str
    description:Union[str,None]=None
    price: float
    tax:Union[float,None]=None
    tags:list[str]=[]


@app.post ("/items/",response_model=Item)
async def create_item (item:Item):
    return item    """
    
    
"""from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr


app = FastAPI()


class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
@app.post("/user/",response_model=UserIn)
async def create_user(user:UserIn):
    return user
    
    

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel,EmailStr

app=FastAPI()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
@app.post("/user/",response_model=UserIn)
async def  create_user(user:UserIn):
    return user     """
    
    
    
"""from typing import Union


from fastapi import FastAPI
from pydantic import BaseModel,EmailStr


app = FastAPI()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None   
    
    
class UserOut(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None     
       
      
@app.post("/user/",response_model=UserOut)
async def create_user(user:UserIn):
    return user 
    
    
    
from typing import List, Union

from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Item(BaseModel):
    name:str
    description:Union [str,None]=None
    price:float
    tax:float=10.5
    tags:list[str]=[]
    
    items={
         "foo":{"name":"foo","price":50.2},
         "bar":{"name":"Bar","description":"the bartenders","price":62,"tax":20.2},
         "baz":{"name":"Bar","description":None,"price":50.2,"tax":10.5,"tags":[]},
         
    }  
    
@app.get("/items/{item_id}",response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id:str):
    return items[item_id] """
    
    
"""from typing import Union

from  fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name:str
    description:Union [str,None]=None
    price:float
    tax:float=10.5
    
    
items={
    "foo":{"name":"foo","price":50.2},
    "bar":{"name":"bar","description":"the Bar fighters","price":62,"tax":20.2},
    "baz":{
        "name":"baz",
        "description":"there goes my baz",
        "price":50.2,
        "tax":10.5,
        
    },
    
}    
    

    
@app.get(
    
    "/items/{item_id}/name",
    response_model=Item,
    response_model_include=["name","description"],
)     

async def read_item_name(item_id:str):
    return items[item_id]

@app.get ("/items/{item_id}/public",response_model=Item,response_model_exclude=["tax"])  
async def read_item_public_data(item_id:str):
    return items[item_id]"""




"""from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,EmailStr


app= FastAPI()

class UserIn(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
class UserOut(BaseModel):
    username:str
    password:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
class userINDB(BaseModel):
    username:str
    email:EmailStr
    full_name:Union[str,None]=None
    
    
    
def fake_password_hasher(raw_password:str):
    return"supersecret"+raw_password


def fake_save_user(user_in:UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db=userINDB(**user_in.dict(),hashed_password=hashed_password)
    print("user saved!..not really")
    return user_in_db



@app.post("/user/",response_model=UserOut)
async def create_user(user_in:UserIn):
    user_saved=fake_password_hasher(user_in)
    return user_saved  
    
    
from typing import Union
from Fastapi import FastAPI
from pydantic import BaseMOdel,EmailStr

app = FastAPI()

class userBase(BaseMOdel):
    username:str
    Email: EmailStr
    full_name:Union[str,None]=None
    
    
class UserIN(UserBase):
    password:str
    
class UserIn(UserBase):
    pass

class userINDB(userBase):
    hashed_password:str


def fake_password_hasher(raw_password:str):
    return "supersecret"+raw_password


def fake_save_user(user_in:UserIn):
    hashed_password=fake_password_hasher(user_in.password)
    user_in_db=userINDB(**user_in.dict(),hashed_password=hashed_password)
    print("user saved!..not really")
    return user_in_db



@app.post("/user/",response_model=UserOut)
async def  create_user(user_in:UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved """
    
    
    
    
"""from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app =FastAPI()

class BaseItem(BaseModel):
    description:str
    typr:str
    
class CarItem(BaseItem):
    type ="car"
    
class PlaneItem(BaseItem):
    type="plane"
    size:int
    
    
items = {
    
    "item1":{"description": "All my friends drive a low rider","type":"car"},
    "item2":{
        "description":"music is my aeroplane, it's my aeroplane",
        "type":"plane",
        "size":5,
    },
} 

@app.get ("/items/{item_id}"response_model=Union[planeItem,carItem])
async def read_item(item_id:str):
    return items[item_id]   """            
                                       