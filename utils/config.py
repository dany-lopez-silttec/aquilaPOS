import configparser
import os

directorio = ""
config = None
config_file = ''

def set_directorio(path):
    global directorio
    directorio = path
    print(f"Directorio configurado: {directorio}")
    return directorio
    
def get_directorio():
    global directorio
    return directorio

def load_config():
    global directorio, config, config_file
    
    if not directorio:
        set_directorio(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    print("Cargando configuración...", directorio)
    
    config = configparser.ConfigParser()
    config_file = os.path.join(directorio, 'config.ini')
    config.read(config_file)
    return True
    
def get_parameter(parameter, default_value, section='global'):
    global config, config_file
    if config is None:
        load_config()
    if section in config and parameter in config[section]:
        return config[section][parameter]
    else:
        if section not in config:
            config.add_section(section)
        config[section][parameter] = default_value
        save_config()
        return default_value

def set_parameter(parameter, value, section='global'):
    global config, config_file
    if config is None:
        load_config()
    if section not in config:
        config.add_section(section)
    config[section][parameter] = value
    save_config()
    return value
        
def save_config():
    global config, config_file
    if config is None:
        load_config()
    with open(config_file, 'w') as configfile:
        config.write(configfile)
    return True