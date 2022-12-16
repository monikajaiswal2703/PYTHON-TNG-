class Mobile:
    def __init__(self,brand,model,price):
        self.__brand=brand
        self.__model=model
        self.__price=price
    def get_brand(self):
        return self.__brand
    def get_model(self):
        return self.__model
    def get_price(self):
        return self.__price
    def set_brand(self,_brand):
        self.__brand=_brand
    def set_model(self,_model):
        self.__model=_model
    def set_price(self,_price):
        self.__price=_price
    def call(self,mobile_number):
        print("calling to:-",mobile_number)
    def discount(self,discount_amt):
        self.__price-=discount_amt
phone=Mobile("MI","Redmi Note 11",17000)
#print(phone.brand,phone.model,phone.price)
phone.call(9420534567)
phone.discount(500)
print(phone.get_price())
phone.set_brand("Apple")
phone.set_model("iPhone 12 Pro Max")
phone.set_price(2465900)
print(phone.get_brand(),phone.get_model(),phone.get_price())
print(phone.set_brand(),phone.set_model(),phone.set_price())

