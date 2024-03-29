class Vehicle:
    def __init__(self,type:str,model:str,price:int):
        self.type=type
        self.model=model
        self.price=price
        self.owner=None

    def buy(self,money: int, owner: str):
        self.money=money
        self.owner=owner
        if money>self.price and owner==None:
            return f"Successfully bought a {self.type}. Change: {money-self.price}"
        elif money<self.price:
            return f"Sorry, not enough money"
        else:
            return f"Car already sold"

    def sell(self):
        if self.owner!=None:
            self.owner=None
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner != None:
            return f"{self.model} {self.type} is owned by: {self.owner}"
        else:
            return f"{self.model} {self.type} is on sale: {self.price}"
