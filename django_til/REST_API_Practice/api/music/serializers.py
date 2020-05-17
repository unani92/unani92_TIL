from rest_framework import serializers
from .models import Artist,Music,Comment

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['id','name']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = ['id','artist','title']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','content','music_id']

class ArtistDetailSerializer(ArtistSerializer):
    music_set = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ['music_set']

class MusicDetailSerializer(MusicSerializer):
    # 역참조 매서드랑 같아야 한다!!!!
    comments = CommentSerializer(source='comment_set',many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ['comments']