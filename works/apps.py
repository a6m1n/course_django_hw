from django.apps import AppConfig


class WorksConfig(AppConfig):
    name = 'works'

    def ready(self):
        from django.db.models.signals import post_save
        from works.signals import signal_to_chanells
        from .models import Companies, Work, Worker, WorkPlace, Manager

        post_save.connect(signal_to_chanells, sender=Companies)
        post_save.connect(signal_to_chanells, sender=Work)
        post_save.connect(signal_to_chanells, sender=Worker)
        post_save.connect(signal_to_chanells, sender=WorkPlace)
        post_save.connect(signal_to_chanells, sender=Manager)
