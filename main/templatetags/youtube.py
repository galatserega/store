from urllib.parse import urlparse, parse_qs
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


def _youtube_id(url: str) -> str | None:
    try:
        u = urlparse(url)
        host = (u.netloc or "").lower()

        if "youtu.be" in host:
            return u.path.strip("/").split("/")[0] or None

        if "youtube.com" in host or "youtube-nocookie.com" in host:
            if u.path.startswith("/embed/"):
                return u.path.split("/embed/")[1].split("/")[0] or None
            qs = parse_qs(u.query)
            return (qs.get("v", [None])[0]) or None
    except Exception:
        return None
    return None


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
