from rest_framework import serializers

from .models import Movies


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"
        read_only_fields = (
            "id",
            "created_date",
            "updated_date",
        )
