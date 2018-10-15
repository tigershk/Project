from rest_framework import serializers
from .models import Movie

# class MovieSerializer(serializers.ModelSerializer):
class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie

        fields = ('id','url','title','imdbid')
        # fields = ('id','title','imdbid')