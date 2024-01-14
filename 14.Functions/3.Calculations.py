# "multiply", "divide", "add", "subtract"

def multiply(a,b):
    return a*b

def divide(a,devidor):
    return a//devidor

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

action=input()
a=int(input())
b=int(input())
if action=='multiply':
    print(multiply(a,b))

elif action=='divide':
    print(divide(a,b))

elif action=='add':
    print(add(a,b))

elif action=='subtract':
    print(subtract(a,b))