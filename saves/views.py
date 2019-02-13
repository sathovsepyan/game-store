from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

import json

from saves.models import Save
from games.models import Game


@login_required
def savegame(request, game_id):
    user = request.user
    game = get_object_or_404(Game, pk=game_id)
    data = {}
    data['state'] = 'ok'
    # TODO: bruno make the request override, current state.
    # First we fetch the previos state, then we override to the new gamestate.
    # TODO: Try to use csfr tokem. change to POST request.
    toSave = Save.objects.create(game=game, user=user, gamestate=request.GET.get('gameState'))
    return JsonResponse(data)
    
@login_required
def loadgame(request, game_id):
    # user = request.user
    # If there is no object, try and catch
    # TODO:
    # catch the other error that is associated with get call.
    toLoad = Save.objects.get(game__id=game_id, user=request.user)
    data = {
        'messageType': "LOAD",
        'gameState': json.loads( toLoad.gamestate)
    }    
    return JsonResponse(data)