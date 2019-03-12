from django.urls import path

from . import views

urlpatterns = [
    path('', views.GiftCardListView.as_view(), name='giftcard-list'),
    path('archive/<int:gf_id>/<str:username>', views.archive, name='archive'),
    path('active/<int:gf_id>/<str:username>', views.active, name='active'),
]
