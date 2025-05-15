import os

def is_debug():
    return os.environ.get("DJANGO_DEBUG", "True") == "True"
