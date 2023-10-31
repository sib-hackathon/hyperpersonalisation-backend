from django.shortcuts import render
from rest_framework.views import APIView
from suggestions.models import Button, UserButtonInteraction, UserAddedButtons
from django.db.models import Count
from suggestions.serializer import ButtonSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ButtonSuggestionView(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request):
    """
    This function is called when a user wants to see the top 5 buttons he clicked on
    """
    user = request.user
    #gets the top 5 clicked buttons by this user
    query_set = UserButtonInteraction.objects.filter(user=user).values('button__id', 'button__name').annotate(count=Count('button')).order_by()[:5]
    serializer = ButtonSerializer(query_set, many=True)
    return Response(serializer.data)
  
  def post(self, request):
    """
    This function is called when a user clicks on a button
    """
    user = request.user
    button_id = request.data['button_id']
    button = Button.objects.get(id=button_id)
    user_button_interaction = UserButtonInteraction(user=user, button=button)
    user_button_interaction.save()
    return Response(status=201)
  

class CustomSavedButtons(APIView):
  permission_classes = [IsAuthenticated]
  
  def get(self, request):
    """
    This function is called when a user wants to see his saved buttons
    """
    user = request.user
    buttons = UserAddedButtons.objects.filter(user=user).values('button__id', 'button__name').annotate(count=Count('button')).order_by()
    serializer = ButtonSerializer(buttons, many=True)
    return Response(serializer.data)

  def post(self, request):
    """
    This function is called when a user saves a button on his interest
    """
    user = request.user
    button_id = request.data['button_id']
    button = Button.objects.get(id=button_id)
    user_saved_button = UserAddedButtons(user=user, button=button)
    user_saved_button.save()
    return Response(status=201)