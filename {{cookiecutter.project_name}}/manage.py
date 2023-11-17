#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# read a local extension of the virtualenv path
# good to develop other libraries
if os.path.exists('.project.pth'):
    with open('.project.pth') as f:
        for path in f:
            if not path.startswith('#'):
                sys.path.insert(0, path.strip())


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_dir}}.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
