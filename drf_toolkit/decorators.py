from power_dict.schema_validator import SchemaValidator
from six import wraps
from drf_toolkit.drf_utils import DrfUtils

def validate_request(schema):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, *args, **kwargs):
            request = view.request
            context = DrfUtils.get_request_parameters(request)
            context = SchemaValidator.validate(context, schema)
            kwargs['context'] = context
            return view_func(request, *args, **kwargs)

        return _wrapped_view

    return decorator


def except_error():
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(view, *args, **kwargs):
            try:
                return view_func(view, *args, **kwargs)
            except Exception as ex:
                return DrfUtils.generate_bad_response(exception=ex)

        return _wrapped_view

    return decorator
