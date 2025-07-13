from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils import timezone


def parse_datetime(datetime_string, format_string="%Y-%m-%dT%H:%M:%S"):
    """
    Parse a datetime string and return a timezone-aware datetime object for Django.

    Args:
        datetime_string (str): The datetime string to parse
        format_string (str): The format pattern (default: "%Y-%m-%d %H:%M:%S")

    Returns:
        datetime: Timezone-aware datetime object

    Raises:
        ValidationError: If the datetime string cannot be parsed
    """
    try:
        # Parse the datetime string
        parsed_datetime = datetime.strptime(datetime_string, format_string)

        # Make it timezone-aware (Django requirement)
        if timezone.is_naive(parsed_datetime):
            parsed_datetime = timezone.make_aware(parsed_datetime)

        return parsed_datetime

    except ValueError as e:
        raise ValidationError(f"Invalid datetime format. Expected format: {format_string}")
