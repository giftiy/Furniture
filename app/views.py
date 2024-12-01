
    
    
from django.views import View
from django.shortcuts import render

def home(request):
    return render(request, "app/home.html")  # This path should match your directory structure

class CategoryView(View):
    def get(self, request):
        return render(request, 'app/category.html')  # Adjust the template path as needed    