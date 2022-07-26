from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer
from .models import Post

@api_view(['GET']) # методы которые могут быть запрошены
def posts_list(request):
    queryset = Post.objects.all()
    serializer = PostSerializer(queryset, many=True)
    return Response(serializer.data)



