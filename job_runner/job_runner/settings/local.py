from unipath import Path

from .base import *


BASE_DIR = Path(__file__).absolute().ancestor(3)

TEMPLATE_DIRS = (
    BASE_DIR.child("templates"),
)
