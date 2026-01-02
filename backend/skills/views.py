from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import UserSkill

@login_required
def skill_gap(request):
    user = request.user
    user_skills = UserSkill.objects.filter(user=request.user)

    response = []

    for us in user_skills:
        required_level = 4  # fixed for now
        gap = required_level - us.current_level

        if gap >= 3:
            severity = "High"
        elif gap == 2:
            severity = "Medium"
        else:
            severity = "Low"

        response.append({
            "skill": us.skill.name,
            "current_level": us.current_level,
            "required_level": required_level,
            "gap": gap,
            "severity": severity
        })

    return JsonResponse(response, safe=False)
