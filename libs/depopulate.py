from django.apps import apps
from django.db import transaction
from django.contrib.auth import get_user_model


@transaction.atomic()
def depopulate():
    User = get_user_model()
    User.objects.all().delete()

    app_names = ['product']
    for app in app_names:
        app_models = apps.get_app_config(app).get_models()

        for model in app_models:
            model.objects.all().delete()
