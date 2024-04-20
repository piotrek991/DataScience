"""pd_ds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from books.views import BookDetailView, BookView, AddBook, EventShow
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book-detail"),
    path("books/", BookView.as_view(), name="book-list"),
    path("books/add_book/", AddBook.as_view(), name="book-add"),
    path("books/events/", EventShow.as_view(), name="events")
]

