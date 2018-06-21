from rest_framework import serializers

from file_app.models import File

class FileSerializer(serializers.ModelSerializer):
  class Meta():
    model = File
    fields = ['id', 'file', 'remark', 'timestamp']
