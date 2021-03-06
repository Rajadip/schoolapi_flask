from schoolapi.extension import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, server_default=db.func.now())
    date_modified = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

    def update(self, **kwargs):
        for key, value in kwargs.items():
            try:
                getattr(self, key)
                setattr(self, key, value)
            except AttributeError:
                pass

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(BaseModel):
    first_name = db.Column(db.VARCHAR(40))
    last_name = db.Column(db.VARCHAR(40))
    email = db.Column(db.VARCHAR(40), unique=True)
    password = db.Column(db.VARCHAR(90))
    phone = db.Column(db.VARCHAR(12))

    def __repr__(self):
        return "<%s>" % self.email
