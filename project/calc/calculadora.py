#/usr/bin/python3
import sys

def suma(num1, num2):
    return num1+num2
    
def resta(num1, num2):
    return num1-num2
 
def multiplicacion(num1, num2):
    return num1*num2
    
def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return("Zero Division Error")  

diccionario = {"sum":suma, "res":resta, "mul":multiplicacion, "div":division}
