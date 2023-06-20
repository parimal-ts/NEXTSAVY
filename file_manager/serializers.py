from rest_framework import serializers
from .models import FileManager
from django.conf import settings
import os
class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileManager
        fields =  ["file_type"]
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["file_url"] =   os.path.join(settings.DOWNLOAD_ORIGIN + instance.file.url)
        return data