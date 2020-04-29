from django.shortcuts import render, redirect
# from django.views.generic import DetailView
from .models import Item
from .forms import PostItemForm
# from app.helpers import grouped
# Create your views here.


def home(request):

    items = Item.objects.all()
    # context['items'] = grouped(Item.objects.all(), 4)
    # return render(request, 'itemsapp/grid.html', context)
    return render(request, 'itemsapp/grid.html', {'items': items})
    # return render(request, 'home.html', {'items': items})


def details(request, item_id):
    particular_item = Item.objects.get(id=item_id)
    return render(request, 'itemsapp/item_detail.html', {'particular_item': particular_item})


def post_item(request):
    form = PostItemForm(request.POST)
    if form.is_valid():
        item = Item(
            name=form.cleaned_data['name'],
            type=form.cleaned_data['type'],
            value=form.cleaned_data['value'],
            image=form.cleaned_data['image']
        )
        item.save()
        return redirect('items_home')
    else:
        return render(request, 'itemsapp/post_item.html', {'form': form})
