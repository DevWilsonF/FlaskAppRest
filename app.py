from flask import Flask, request

app = Flask(__name__)

shops = [{"name": "My Shops", "products": [{"name": "Chair", "price": 15.99}]}]


@app.get("/shop")
def get_shops():
    return {"shops": shops}


@app.post("/shop")
def create_shop():
    request_data = request.get_json()
    new_shop = {"name": request_data["name"], "products": []}
    shops.append(new_shop)
    return new_shop, 201


@app.post("/shop/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for shop in shops:
        if shop["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            shop["products"].append(new_item)
            return new_item, 201
    return {"message": "shop not found"}, 404


@app.get("/shop/<string:name>")
def get_shop(name):
    for shop in shops:
        if shop["name"] == name:
            return shop
    return {"message": "shop not found"}, 404


@app.get("/shop/<string:name>/item")
def get_item_in_shop(name):
    for shop in shops:
        if shop["name"] == name:
            return {"products": shop["products"]}
    return {"message": "shop not found"}, 404