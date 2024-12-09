from flask import Flask

from .config import Config

# Inicializações
app = Flask(__name__)
app.config.from_object(Config())

# Importar modelos e rotas
from .models import *
from .routes import *
from .modules import *
