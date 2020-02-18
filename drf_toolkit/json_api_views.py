from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView

from drf_toolkit.json_parser import JsonParser


class JsonApiView(APIView):
    parser_classes = (JsonParser, )
    renderer_classes = (JSONRenderer,)


class AnonymousJsonApiView(JsonApiView):
    authentication_classes = ()
    permission_classes = (AllowAny,)


class AdminJsonApiView(JsonApiView):
    permission_classes = (IsAdminUser,)
