import os
import requests
from dotenv import load_dotenv
from tools.shell import run

load_dotenv()

def create_github_repo():
    """
    Crea un repositorio en GitHub y sube el código local mediante Git.
    Requiere que GITHUB_TOKEN, GITHUB_REPO y GITHUB_USERNAME estén en el .env.

    Returns:
        dict: Resultado de la operación con exit_code y output descriptivo.
    """
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPO")
    username = os.getenv("GITHUB_USERNAME")

    if not all([token, repo_name, username]):
        return {"exit_code": 1, "output": "Faltan credenciales de GitHub en el .env"}

    url = "https://api.github.com/user/repos"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {
        "name": repo_name,
        "private": False
    }

    print(f"📡 Creando repositorio {repo_name} en GitHub...")
    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 201:
        print("✅ Repositorio creado con éxito.")
    elif response.status_code == 422:
        print("ℹ El repositorio ya existe.")
    else:
        return {"exit_code": 1, "output": f"Error al crear repo: {response.text}"}

    remote_url = f"https://{token}@github.com/{username}/{repo_name}.git"
    
    steps = [
        "git init",
        "git add .",
        'git commit -m "🚀 Initial commit from Self-Evolving Agent"',
        "git branch -M main",
        f"git remote remove origin",
        f"git remote add origin {remote_url}",
        "git push -u origin main"
    ]

    for step in steps:
        res = run(step)
        if res['exit_code'] != 0 and "remote remove" not in step:
            return res

    return {"exit_code": 0, "output": "Proyecto subido a GitHub correctamente."}
