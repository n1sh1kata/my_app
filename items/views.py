import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET
from django.views.decorators.http import require_http_methods
from django.core.files.uploadhandler import TemporaryFileUploadHandler
from django.http.multipartparser import MultiPartParser

# Bonus (10 points): Ensure the Python list updates dynamically upon adding, updating, and 
# deleting. 

items = []

# http://localhost:8000/api/items/
# http://localhost:8000/api/items/?search=anything
@csrf_exempt
@require_GET
def get_items(request):
    search_query = request.GET.get('search', '')
    filtered_items = [item for item in items if search_query.lower() in item['name'].lower()]
    return JsonResponse({"message": "Item(s) Retrieved Successfully", "payload": {'items': filtered_items if search_query else items}, "developed_by":"Nishikata"}, status=200)

# http://localhost:8000/api/items/1
@csrf_exempt
@require_GET
def get_item(request, item_id):
    try:
        item = next((item for item in items if item['id'] == item_id), None)
        if item:
            return JsonResponse({"message": "Item Retrieved Successfully", "payload": {'items': item}, "developed_by":"Nishikata"}, status=200)
        else:
            return JsonResponse({"message": "Item Not Found", "payload": {'error': f'Item {item_id} not found'}, "developed_by":"Nishikata"}, status=404)
    except ValueError:
        return JsonResponse({"message": "Item Not Found", "payload": {'error': f'Item {item_id} is invalid'}, "developed_by":"Nishikata"}, status=400)

# http://localhost:8000/api/add/
# can use form-data and json
@csrf_exempt
@require_POST
def add_item(request):
    try:
        if request.content_type == 'application/json':
            data = json.loads(request.body)
            name = data.get('name')
        else:
            name = request.POST.get('name')

        if not name:
            return JsonResponse({"message": "Invalid", "payload": {'error': 'Name is required'}, "developed_by":"Nishikata"}, status=400)

        new_item = {'id': len(items) + 1, 'name': name}
        items.append(new_item)
        return JsonResponse({"message": "Item added Successfully", "payload": {'item': new_item}, "developed_by":"Nishikata"}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({"message": "Invalid", "payload": {'error': 'Invalid JSON data'}, "developed_by":"Nishikata"}, status=400)

# http://localhost:8000/api/update/1
# can use form-data and json
@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    try:
        item_id = int(item_id)
        item = next((item for item in items if item['id'] == item_id), None)
        if not item:
            return JsonResponse({"message": "Not Found", "payload": {'error': 'Item not found'}, "developed_by":"Nishikata"}, status=404)

        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                name = data.get('name')
            except json.JSONDecodeError:
                return JsonResponse({"message": "Invalid", "payload": {'error': 'Invalid JSON data'}, "developed_by":"Nishikata"}, status=400)
        elif request.content_type.startswith('multipart/form-data'):
            request.upload_handlers = [TemporaryFileUploadHandler()]
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, files = parser.parse()

            name = data.get('name')
            print("Form Data Name:", name)
        else:
            return JsonResponse({"message": "Unsupported", "payload": {'error': 'Unsupported content type'}, "developed_by":"Nishikata"}, status=415)

        if name:
            item['name'] = name
            return JsonResponse({"message": "Item Updated Successfully", "payload": {'item': item}, "developed_by":"Nishikata"}, status=200)
        else:
            return JsonResponse({"message": "Invalid", "payload": {'error': 'No valid data provided'}, "developed_by":"Nishikata"}, status=400)
    except ValueError:
        return JsonResponse({"message": "Invalid", "payload": {'error': 'Invalid item ID'}, "developed_by":"Nishikata"}, status=400)

# http://localhost:8000/api/delete/1
@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    global items
    try:
        items = [item for item in items if item['id'] != item_id]
        return JsonResponse({"message": "Item Deleted Successfully", "developed_by":"Nishikata"}, status=200)
    except ValueError:
        return JsonResponse({"message": "Invalid", "payload": {'error': 'Invalid item ID'}, "developed_by":"Nishikata"}, status=400)