def evaluate(result):
    if result is None:
        return "error"
    
    output = ""
    exit_code = 0

    if isinstance(result, dict):
        exit_code = result.get("exit_code", 0)
        output = result.get("output", "").lower()
    
    # Lista de errores comunes que indican que algo salió mal aunque el shell no lo marque
    error_keywords = [
        "traceback (most recent call last):",
        "syntaxerror:",
        "modulemetanotfounderror:",
        "access is denied",
        "is not recognized as an internal or external command"
    ]

    if exit_code != 0:
        return "error"
    
    for kw in error_keywords:
        if kw in output:
            return "error"
        
    return "ok"
