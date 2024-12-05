from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from lists.models import List, Item
from lists.forms import ItemForm

# View para exibir a lista
def view_list(request, id):
    # Garante que a lista existe ou retorna 404 caso contrário
    list_ = get_object_or_404(List, id=id)
    error = None

    if request.method == "POST":
        item_text = request.POST.get("item_text", "").strip()  # Evita erros de chave ausente

        if not item_text:
            error = "You can't have an empty list item"  # Se o texto do item estiver vazio
        else:
            try:
                item = Item(text=item_text, list=list_)  # Cria o item com texto
                item.full_clean()  # Realiza a validação
                item.save()  # Salva o item se estiver válido
                return redirect(list_)  # Redireciona para a lista após salvar o item
            except ValidationError:
                list_.delete()
                error = "You can't have an empty list item"
                return render(request, "home.html", {"error": error})

    # Retorna a renderização com o list_ e o erro (se houver)
    return render(request, "list.html", {"list": list_, "error": error})

# View para a página inicial
def home_page(request):
    form = ItemForm()  # Cria uma instância do ItemForm
    return render(request, 'home.html', {'form': form})  # Passa o form para o contexto

# View para criar uma nova lista
def new_list(request):
    if request.method == 'POST':
        item_text = request.POST.get('item_text', '').strip()
        if item_text:
            list_ = List.objects.create()  # Cria uma nova lista
            item = Item.objects.create(text=item_text, list=list_)  # Cria o primeiro item
            return redirect(list_)  # Redireciona para a lista criada
        else:
            return render(request, 'home.html', {'error': "You can't have an empty list item"})
    
    return render(request, 'home.html')
