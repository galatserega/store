import base64
from django.contrib.staticfiles import finders
import functools


@functools.lru_cache(maxsize=8)
def get_static_base64(static_path: str) -> str | None:
    """
    Повертає base64-рядок для static-файлу (наприклад 'img/logo.png').
    Працює і в DEV, і після collectstatic.
    """
    abs_path = finders.find(static_path)  # шукає у всіх STATICFILES_DIRS та зібраних файлах
    if not abs_path:
        return None
    with open(abs_path, "rb") as f:
        return base64.b64encode(f.read()).decode("ascii")