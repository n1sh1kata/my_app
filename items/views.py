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

@csrf_exempt
@require_GET
def get_items(request):
    search_query = request.GET.get('search', '')
    filtered_items = [item for item in items if search_query.lower() in item['name'].lower()]
    return JsonResponse({'items': filtered_items if search_query else items}, status=200)

@csrf_exempt
@require_GET
def get_item(request, item_id):
    try:
        item = next((item for item in items if item['id'] == item_id), None)
        if item:
            return JsonResponse({'item': item}, status=200)
        else:
            return JsonResponse({'error': f'Item {item_id} not found'}, status=404)
    except ValueError:
        return JsonResponse({'error': 'Invalid item ID'}, status=400)

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
            return JsonResponse({'error': 'Name is required'}, status=400)

        new_item = {'id': len(items) + 1, 'name': name}
        items.append(new_item)
        return JsonResponse({'message': 'Item added', 'item': new_item}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def update_item(request, item_id):
    try:
        item_id = int(item_id)
        item = next((item for item in items if item['id'] == item_id), None)
        if not item:
            return JsonResponse({'error': 'Item not found'}, status=404)
        
        print("Request Content-Type:", request.content_type)

        if request.content_type == 'application/json':
            try:
                data = json.loads(request.body)
                name = data.get('name')
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON data'}, status=400)
        elif request.content_type.startswith('multipart/form-data'):
            request.upload_handlers = [TemporaryFileUploadHandler()]
            parser = MultiPartParser(request.META, request, request.upload_handlers)
            data, files = parser.parse()

            name = data.get('name')
            print("Form Data Name:", name)
        else:
            return JsonResponse({'error': 'Unsupported content type'}, status=415)

        if name:
            item['name'] = name
            return JsonResponse({'message': 'Item updated', 'item': item}, status=200)
        else:
            return JsonResponse({'error': 'No valid data provided'}, status=400)
    except ValueError:
        return JsonResponse({'error': 'Invalid item ID'}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_item(request, item_id):
    global items
    try:
        items = [item for item in items if item['id'] != item_id]
        return JsonResponse({'message': 'Item deleted'}, status=200)
    except ValueError:
        return JsonResponse({'error': 'Invalid item ID'}, status=400)