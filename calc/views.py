from django.shortcuts import render
import calculadora
from django.http import HttpResponse

# Create your views here.
def suma(request, op1, op2):
    return HttpResponse(calculadora.suma(op1, op2))
def resta(request, op1, op2):
    return HttpResponse(calculadora.resta(op1, op2))
def mul(request, op1, op2):
    return HttpResponse(calculadora.multiplicacion(op1, op2))
def div(request, op1, op2):
    return HttpResponse(calculadora.division(op1, op2))
def barra(request, op1, op2):
    return HttpResponse("introduce operandos")
    
