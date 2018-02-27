from django.shortcuts import render
from django.http import HttpResponse

def book_list(request):
    return HttpResponse("list view")

def book_detail(request, slug):
    return HttpResponse("detail view")

def book_add(request):
    return HttpResponse("add view")

def book_delete(request, slug):
    return HttpResponse("delete view")

def book_edit(request, slug):
    return HttpResponse("edit view")
