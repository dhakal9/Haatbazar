import os
import sys
from django.core.management.commands.runserver import Command as runserver
from django.core.management import execute_from_command_line


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'haatbazar.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Configure Django settings
    import django.conf
    django.conf.settings.configure(
        DEBUG=True,
        ALLOWED_HOSTS=['*'],  # Update with your allowed hosts
        # Add other Django settings here
    )

    if __name__ == '__main__':
        runserver.default_addr = '0.0.0.0'
        runserver.default_port = '8000'
        runserver.default_ipv6 = False
        runserver.use_reloader = True
        execute_from_command_line(sys.argv)
