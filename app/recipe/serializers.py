from rest_framework import serializers

from core.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        # id will be read-only
        read_only_fields = ('id', )
