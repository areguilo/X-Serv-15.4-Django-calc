from django.shortcuts import render
import calculadora
from django.http import HttpResponse

# Create your views here.
def suma(request, op1, op2):
    op1 = float(op1)
    op2 = float(op2)
    return HttpResponse(calculadora.suma(op1, op2))
def resta(request, op1, op2):
    op1 = float(op1)
    op2 = float(op2)
    return HttpResponse(calculadora.resta(op1, op2))
def multiplicacion(request, op1, op2):
    op1 = float(op1)
    op2 = float(op2)
    return HttpResponse(calculadora.multiplicacion(op1, op2))
def division(request, op1, op2):
    op1 = float(op1)
    op2 = float(op2)
    return HttpResponse(calculadora.division(op1, op2))
def barra(request):
    return HttpResponse("introduce operandos")
def error(request):
    return HttpResponse("Error, \n"+"suma:sum, resta:res, multiplicacion:mul, division:div")
