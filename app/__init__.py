# from flask import Flask

# # Initializing application
# app = Flask(__name__)

# from app import views

# from flask import Flask
# from .config import DevConfig

# # Initializing application
# app = Flask(__name__)

# # Setting up configuration
# app.config.from_object(DevConfig)

# from app import views

from flask import Flask
from .config import DevConfig

# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

from app import views

...
from flask_bootstrap import Bootstrap
...

...
# Initializing application
app = Flask(__name__,instance_relative_config = True)

# Setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile("config.py")

# Initializing Flask Extensions
bootstrap = Bootstrap(app)
...

