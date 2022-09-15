from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self , requste):
        return render(requste, 'home/index.html')
