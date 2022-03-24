class CustomFieldOption:
    custom_field_options = []

    def __init__(self, id, id_custom_field, custom_field_value):
        self.id = id
        self.id_custom_field = id_custom_field
        self.custom_field_value = custom_field_value

        CustomFieldOption.custom_field_options.append(self)

    def __repr__(self):
        return f"CustomFieldOption('{self.id}', '{self.id_custom_field}', '{self.custom_field_value}')"

    def convert_to_list(self):
        return [self.id, self.id_custom_field, self.custom_field_value]

    @staticmethod
    def instantiate_from_json(custom_field_options_json):
        for option_json in custom_field_options_json:
            CustomFieldOption(
                option_json['id'],
                option_json['idCustomField'],
                option_json['value']['text'],
            )

    @staticmethod
    def convert_all_to_list():
        values = []
        for custom_field_option in CustomFieldOption.custom_field_options:
            values.append(custom_field_option.convert_to_list())
        return values
