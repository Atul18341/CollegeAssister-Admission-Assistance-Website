from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize=value.size

    if filesize>102400:
        raise ValidationError("Maximum File Size to be uploaded is 100Kb.")
    else:
        return value