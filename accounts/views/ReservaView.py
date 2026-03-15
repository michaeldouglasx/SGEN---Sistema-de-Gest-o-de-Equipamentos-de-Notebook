from django.http import HttpResponse
from django.shortcuts import render

def Reserva_View(requests):
    return (requests, 'reserva.html') 