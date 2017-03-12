from django.apps import apps
from django.conf import settings

class DBRouter(object):

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth models go to auth_db.
        """
        database = getattr(model, "_db", None)
        return database if database in settings.DATABASES.keys() else None
    def db_for_write(self, model, **hints):
        """
        Attempts to write auth models go to auth_db.
        """
        database = getattr(model, "_db", None)
        return database if database in settings.DATABASES.keys() else None
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations
        """
        return True
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Allow migrations
        """
        database = db
        if model_name:
            model = apps.get_model(app_label=app_label,model_name=model_name)
            if model:
                database = getattr(model, "_db", db)
        return database == db
