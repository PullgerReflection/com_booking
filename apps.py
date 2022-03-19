from django.apps import AppConfig


class djPullgerReflection_com_bookingConfig(AppConfig):
    name = 'djPullgerReflection.com_booking'

    def ready(self):
        import djPullgerReflection.com_booking.signals  # noqa
