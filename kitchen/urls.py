from django.urls import path
from .views import (
    IndexView,
    DishTypeListView,
    DishListView,
    CookListView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    DishDetailView,
    ToggleAssignToDishView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path(
        "dish-types/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/<int:pk>/toggle-assign/",
        ToggleAssignToDishView.as_view(),
        name="toggle-dish-assign"
    ),
]

app_name = "kitchen"
