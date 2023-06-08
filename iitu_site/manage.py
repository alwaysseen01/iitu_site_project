#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
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


    def print_directory_tree(path, indent=''):
        print(indent + os.path.basename(path))
        if os.path.isdir(path):
            for filename in os.listdir(path):
                print_directory_tree(os.path.join(path, filename), indent + '  ')


    print_directory_tree('D:\Python works\iitu_site_project')
