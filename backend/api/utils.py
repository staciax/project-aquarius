from datetime import datetime

from django.utils import timezone


def get_media_filename(
    filename: str,
    *,
    prefix: str | None = None,
    with_timestamp: bool = True,
) -> str:
    filename = filename.lower().replace(' ', '_').replace('-', '_')

    if prefix:
        filename = f'{prefix}_{filename}'

    if with_timestamp:
        tz_now = datetime.now(timezone.get_default_timezone())
        timestamp = tz_now.strftime('%Y%m%d%H%M%S')
        filename = f'{timestamp}_{filename}'

    return filename.lower().replace(' ', '_').replace('-', '_')
