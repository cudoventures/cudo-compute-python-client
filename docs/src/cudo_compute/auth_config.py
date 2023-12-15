from ruamel.yaml import YAML
import os

home = os.path.expanduser("~")


def load_config(path, context_name):
    key_config = None
    context_config = None
    error = None

    with open(path, 'r') as file:
        yaml = YAML(typ='safe')
        config_data = yaml.load(file)

    if config_data['configVersion'] != "v0":
        error = Exception("Only config version v0 is supported")
        return key_config, context_config, error

    if not context_name:
        if 'current-context' in config_data:
            context_name = config_data['current-context']
        else:
            return key_config, context_config, Exception("No current context selected")

    if 'contexts' in config_data:
        for context_data in config_data['contexts']:
            if context_data['name'] == context_name:
                context_config = context_data
                break

    if not context_config:
        error = Exception("Context not found")
        return key_config, context_config, error

    if 'keys' in config_data:
        for key_data in config_data['keys']:
            if key_data['name'] == context_config['key']:
                key_config = key_data

    if not key_config:
        error = Exception("Key not found")

    return key_config, context_config, error



