from peewee import *
from . import database
from utils import config, logger

_logger = logger.create_logger(__name__)


def create_tables():
    """Create all tables in the database."""
    db = database.get_db()
    try:
        db.connect()
        _logger.info("Creating tables if they do not exist...")
        db.create_tables([ 
            Product,
        ], safe=True)  # safe=True prevents errors if tables already exist
        _logger.info("Tables created successfully.")
    except Exception as e:
        _logger.error(f"Failed to create tables: {e}")
    finally:
        db.close()  # Close the connection after creating tables
        
        
        
class Product(Model):
    code = CharField(unique=True, max_length=50)
    name = CharField()
    description = TextField(null=True)
    tags = CharField(null=True)  # Comma-separated tags
    category = CharField(null=True)  # Category name
    price = DecimalField(max_digits=10, decimal_places=4)
    stock = IntegerField()
    image = CharField(null=True) #Path from image file

    class Meta:
        database = database.get_db() 