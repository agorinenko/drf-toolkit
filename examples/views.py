from power_dict.utils import DictUtils
from rest_framework.response import Response

from drf_toolkit.decorators import except_error, validate_request
from drf_toolkit.json_api_views import AnonymousJsonApiView


class LoginView(AnonymousJsonApiView):
    @except_error()
    @validate_request(
        [
            {'name': 'username', 'type': "str", 'required': True, 'description': 'User login',
             'required_error': 'User login is not specified'},
            {'name': 'password', 'type': "object", 'required': True, 'description': 'User password',
             'required_error': 'The user password is not specified'},
        ])
    def post(self, request, *args, **kwargs):
        username = DictUtils.get_required_str_dict_property(kwargs['context'], "username")
        password = DictUtils.get_required_str_dict_property(kwargs['context'], "password")

        # authenticate user with username / password

        return Response({
            # User info
        })
