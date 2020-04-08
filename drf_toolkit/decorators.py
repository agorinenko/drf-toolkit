from functools import wraps

from power_dict.schema_validator import SchemaValidator
from power_dict.utils import DictUtils
from rest_framework.exceptions import APIException

from drf_toolkit.drf_utils import DrfUtils


def validate_request(schema):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, *args, **kwargs):
            if isinstance(schema, dict):
                target_schema = DictUtils.get_required_list_dict_property(schema, view_func.__name__)
            elif isinstance(schema, list):
                target_schema = schema
            else:
                raise Exception("Schema type must be dict or list")

            request = view.request
            context = DrfUtils.get_request_parameters(request)
            context = DrfUtils.transform_list_parameters(context, target_schema)

            context = SchemaValidator.validate(context, target_schema)
            kwargs['context'] = context
            return view_func(view, *args, **kwargs)

        return _wrapped_view

    return decorator


def except_error():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, *args, **kwargs):
            try:
                return view_func(view, *args, **kwargs)
            except APIException as ex:
                raise ex
            except Exception as ex:
                return DrfUtils.generate_bad_response(exception=ex)

        return _wrapped_view

    return decorator
