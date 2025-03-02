from django.urls import path
from .views import add_item, delete_item, get_item, get_items,update_item

app_name = "items"

# a. GET /api/items/ → Return all items. 
# b. GET /api/items/?search=Item → Filter items using a query parameter. 
# c. POST /api/items/add/ → Add a new item (JSON or form data). 
# d. GET /api/items/<int:item_id>/ → Get a single item. 
# e. PUT /api/items/update/<int:item_id>/ → Update an item (JSON or form data). 
# f. DELETE /api/items/delete/<int:item_id>/ → Delete an item. 

urlpatterns = [
    path('', get_items, name='get_items'),
    path('<int:item_id>', get_item, name='get_item'),
    path('add/', add_item, name='add_item'),
    path('update/<int:item_id>', update_item, name='update_item'),
    path('delete/<int:item_id>', delete_item, name='delete_item'),
]
