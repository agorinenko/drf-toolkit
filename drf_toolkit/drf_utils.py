import logging

from django.contrib.auth import get_user
from django.http import Http404
from power_dict.errors import NoneParameterError, InvalidParameterError, InvalidSchemeError, NotAllowedParameterError
from power_dict.utils import DictUtils
from rest_framework.response import Response
from drf_toolkit.errors import ApiViewError, DjangoModelError


class DrfUtils:
    @staticmethod
    def generate_bad_response(exception: Exception = None, error: str = None, status: int = None) -> Response:
        error_message = 'Возникла неожиданная ошибка. Попробуйте позднее'
        if not DictUtils.str_is_null_or_empty(error):
            error_message = error
        elif exception is not None and not DictUtils.str_is_null_or_empty(str(exception)):
            error_message = str(exception)

        if status is None:
            exception_type = type(exception)

            if exception_type in [
                InvalidParameterError,
                NoneParameterError,
                InvalidSchemeError,
                DjangoModelError,
                NotAllowedParameterError
            ]:
                status = 400
            elif exception_type in [
                ApiViewError
            ]:
                status = exception.status
            elif exception_type in [
                Http404
            ]:
                status = 404
            else:
                status = 500

        logger = logging.getLogger('drf_toolkit')

        if logger is not None:
            if exception is not None:
                logger.exception(exception)
            else:
                logger.exception(error_message)

        return Response({
            'detail': error_message
        }, status=status)

    @staticmethod
    def get_request_parameters(request) -> dict:
        result = {}
        if request.query_params is not None and len(request.query_params) > 0:
            qp = request.query_params.dict()
            result = {**result, **qp}

        if request.data is not None and len(request.data) > 0:
            if type(request.data) == dict:
                qp = request.data
            else:
                qp = dict(request.data)
            result = {**result, **qp}

        return result

    @staticmethod
    def get_request_parameter(request, name):
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_dict_property(qp, name)

    @staticmethod
    def get_required_request_parameter(request, name):
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_required_dict_property(qp, name)

    @staticmethod
    def get_str_request_parameter(request, name, default_value='') -> str:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_str_dict_property(qp, name, default_value)

    @staticmethod
    def get_required_str_request_parameter(request, name) -> str:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_required_str_dict_property(qp, name)

    @staticmethod
    def get_required_int_request_parameter(request, name) -> int:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_required_int_dict_property(qp, name)

    @staticmethod
    def get_int_request_parameter(request, name, default_value=None) -> int:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_int_dict_property(qp, name, default_value)

    @staticmethod
    def get_bool_request_parameter(request, name, default_value=None) -> bool:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_bool_dict_property(qp, name, default_value)

    @staticmethod
    def get_required_bool_request_parameter(request, name) -> bool:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_required_bool_dict_property(qp, name)

    @staticmethod
    def get_required_list_request_parameter(request, name) -> list:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_required_list_dict_property(qp, name)

    @staticmethod
    def get_list_request_parameter(request, name, default_value=None) -> list:
        qp = DrfUtils.get_request_parameters(request)
        return DictUtils.get_list_dict_property(qp, name, default_value)

    @staticmethod
    def get_current_user(request):
        user = get_user(request)
        from django.contrib.auth.models import AnonymousUser
        if type(user) is AnonymousUser:
            return None

        return user

    @staticmethod
    def get_current_user_name(request):
        user = DrfUtils.get_current_user(request)

        if user is None:
            return 'anonymous'

        return user.username

    @staticmethod
    def transform_list_parameters(context: dict, schema: list):
        list_rows = list(filter(lambda x: DictUtils.get_required_str_dict_property(x, 'type') == 'list', schema))
        if len(list_rows) > 0:
            for row in list_rows:
                context_key = DictUtils.get_required_str_dict_property(row, 'name')
                context_value = DictUtils.get_dict_property(context, context_key)
                if isinstance(context_value, str):
                    if DictUtils.str_is_null_or_empty(context_value):
                        context[context_key] = []
                    else:
                        str_list = context_value.split(',')
                        str_list = list(filter(None, str_list))
                        context[context_key] = str_list
        return context
