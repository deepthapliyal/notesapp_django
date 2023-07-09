from django.shortcuts import render
from django.http import JsonResponse
from .models import Item

def get_items(request):
    items = Item.objects.all().values()
    return JsonResponse(list(items), safe=False)

def create_item(request):
    name = request.POST.get('name')
    description = request.POST.get('description')
    item = Item(name=name, description=description)
    item.save()
    return JsonResponse({'message': 'Item created successfully!'})

def update_item(request, item_id):
    name = request.POST.get('name')
    description = request.POST.get('description')
    item = Item.objects.get(id=item_id)
    item.name = name
    item.description = description
    item.save()
    return JsonResponse({'message': 'Item updated successfully!'})

def delete_item(request, item_id):
    item = Item.objects.get(id=item_id)
    item.delete()
    return JsonResponse({'message': 'Item deleted successfully!'})
