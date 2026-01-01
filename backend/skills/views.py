from django.http import JsonResponse

def skill_gap(request):
    data = [
        {
            "skill": "Python",
            "current_level": 2,
            "required_level": 4,
            "gap": 2,
            "severity": "High"
        },
        {
            "skill": "SQL",
            "current_level": 1,
            "required_level": 3,
            "gap": 2,
            "severity": "Medium"
        }
    ]
    return JsonResponse(data, safe=False)
