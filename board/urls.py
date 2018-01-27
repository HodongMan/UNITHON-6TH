from django.urls import path

from .views import BoardList, BoardDetail, BoardAnalizeByBoardId
from .views import BoardCollocationsByBoardId, BoardCollocationsExtractByBoardId
from .views import BoardAnalizeByBoardIdPretty, BoardCollocationsByBoardIdPretty

urlpatterns = [
    path("board/", BoardList.as_view(), name=BoardList.name),
    path("board/<int:pk>/", BoardDetail.as_view(), name=BoardDetail.name),
    path("board/analyze/<int:pk>/pretty/", BoardAnalizeByBoardIdPretty.as_view(), name=BoardAnalizeByBoardIdPretty   .name),
    path("board/analyze/<int:pk>/", BoardAnalizeByBoardId.as_view(), name=BoardAnalizeByBoardId.name),
    path("board/collocation/<int:pk>/pretty/", BoardCollocationsByBoardIdPretty.as_view(), name=BoardCollocationsByBoardIdPretty.name),
    path("board/collocation/<int:pk>/", BoardCollocationsByBoardId.as_view(), name=BoardCollocationsByBoardId.name),
    path("board/collocation/extract/<int:pk>/", BoardCollocationsExtractByBoardId.as_view(), name=BoardCollocationsExtractByBoardId.name),
]