from django.core.exceptions import ValidationError


def validate_file_type(file):
    valid_types = ['image/jpeg', 'image/png', 'video/mp4']
    if file.content_type not in valid_types:
        raise ValidationError('Only images and videos are allowed.')


def validate_file_size(file):
    max_size = 10 * 1024 * 1024 if 'image' in file.content_type else 50 * 1024 * 1024
    if file.size > max_size:
        raise ValidationError('File size exceeds the allowed limit.')
