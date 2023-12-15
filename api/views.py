from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer
from .models import Note
from .utils import read_agents


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
            
        return Response("None agents was found for this event type", status=404)
    
    return Response("Bad request", status=400)

