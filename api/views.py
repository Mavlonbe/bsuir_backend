from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Note
from .utils import read_agents

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {'Endpoint': '/notes/',
         'method': 'GET',
         'body': None,
         'description': 'Returns an array of notes'},
        
        {'Endpoint': '/notes/id',
        'method': 'GET',
        'body': None,
        'description': 'Returns a single note object'},
        
        {'Endpoint': '/notes/create/',
        'method': 'POST',
        'body': {'body': ""},
        'description': 'Creates new note with data sent in post req'},
    ]
    
    
    return Response(routes)


@api_view(['POST'])
def takeEvent(request):
    data = request.data 
    
    body = EventSerializer(data=data, many=False)
    
    if body.is_valid():
        agents = read_agents()
        
        for agent in agents:
            result = agent.trigger(body)
            
            if result != None:
                return Response(result, status=200)
            
        return Response("None triggers was found", status=200)
    
    return Response(status=400)
