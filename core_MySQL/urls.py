from django.urls import path
from .views import index, contato, produto
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/', produto, name='produto'),
]

favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path(r'^favicon\.ico$', favicon_view),

]
