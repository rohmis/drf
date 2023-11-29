from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['POST',])
def logout_user(request):
    if request.method == "POST":
        request.user.auth_token.delete()
        return Response({"message":"you are loged out"}, status=status.HTTP_200_OK)
