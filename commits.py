import os
import random
from datetime import datetime, timedelta
from git import Repo

# Configuración
REPO_PATH = '.'  # Ruta a tu repositorio local
GITHUB_USERNAME = 'tu_usuario_github'
GITHUB_REPO = 'tu_repositorio'
BRANCH = 'main'  # o 'master' dependiendo de tu repositorio

def create_commits():
    # Inicializar el repositorio
    repo = Repo(REPO_PATH)
    
    # Fechas de inicio y fin
    start_date = datetime(2025, 4, 15)
    end_date = datetime(2025, 5, 1)
    
    current_date = start_date
    
    while current_date <= end_date:
        # Crear un archivo con la fecha actual
        filename = f"commits_{current_date.strftime('%Y-%m-%d')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Commit automático para {current_date.strftime('%Y-%m-%d')}\n")
            f.write(f"Contenido aleatorio: {random.randint(1, 10000)}\n")
        
        # Añadir el archivo al staging area
        repo.index.add([filename])
        
        # Configurar la fecha del commit
        os.environ['GIT_AUTHOR_DATE'] = current_date.strftime('%Y-%m-%d %H:%M:%S')
        os.environ['GIT_COMMITTER_DATE'] = current_date.strftime('%Y-%m-%d %H:%M:%S')
        
        # Hacer el commit
        repo.index.commit(f"Commit automático {current_date.strftime('%Y-%m-%d')}")
        
        print(f"Commit creado para {current_date.strftime('%Y-%m-%d')}")
        
        # Avanzar al siguiente día
        current_date += timedelta(days=1)
    
    # Empujar los cambios a GitHub
    origin = repo.remote(name='origin')
    origin.push()
    print("Todos los commits han sido empujados a GitHub")

if __name__ == "__main__":
    create_commits()