import json


class AbstractConfig:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_config_string(self):
        config_string = ""
        params = self.__dict__
        # remove 'column_names' from params
        column_names = params.pop("column_names", None)
        items = list(params.items())
        flatted_items = []
        for key, value in items:
            if isinstance(value, list):
                for item in value:
                    flatted_items.append((key, item))
            else:
                flatted_items.append((key, value))
        for key, value in flatted_items:
            if isinstance(value, AbstractConfig):
                value = value.to_config_string()
            elif isinstance(value, dict):
                value = json.dumps(value)
            config_string += f"# {key}: {value}\n"
        if column_names is not None:
            config_string += ", ".join(column_names) + "\n"
        return config_string
