# CRUD App Tutorial

This tutorial will guide you through the process of creating a simple CRUD (Create, Read, Update, Delete) app using Django for the backend and plain HTML and JavaScript for the frontend

## Backend (Django)

1. Install Django by running the following command:
   ```bash
   pip install django 
   ```

2. Create a new Django project by running:
   ```bash
   django-admin startproject crudapp
   ```

3. Create a new Django app within the project:
   ```bash
   cd crudapp 
   python manage.py startapp myapp
   ```

4. Open the `myapp/models.py` file and define the `Item` model:
   ```python
   from django.db import models 
   
   class Item(models.Model):
       name = models.CharField(max_length=100)
       description = models.TextField()
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
       def __str__(self):
           return self.name
   ```

5. Open the `myapp/views.py` file and add the view functions for CRUD operations:
   ```python
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
   ```

6. Create a new file `myapp/urls.py` and add the URL configuration for the app:
   ```python
   from django.urls import path
   from . import views
   
   urlpatterns = [
       path('api/items/', views.get_items, name='get_items'),
       path('api/items/create/', views.create_item, name='create_item'),
       path('api/items/update/<int:item_id>/', views.update_item, name='update_item'),
       path('api/items/delete/<int:item_id>/', views.delete_item, name='delete_item'),
   ]
   ```

7. Open the `crudapp/urls.py` file and include the URL configuration for the app:
   ```python
   from django.contrib import admin
   from django.urls import include, path
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('', include('myapp.urls')),
   ]
   ```

8. Run the server by executing the command:
   ```bash
   python manage.py runserver
   ```

## Frontend (HTML and JavaScript)

1. Create a new HTML file named `index.html` with the following content:
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>CRUD App</title>
       <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
   </head>
   <body>
       <h1>CRUD App</h1>
       
       <h2>Items</h2>
       <ul id="item-list"></ul>
   
       <h2>Create Item</h2>
       <form id="create-form">
           <input type="text" id="name" placeholder="Name" required>
           <input type="text" id="description" placeholder="Description" required>
           <button type="submit">Create</button>
       </form>
   
       <script>
           $(document).ready(function() {
               // Fetch all items on page load
               $.ajax({
                   url: '/api/items/',
                   type: 'GET',
                   success: function(response) {
                       var items = response;
                       var itemList = $('#item-list');
                       itemList.empty();
                       $.each(items, function(index, item) {
                           itemList.append('<li>' + item.name + ' - ' + item.description + ' <button onclick="editItem(' + item.id + ')">Edit</button> <button onclick="deleteItem(' + item.id + ')">Delete</button></li>');
                       });
                   }
               });
   
               // Create item
               $('#create-form').submit(function(event) {
                   event.preventDefault();
                   var name = $('#name').val();
                   var description = $('#description').val();
                   $.ajax({
                       url: '/api/items/create/',
                       type: 'POST',
                       data: { 'name': name, 'description': description },
                       success: function(response) {
                           alert(response.message);
                           location.reload();
                       }
                   });
               });
           });
   
           // Edit item
           function editItem(itemId) {
               var newName = prompt('Enter a new name:');
               var newDescription = prompt('Enter a new description:');
               $.ajax({
                   url: '/api/items/update/' + itemId + '/',
                   type: 'POST',
                   data: { 'name': newName, 'description': newDescription },
                   success: function(response) {
                       alert(response.message);
                       location.reload();
                   }
               });
           }
   
           // Delete item
           function deleteItem(itemId) {
               if (confirm('Are you sure you want to delete this item?')) {
                   $.ajax({
                       url: '/api/items/delete/' + itemId + '/',
                       type: 'POST',
                       success: function(response) {
                           alert(response.message);
                           location.reload();
                       }
                   });
               }
           }
       </script>
   </body>
   </html>
   ```

2. Open the `index.html` file in your browser, and you should see a simple CRUD app with a list of items, a create form, and the ability to edit and delete items.

Congratulations! You have successfully created a CRUD app using Django for the backend and plain HTML and JavaScript for the frontend. You can further customize and enhance the app according to your requirements.


 
 
