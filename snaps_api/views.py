from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def root_route(request):
    return Response({
        'message': 'My drf API, for my photo sharing website, Snaps.'
    })
