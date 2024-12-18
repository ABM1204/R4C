from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from robots.models import Robot

def index(request):
    return render(request, 'index.html')

def get_all_robots(request):
    if request.method == "GET":
        try:
            robots = Robot.objects.all()
            robots_data = [
                {
                    "id": robot.id,
                    "serial": robot.serial,
                    "model": robot.model,
                    "version": robot.version,
                    "created": robot.created.strftime("%Y-%m-%d %H:%M:%S")
                }
                for robot in robots
            ]
            return JsonResponse({"status": "success", "data": robots_data}, status=200)
        except Exception as e:
            return JsonResponse({"status": "error", "message": "An unexpected error occurred."}, status=500)
    return JsonResponse({"status": "error", "message": "Only GET requests are allowed."}, status=405)
