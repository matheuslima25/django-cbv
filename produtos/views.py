from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Produto
from django.urls import reverse_lazy

class ProdutoListView(ListView):
    model = Produto
    template_name = 'produtos/produto_list.html'
    context_object_name = 'produtos'
    paginate_by = 5

    def get_queryset(self):
        queryset = Produto.objects.all()
        busca = self.request.GET.get('busca')
        ordenar = self.request.GET.get('ordenar_por')

        if busca:
            queryset = queryset.filter(nome__icontains=busca)
        
        if ordenar:
            queryset = queryset.order_by(ordenar)
        
        return queryset

class ProdutoDetailView(DetailView):
    model = Produto
    template_name = 'produtos/produto_detail.html'
    context_object_name = 'produto'

class ProdutoCreateView(CreateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('lista_produtos')

class ProdutoUpdateView(UpdateView):
    model = Produto
    fields = ['nome', 'descricao', 'preco']
    template_name = 'produtos/produto_form.html'
    success_url = reverse_lazy('lista_produtos')

class ProdutoDeleteView(DeleteView):
    model = Produto
    template_name = 'produtos/produto_confirm_delete.html'
    success_url = reverse_lazy('lista_produtos')
