from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

import json

from saves.models import Save
from games.models import Game


@login_required
def savegame(request, game_id):
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    data = {}
    data['state'] = 'ok'

    # check if the user request.user belongs  to the game/profile.
    if game not in request.user.profile.games.all():
        raise PermissionDenied()

    try:        
        toSave = Save.objects.get(game=game, user=user)
        # If we have a save already, we update it
        toSave.gamestate = request.GET.get('gameState')    
        toSave.save()   
    except Save.DoesNotExist:        
        toSave = Save.objects.create(game=game, user=user, gamestate=request.GET.get('gameState'))
    except Exception as e:
        data = {
            'messageType': "ERROR",
            'info': 'Error saving the game state.'
        } 

    # TODO: Try to use csfr tokem. change to POST request.
    # toSave = Save.objects.create(game=game, user=user, gamestate=request.GET.get('gameState'))
    return JsonResponse(data)
    
@login_required
def loadgame(request, game_id): 
    game = get_object_or_404(Game, pk=game_id)
    # check if the user request.user belongs  to the game/profile.
    if game not in request.user.profile.games.all():
        raise PermissionDenied()

    try:
        toLoad = Save.objects.get(game__id=game_id, user=request.user)
        data = {
            'messageType': "LOAD",
            'gameState': json.loads( toLoad.gamestate)
        }    
    except Save.DoesNotExist:            
        data = {
            'messageType': "ERROR",
            'info': 'There is no game to load'
        }   
    except Save.MultipleObjectsReturned:
        data = {
            'messageType': "ERROR",
            'info': 'There are many games to load'
        } 

    return JsonResponse(data)