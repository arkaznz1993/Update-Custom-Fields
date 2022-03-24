from custom_field_option import CustomFieldOption

CUSTOM_FIELD_TYPE_DROPDOWN = 'Dropdown'
CUSTOM_FIELD_TYPE_VALUE = 'Value'


class CustomField:
    custom_fields = []

    def __init__(self, id, id_board, name, type):
        self.id = id
        self.id_board = id_board
        self.name = name
        self.type = type

        CustomField.custom_fields.append(self)

    def __repr__(self):
        return f"CustomField('{self.id}', '{self.id_board}', '{self.name}', '{self.type}')"

    def convert_to_list(self):
        return [self.id, self.id_board, self.name, self.type]

    @staticmethod
    def instantiate_from_json(custom_fields_json, board):
        for custom_field in custom_fields_json:
            try:
                options = custom_field['options']
                CustomField(custom_field['id'], board, custom_field['name'], CUSTOM_FIELD_TYPE_DROPDOWN)
                CustomFieldOption.instantiate_from_json(options)
            except:
                CustomField(custom_field['id'], board, custom_field['name'], CUSTOM_FIELD_TYPE_VALUE)

    @staticmethod
    def convert_all_to_list():
        values = []
        for custom_field in CustomField.custom_fields:
            values.append(custom_field.convert_to_list())
        return values


