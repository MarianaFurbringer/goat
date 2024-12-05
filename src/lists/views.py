from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ValidationError
from lists.models import List, Item
from lists.forms import ItemForm

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(data=request.POST)
        if form.is_valid():
            Item.objects.create(text=request.POST["text"], list=list_)
            return redirect(list_)
    else:
        form = ItemForm()
    return render(request, "list.html", {"list": list_, "form": form})


# View para a página inicial
def home_page(request):
    form = ItemForm()  # Cria uma instância do ItemForm
    return render(request, 'home.html', {'form': form})  # Passa o form para o contexto

# View para criar uma nova lista
def new_list(request):
    form = ItemForm(data=request.POST)  
    if form.is_valid():  
        list_ = List.objects.create()
        Item.objects.create(text=request.POST["text"], list=list_)
        return redirect(list_)
    else:
        return render(request, "home.html", {"form": form})  

