from django.urls import path,include
#noinspection PyUnresolvedReferences
from .serializers import BookSerializer,AuthorSerializer,CommentSerializer
from .views import Bookgenericview,AuthorgenericView,AuthorAPIView,CommentAPIView

urlpatterns=[
    path('book/',Bookgenericview.as_view()),
path('generic/book/<int:id>/',Bookgenericview.as_view()),
    path('author/',AuthorgenericView.as_view()),
    #path('book/list/',BookList.as_view()),
    path('author/list/',AuthorAPIView.as_view()),
    path('comment/',CommentAPIView.as_view()),
    path('api/', include('rest_framework.urls')),
]