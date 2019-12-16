from rest_framework.exceptions import ParseError

from rest_framework.parsers import JSONParser


class JsonParser(JSONParser):
    def parse(self, stream, media_type=None, parser_context=None):
        try:
            return super().parse(stream, media_type, parser_context)
        except ParseError:
            raise ParseError('Ошибка обработки тела запроса')
