from django.urls import path

from liberty.views import AuthorView, CreateView, DetailsView, ExploreView, UserLoginview, UserRegisterView, filter_items, home_page, item_updateView

app_name = "liberty"

urlpatterns = [
    path('', home_page, name="home"),
    path('explore/', ExploreView.as_view(), name="explore"),
    path('details/<int:pk>', DetailsView.as_view(), name="details"),
    path('author/', AuthorView.as_view(), name="author"),
    path('create/', CreateView.as_view(), name='create' ),    
    path('login/', UserLoginview.as_view(), name = 'login' ),    
    path('register/', UserRegisterView.as_view(), name = 'register'),
    path('update/<int:pk>', item_updateView, name = 'update'),
      path('filter/', filter_items, name='filter_products'),
]
