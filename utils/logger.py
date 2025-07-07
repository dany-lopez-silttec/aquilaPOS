import os
from . import config
import logging
import logging.handlers

log_handler = None

def create_logger(name:str, log_level=logging.INFO) -> logging.Logger:
    global log_handler
    """
    Create a logger instance with a rotating file handler.
    The log file will be stored in the directory specified in the config.
    """  
    #Set logger with required log level as base 
    #print(f"Creando logger: {name} con nivel: {log_level}")
    loggerInstance = logging.getLogger(name)
    loggerInstance.setLevel(log_level)

    if not log_handler:        
        #Specify the required format                                               
        formatter = logging.Formatter('%(asctime)s %(filename)s %(funcName)s %(lineno)d %(levelname)s %(message)s')
        
        # Configure the handler with filePath,maxBytes and backupCount
        # maxBytes - theMaxSizeOfLogFileInBytes
        # backupCount - numberOFBackUpFiles to be created ex: logFile1,logFile2 etc (after log rotation)        
        log_file = os.path.join(config.get_directorio(), 'logs', config.get_parameter('log_name', 'aquilaPOS.log', 'logging'))
        log_handler = logging.handlers.RotatingFileHandler(log_file,
                                                    maxBytes=int(config.get_parameter('log_size', "10485760", 'logging')),  # Default 10 MB
                                                    backupCount=int(config.get_parameter('log_backup_count', "5", 'logging')))
        #Add formatter to handler
        log_handler.setFormatter(formatter)
      
        
    #Initialize logger instance with handler
    loggerInstance.addHandler(log_handler)
    loggerInstance.addHandler(logging.StreamHandler()) #Para q imprima en consola
    
    return loggerInstance
