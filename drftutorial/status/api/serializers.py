from rest_framework import serializers

from status.models import Status


class CustomSerializer(serializers.Serializer):
    content = serializers.CharField()
    email = serializers.EmailField()


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
        read_only_fields = ['user'] # GET

    # def validate_content(self, value):
    #      if len(value) > 10000:
    #         raise serializers.ValidationError("This a wayy too long.")
    #      return value

    def validate(self, data):
        content = data.get("content", None)
        if content == "":
            content = None
        image = data.get("image", None)
        if content is None and image is None:
            raise serializers.ValidationError("Content or image is required.")
        return data