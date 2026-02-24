from urllib.parse import urlparse, parse_qs
import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

_YT_ID_RE = re.compile(r"^[A-Za-z0-9_-]{6,20}$")


def _clean_youtube_id(value: str | None) -> str | None:
    if not value:
        return None
    value = value.strip()
    if _YT_ID_RE.match(value):
        return value
    return None


def _youtube_id(url: str) -> str | None:
    try:
        u = urlparse(url)
        host = (u.netloc or "").lower()
        path = u.path or ""

        # youtu.be/<id>
        if "youtu.be" in host:
            return _clean_youtube_id(path.strip("/").split("/")[0] or None)

        # youtube.com / youtube-nocookie.com
        if "youtube.com" in host or "youtube-nocookie.com" in host:
            if path.startswith("/embed/"):
                return _clean_youtube_id(path.split("/embed/")[1].split("/")[0] or None)
            if path.startswith("/shorts/"):
                return _clean_youtube_id(path.split("/shorts/")[1].split("/")[0] or None)
            if path.startswith("/live/"):
                return _clean_youtube_id(path.split("/live/")[1].split("/")[0] or None)

            qs = parse_qs(u.query)
            return _clean_youtube_id((qs.get("v", [None])[0]) or None)
    except Exception:
        return None
    return None


@register.filter
def youtube_id(url: str) -> str:
    return _youtube_id(url or "") or ""


@register.filter
def youtube_iframe(url: str) -> str:
    vid = _youtube_id(url or "")
    if not vid:
        return ""
    return mark_safe(
        '<div class="video-embed" style="position:relative;padding-top:56.25%;">'
        f'<iframe src="https://www.youtube-nocookie.com/embed/{vid}" '
        'style="position:absolute;top:0;left:0;width:100%;height:100%;" '
        'frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" '
        'allowfullscreen></iframe>'
        '</div>'
    )
