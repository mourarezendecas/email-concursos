import subprocess
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

python_venv = os.path.join(current_dir, '.venv', 'Scripts', 'python.exe')

subprocess.run([python_venv, 'sisconcurso_scraper.py'])