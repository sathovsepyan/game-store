from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def savegame(request, game_id, user_id):
    data = {}
    data['state'] = 'ok'
    return JsonResponse(data)
    
    
