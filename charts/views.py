from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import View
import random

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

class APIViewPie(View):
    def get(self, request):
        values = [random.randint(1,100) for _ in range(3)]
        labels = ['Red Lorries', 'Yellow Lorries', 'Blue Lorries']
        label = "Distribution of Lorries"
        backgroundColor = ["rgb(255, 99, 132)","rgb(54, 162, 235)","rgb(255, 205, 86)"]
        data = {
            'datasets': [{
                'label': label,
                'data': values,
                'backgroundColor': backgroundColor,
            }],
            'labels': labels
        }
        return JsonResponse(data)

class APIViewBar(View):
    def get(self, request):
        barChartsData = {
            'labels': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'datasets': [
                {
                'label': 'Red Lorries',
                'backgroundColor': "rgb(255, 99, 132)",
                'data':[random.randint(1,10) for _ in range(6)]
                },
                {
                'label': 'Yellow Lorries',
                'backgroundColor': "rgb(54, 162, 235)",
                'data':[random.randint(1,10) for _ in range(6)]
                },
                {
                'label': 'Blue Lorries',
                'backgroundColor': "rgb(255, 205, 86)",
                'data':[random.randint(1,10) for _ in range(6)]
                }
            ]}
        return JsonResponse(barChartsData)
