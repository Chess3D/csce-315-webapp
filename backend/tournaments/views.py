from django.shortcuts import render
from django.http import HttpResponse
from .models import Tournament
from .serializers import *

@api_view(['GET', 'POST'])
def tournaments_list(request):
    if request.method == 'GET':
        data = Tournament.objects.all()
        serializer = TournamentSerializer(data, context={'request', request}, many=True)
        return HttpResponse(serializer.data)
    elif request.method == 'POST':
        serializer = TournamentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.sasve()
            return HttpResponse(status=status.HTTP_201_CREATED)

@api_view(['PUT', 'DELETE'])
def tournaments_details(request, pk):
    try:
        tournament = Tournament.objects.get(pk=pk)
    except Tournament.DoesNotExist:
        return HttpResponse(status.status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = TournamentSerializer(tournament, data=request.data, context={'request', request})
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=.statusHTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)