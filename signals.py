from django.db.models import signals
from django.dispatch import receiver
from .models import reviews, hotels

# pre_save method signal
@receiver(signals.pre_save, sender=reviews)
def add_reviews_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())


@receiver(signals.pre_save, sender=hotels)
def add_hotels_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())