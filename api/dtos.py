from pydantic import BaseModel 


class user(BaseModel):
    first_name : str
    last_name : str
    email : str
    password : str
    phone : str
    status: str
    created_by : int
    updated_by : int

    

class user_login(BaseModel):
    email : str
    password : str
