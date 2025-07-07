from peewee import *
import os
from utils import config, logger
#from .product import Product

db = None
_logger = logger.create_logger(__name__)

def get_db():
    global db
    
    if db is not None:
        return db
    
    db_tipo = config.get_parameter('db_type', 'sqlite', 'database')    
    _logger.info(f"Initializing database of type: {db_tipo}")
    
    if db_tipo == 'sqlite':
        db_file = os.path.join(config.get_directorio(), 'aquilaPOS.db')
        db = SqliteDatabase(db_file)
        
    elif db_tipo == 'postgresql':
        db = PostgresqlDatabase(
            database=config.get_parameter('db_name', 'aquilaPOS', 'database'),
            user=config.get_parameter('db_user', 'postgres', 'database'),
            password=config.get_parameter('db_password', 'password', 'database'),
            host=config.get_parameter('db_host', 'localhost', 'database'),
            port=int(config.get_parameter('db_port', '5432', 'database'))
        )   
    elif db_tipo == 'mysql':
        db = MySQLDatabase(
            config.get_parameter('db_name', 'aquilaPOS', 'database'),
            user=config.get_parameter('db_user', 'root', 'database'),
            password=config.get_parameter('db_password', '', 'database'),
            host=config.get_parameter('db_host', 'localhost', 'database'),
            port=int(config.get_parameter('db_port', '3306', 'database'))
        )
    else:
        raise ValueError(f"Unsupported database type: {db_tipo}")
    
    _logger.info(f"Connecting to database: {db.database}")
    try:
        db.connect()  # Connect to the database
        _logger.info("Database connection established successfully.")
    except Exception as e:
        _logger.error(f"Failed to connect to the database: {e}")
        raise
    finally:
        db.close()  # Close the connection immediately after checking        
    
    return db  

