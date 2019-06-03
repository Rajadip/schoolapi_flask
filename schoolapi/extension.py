
## sqlalchemy
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

## migration
from flask_migrate import Migrate
migrate = Migrate(db=db)
