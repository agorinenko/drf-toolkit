import unittest

from drf_toolkit.drf_utils import DrfUtils


class CommonTests(unittest.TestCase):
    def test_transform_list_parameters(self):
        schema = [
            {'name': 'type_of_message', 'type': 'list',
             'items': {'type': 'enum', 'choices': ['text_message', 'issue', 'solution', 'solution_without_request']},
             'required': False, 'unique': True, 'description': 'Тип сообщения'},
            {'name': 'limit', 'type': 'int', 'required': False, 'default_value': 20,
             'description': 'Количество извлекаемых элементов'},
            {'name': 'offset', 'type': 'int', 'required': False, 'default_value': 0,
             'description': 'Начальная позиция для извлечения элементов'}]

        context = {'type_of_message': 'solution,solution_without_request'}

        context = DrfUtils.transform_list_parameters(context, schema)
        self.assertIsInstance(context['type_of_message'], list)
        self.assertEqual(context['type_of_message'].sort(), ['solution', 'solution_without_request'].sort())

    def test_transform_list_parameters_2(self):
        schema = [
            {'name': 'limit', 'type': 'int', 'required': False, 'default_value': 20,
             'description': 'Количество извлекаемых элементов'},
            {'name': 'offset', 'type': 'int', 'required': False, 'default_value': 0,
             'description': 'Начальная позиция для извлечения элементов'}]

        context = {'limit': 1, 'offset': 0}
        context_2 = DrfUtils.transform_list_parameters(context, schema)
        self.assertEqual(context, context_2)
