import subprocess

def run(cmd):
    """
    Ejecuta un comando en el shell del sistema y captura su salida.

    Args:
        cmd (str): El comando de consola a ejecutar.

    Returns:
        dict: Un diccionario con 'exit_code' (int) y 'output' (str).
              Si hay un error de ejecución, el exit_code será -1.
    """
    print(f"💻 Running: {cmd}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        output = result.stdout if result.returncode == 0 else result.stderr
        return {
            "exit_code": result.returncode,
            "output": output.strip()
        }
    except Exception as e:
        return {
            "exit_code": -1,
            "output": str(e)
        }
