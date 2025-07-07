# This Python file uses the following encoding: utf-8
import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication

from utils import config, logger
from widgets.v_login import VLogin
from widgets.v_principal import VPrincipal

import os
from peewee import *
from orm.tablas import Product, create_tables
    
config.set_directorio(os.path.dirname(os.path.abspath(__file__)))
    
_logger = logger.create_logger(__name__)


if __name__ == "__main__":
    _logger.info(f"PySide version: {PySide6.__version__} / Qt version: {PySide6.QtCore.__version__}")

    app = QApplication(sys.argv)    
    
    _logger.info(f"Directorio: {config.get_directorio()}")
    
    #initialize_db()
    create_tables()
        
    ps = Product.select()
    if len(ps) == 0:
        _logger.info("No hay productos en la base de datos.")
        Product.create(
            code="001",
            name="Producto de prueba",
            description="Descripción del producto de prueba",
            tags="prueba, ejemplo",
            category="General",
            price=10.99,
            stock=100,
            image=None
        )
    for p in ps:
        _logger.info(f"Producto: {p.name} - Precio: {p.price} - Stock: {p.stock}")
        
    vlogin = VLogin()
    if vlogin.exec() == VLogin.Accepted:
        _logger.info("Login successful")
        # Show the main window after successful login
        vprincipal = VPrincipal()
        vprincipal.show()
    else:
        _logger.info("Login cancelled or failed")
        sys.exit(0)    
    
    sys.exit(app.exec())
