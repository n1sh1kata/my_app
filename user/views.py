from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST, require_GET

@csrf_exempt
@require_GET
def all(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
        ]
    return JsonResponse({"message": "Successfully created", "payload": data}, status=200)

@csrf_exempt
@require_GET
def get_user(request, id):
    try:
        data = {
            "id": id,
            "username": "giervan"
        }
        return JsonResponse({"message": "User Fetched Successfully", "payload": data}, status=200)
    except:
        return JsonResponse({"message": "Failed.", "payload": data}, status=400)

    
@csrf_exempt
@require_POST
def add_user(request):
    try:
        return JsonResponse({"message": "User Added Successfully"}, status=200)
    except:
        return JsonResponse({"message": "Failed."}, status=400)
    
@csrf_exempt
@require_POST
def update_user(request, id):
    try:
        data = {
            "id": id,
            "username": "giervan"
        }
        return JsonResponse({"message": "User Updated Successfully", "payload": data}, status=200)
    except:
        return JsonResponse({"message": "Failed."}, status=400)
    
@csrf_exempt
@require_POST
def delete_user(request, id):
    try:
        data = {
            "id": id,
            "username": "giervan"
        }
        return JsonResponse({"message": "User Deleted Successfully", "payload": data}, status=200)
    except:
        return JsonResponse({"message": "Failed."}, status=400)