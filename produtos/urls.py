from django.urls import path
from .views import ProdutoListView, ProdutoDetailView, ProdutoCreateView, ProdutoUpdateView, ProdutoDeleteView

urlpatterns = [
    path('', ProdutoListView.as_view(), name='lista_produtos'),
    path('<int:pk>/', ProdutoDetailView.as_view(), name='detalhe_produto'),
    path('novo/', ProdutoCreateView.as_view(), name='criar_produto'),
    path('<int:pk>/editar/', ProdutoUpdateView.as_view(), name='editar_produto'),
    path('<int:pk>/deletar/', ProdutoDeleteView.as_view(), name='deletar_produto'),
]
