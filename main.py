from fastapi import FastAPI

"""from fastapi import FastAPI

app = FastAPI()
@app.get("/item/{item_id}")
async def read_item(item_id:int):
    return {"item_id":item_id}"""
    
from enum import Enum
from fastapi import FastAPI

class class_name(str,Enum):
    alexnet ="alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
app=FastAPI()


"""@app.get ("/model/{model_name}")
async def model_name(model_name: ModelNam    e):
    if model_name is ModelName.alexnet:
        return {"model_name":model_name , "message":"helloworld"}

    
    if model_name.value == "lenet":
        return{"model_name":model_name, "message":"how are you"}
        return {"model_name":model_name,"mesage":"how are you"}   """
        
        
        
"""from typing import Union  
from fastapi import FastAPI
from pydantic import Basemodel

class item (Basemodel):
    ame: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item    """
    
    
    


"""from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
    
    
    
    
    from fastapi import FastAPI, Path
    app=FastAPI()
    @app.get ("/item/{item_id}")
    async def read_items(
        *,item_id:int=Path(little="The ID of the item to get",ge=1),q=str
        
    ):
        return {"item_id":iteem_id}
    if q:
        return.update({"q":q})
    return results
    
    
    
    
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
    
    
    
    
    
from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
    
    



from typing import Union
from fastapi import FastAPI
from pydantic import Basemodel

class iteam (Basemodel):
    name:str
    discription:Union(str,None)=None
    price:float
    tax: Union(float,None)=None
    tag:list= []
    
@app.put("/items/{item_id}")
async def update_item(item_id:int,item:Item):
    return {"item_id":item_id,"item":item}
    return results
    
    
    
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
class item (BaseModel):
    name:str
    description:Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    tags:list=[]
    
@app.put("/items/{item_id}")
async def update_item(item_id:int,item:item):
    results={"item_id":item_id,"item":item}
    return results  """   
     
     
     
"""from typing import Union 


from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()

class Image (BaseModel):
    url:HttpUrl
    name:str
    
class Item (BaseModel):
    name:str
    description :Union[str,None]= None
    price:float
    tax:Union[float,None]= None
    tag:set[str]=set()
    image:Union[Image,None]=None      


   
    
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results ={"item_id":item_id,"item":item}
    return results"""
    
    
    



"""from fastapi import FastAPI 
from pydantic import BaseMOdel


app = FastAPI()


class Item (BaseMOdel):
    name:str
    description: str|None=None
    price:float
    tax:float|None=None
    
    class config:
        schema_extra ={
            "example":{
                "name":"foo",
                "description":"a very nice Item",
                "price":35.4,
                "tax":3.2
            }
        }
        
@app.put ("/items/{iteam_id}")
async def update_item(item_id:int,item:Item):
    results_{"item_id":item_id,"item":item}
    return results"""
    
    
    
    
    
    
    



"""from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,  
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results
    
from datetime import datetime,time,timedelta
from uuid import UUID


from fastapi  import BODY ,FastAPI
app=FastAPI()
@app.put ("/items/{item_id}")
async def read_items(
    item_id:UUID
    start_datetime:datetime |None = BODY(default=None)
    end_datetime:datetime |none=BODY(default=None),
    repeat_at:time | None=BODY(default=None),
    process_after:timedata | None=BODY(default=None)
):
    start_process= start_datetime +process_after
    duration = end_datetime -start_process
    return{
        "item_id":item_id,
        "start_datetime": start_datetime,
        "end datetime": end_datetime,
        "repeat_at":repeat_at,
        "process_after":process_after,
        "start_process":start_process,
        "duration":duraction,
    }                    

       
from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
app=FastAPI()


class Item (BaseModel):
    name:str
    discription :Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    tag:list[str]=[]
    
    
    
    
@app.put ("/items/{item_id}")
async def update_item (item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results    

    
    
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app= FastAPI()


class Item (BaseModel):
    name:str
    description:Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    tag:set[str]=set()
    
    
@app.put ("/items/{item_id}")
async def update_item (item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results  
    
    
    
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl


app= FastAPI()


class Image(BaseModel):
    url:HttpUrl
    name:str
    
    
class Item (BaseModel):
    name:str
    description: Union[str,None]=None
    price:float
    tax:Union[float,None]=None
    tags:set[str]=set()
    images:Union[list[Image],None]=None
    
    
class offer(BaseModel):
    name:str
    descrition:Union[str,None]=None
    price:float
    items:list[Item]
    
    
@app.post("/offers/")
async def create_offer(offer:offer):
    return offer   
    
    
    
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel,field
app=FastAPI()

class Item (BaseModel):
    name:str=filed(example="foo")
    description:Union[str,None]=filed(default=None,example="a very nice Item")
    price:float=filed(example=35.4)
    tax:Union[float,None]=filed(default=None,example=3.2)
    
    
@app.put("/item/{item_id}")
async def update_item (item_id:int,item:Item):
    results={"item_id":item_id,"item":item}
    return results     """
    
    
from typing import Union

from fastapi import  cookie,FastAPI

app= FastAPI()

@app.get ("/items/")
async def read_items(ads_Id:Union[str,none]=cookie(default=None)):
    return{"ads_Id":ads_Id}                    


