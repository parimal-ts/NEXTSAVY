from typing import Any, Iterable, Optional
from django.db import models
import os
from datetime import datetime
from django.core.exceptions import ValidationError
import mimetypes

# Create your models here.

# The `FileManager` class defines a model for storing files with a maximum size limit of 50 MiB.
class FileManager(models.Model):

    def file_size_limit(value):
        """
        This function checks if a file's size exceeds a limit of 50 MiB and raises a validation error if
        it does.
        
        :param value: The value parameter is an object that represents a file that is being uploaded or
        processed. It typically contains information about the file, such as its size, content type, and
        name
        """
        limit = 50 * 1024 * 1024
        if value.size > limit:
            raise ValidationError('File size too large. Size should not exceed 50 MiB.')

    file_name = models.CharField(max_length=1000)
    file = models.FileField(upload_to='files/', validators=[file_size_limit])
    file_type = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True)
    file_size = models.CharField(max_length=1000)

    def save(self, *args, **kwargs):
        """
        The function calculates and saves the file type, name, and size of a file being uploaded.
        """
        self.file_type =  mimetypes.guess_type(self.file.name)[0]
        self.file_name = self.file.name
        x = self.file.size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        self.file_size = str(value)+ext
        super(FileManager, self).save(*args, **kwargs)
