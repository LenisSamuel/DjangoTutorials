from django.views import View
from django.shortcuts import render

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV"},
        {"id":"2", "name":"iPhone", "description":"Best iPhone"},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
        {"id":"4", "name":"Glasses", "description":"Best Glasses"}
    ]

class ProductShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        product = Product.products[int(id)-1]

        viewData = {}
        viewData["title"] = product["name"]
        viewData["subtitle"] = "Product information"
        viewData["product"] = product

        return render(request, self.template_name, viewData)