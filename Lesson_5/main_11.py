from fastapi import FastAPI 

app=FastAPI() 

@app.get("/items/{item_id}") 
async def read_item(item_id: int, q: str=None): 
    if q: 
       return {"item_id": item_id, "q": q} 
    return {"item_id": item_id}


@app.get("/users/{user_id}/orders/{order_id}") 
async def read_data(user_id: int, order_id: int): 
   # Обработка данных
    return {"user_id": item_id, "order_id": order_id}