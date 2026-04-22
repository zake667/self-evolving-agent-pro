import logging
import os

LOG_FILE = "docs/agent_activity.log"

def setup_logger():
    """
    Configura el sistema de logging para registrar la actividad en un archivo.
    
    Returns:
        logging.Logger: Instancia del logger configurado.
    """
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='a'
    )
    return logging.getLogger("agent")

logger = setup_logger()

def log_info(message):
    """Registra un mensaje informativo en consola y en el archivo de logs."""
    print(f"ℹ {message}")
    logger.info(message)

def log_error(message):
    """Registra un mensaje de error en consola y en el archivo de logs."""
    print(f"❌ {message}")
    logger.error(message)

def log_command(cmd, result):
    """
    Registra la ejecución de un comando shell y su resultado.

    Args:
        cmd (str): El comando ejecutado.
        result (dict): El resultado devuelto por tools.shell.run.
    """
    status = "SUCCESS" if result['exit_code'] == 0 else "FAILED"
    msg = f"Command: {cmd} | Status: {status} | Output: {result['output'][:100]}..."
    logger.info(msg)
