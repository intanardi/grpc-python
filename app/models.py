import datetime

class User():
    def login(self, username, password):
        _data = [{"username" : "ardi", "password" : 12345}, {"username" : "james", "password" : 54321}, {"username" : "r", "password" : 000}]
        for i in _data:
            if username == i['username'] and password == i['password']:
                return True
        
        return False

class Order():
    def getAllOrder(self):
        _data = {
                "order": [
                    {
                        "order_no" : "abc123",
                        "total_items":2,
                        "detail" :
                        [
                            {
                                "product_id": 1,
                                "name": "Nasi Goreng",
                                "price": 20000
                            }
                        ],
                    },
                ],
                "total_revenue": 40000,
                "transaction_date": datetime.datetime.now()
                
            }
        return _data
    
    def getOrdertById(self, id):
        _data = {
                "order_no": "abc123",
                "id_product": 1,
                "name": "Nasi Goreng",
                "price": 20000,
                "total_order": 1,
                "total_price": 20000,
                "total": 20000
                }
        return _data
        
