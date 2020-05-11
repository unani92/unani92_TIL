## 0511 workshop

### 결과 사진

#### GET : `api/v1/artists/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010233317.png" alt="image-20200512010233317" style="zoom: 80%;" />

#### GET `api/v1/artists/<artist_pk>/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010400402.png" alt="image-20200512010400402" style="zoom:80%;" />

#### GET `api/v1/musics/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010503645.png" alt="image-20200512010503645" style="zoom:67%;" />

#### GET `api/v1/musics/<music_pk>/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010609619.png" alt="image-20200512010609619" style="zoom:80%;" />

#### POST `api/v1/musics/<music_pk>/comments/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010726405.png" alt="image-20200512010726405" style="zoom:80%;" />

#### PUT & DELETE `api/v1/comments/<comment_pk>/`

<img src="../../AppData/Roaming/Typora/typora-user-images/image-20200512010854986.png" alt="image-20200512010854986" style="zoom:80%;" />



### 소스코드

#### `views.py`

```python
from django.shortcuts import render,get_object_or_404
from .models import Music,Artist
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def Artists(request):
    artists = Artist.objects.all()
    serializer = ArtistSerializer(artists,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ArtistsDetail(request,artist_pk):
    artist = get_object_or_404(Artist,pk=artist_pk)
    serializer = ArtistSerializer(artist)
    return Response(
        {
            'data':serializer.data,
            'music_count':artist.musics_count()
        }
    )

@api_view(['GET'])
def Musics(request):
    musics = Music.objects.all()
    serializer = MusicSerializer(musics,many=True)
    return Response(
        {
            "data": serializer.data,
        }
    )

@api_view(['GET'])
def MusicDetail(requset,music_pk):
    music = get_object_or_404(Music,pk=music_pk)
    serializer = MusicDetailSerializer(music)
    return Response(serializer.data)

@api_view(['GET','POST'])
def comment_create(request,music_pk):
    if request.method == "POST":
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 1:N 연결 시 id를 이용해 연결한다.
            serializer.save(music_id=music_pk)
            return Response(serializer.data)
        else :
            return Response(
                {
                    "status" : "404 error"
                }
            )
    else :
        music = get_object_or_404(Music, pk=music_pk)
        serializer = MusicDetailSerializer(music)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def comment_edit(request,comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == "PUT":
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(
                {
                    "msg" : "성공적으로 수정되었습니다.",
                    "data" : serializer.data
                }
            )
    elif request.method == 'DELETE' :
        comment.delete()
        return Response({'msg': '성공적으로 삭제되었습니다.'})

    else :      # request : GET
        comment = get_object_or_404(Comment, pk=comment_pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

```



#### `serializers.py`

```python
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
        fields = ['id','content']

class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(many=True)
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ['musics']

class MusicDetailSerializer(MusicSerializer):
    # 역참조 매서드랑 같아야 한다!!!!
    comment_set = CommentSerializer(many=True)
    class Meta(MusicSerializer.Meta):
        fields = MusicSerializer.Meta.fields + ['comment_set']
```

