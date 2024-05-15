import logging

# Configuración automática del logger
def _configure_logger():
    """
    Configura automáticamente el logger para mostrar en la consola.
    """
    logger = logging.getLogger('__main__')
    logger.setLevel(logging.DEBUG)
    
    # Formateador
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # Manejador de consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)
    
    # Añadir el manejador al logger si no está ya añadido
    if not logger.hasHandlers():
        logger.addHandler(console_handler)
    
    return logger

# Configurar el logger al importar el módulo
logger = _configure_logger()

