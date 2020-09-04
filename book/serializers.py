# noinspection PyUnresolvedReferences
from .models import Author,Book,Comment
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
        # author_book = BookSerializer(many=True)
    class Meta:
        model=Author
        fields=('id','name','created_date','published_by','books')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=('id','book','comment','up_votes')

class BookSerializer(serializers.ModelSerializer):
    boks = CommentSerializer(many=True)
    class Meta:
        model=Book
        fields=('id','title','description','author','boks')

    def create(self, validated_data):
        comment_data = validated_data.pop('boks')
        book = Book.objects.create(**validated_data)
        for comment_data in comment_data:
            Comment.objects.create(thing=Book, **comment_data)
        return book

    def update(self, instance, validated_data):
        comment_data = validated_data.pop('book')
        comments = (instance.book).all()
        comments = list(comments)
        instance.title= validated_data.get('title', instance.title)
        instance.desription = validated_data.get('desription', instance.desription)
        instance.author = validated_data.get('author ', instance.author )
        instance.save()

        for comm_data in comment_data:
            comment = comments.pop(0)
            comment.User = comm_data.get('User', comment.User)
            comment.book = comm_data.get('book', comment.book)
            comment.comment= comm_data.get('comment', comment.comment)
            comment.up_votes=comm_data.get('up_votes',comment.up_votes)
            comment.save()
        return instance