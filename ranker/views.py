from django.shortcuts import render, redirect, get_object_or_404
from .forms import user_handle_form
from .models import user_handle
from .spoj_scrapper import spoj_crawler

def home_view(request):
    context = { "handles" : user_handle.objects.all().order_by("-points")}
    if request.method == "POST":
        submitted_handle = user_handle_form(request.POST)
        if submitted_handle.is_valid():
            user_info = spoj_crawler(request.POST["handle_name"])
            if user_info.handleExists and len(user_handle.objects.filter(handle_name = request.POST["handle_name"])) == 0:
                new_handle = user_handle(
                    handle_name = user_info.handle_name,
                    user_name = user_info.name,
                    user_location = user_info.locale,
                    joining_date = user_info.joined_on,
                    world_rank = int(user_info.world_rank),
                    points = user_info.points,
                    institution = user_info.institution,
                    problems_solved = user_info.problems_solved,
                    total_submissions = user_info.solutions_submitted
                )
                new_handle.save()
                return redirect("home_view")
    else:
        context["form"] = user_handle_form()
    return render(request, "ranker/main_view.html", context)

def delete_handle(request, pk):
    if len(user_handle.objects.filter(handle_name = pk)) > 0:
        db_handle = get_object_or_404(user_handle, pk = pk)
        db_handle.delete()
    return redirect("home_view")

def detailed_view(request, pk):
    if len(user_handle.objects.filter(handle_name = pk)) > 0:
        context = { "db_handle" : get_object_or_404(user_handle, pk = pk) }
        return render(request, "ranker/detailed_view.html", context)
    return redirect("home_view")

