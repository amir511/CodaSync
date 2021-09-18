from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    help = "Automatically create admin user"

    def handle(self, *args, **kwargs):
        admin_user, created = User.objects.get_or_create(username="admin")
        if created:
            admin_user.set_password("changeme")
            admin_user.is_superuser = True
            admin_user.is_staff = True
            admin_user.save()
