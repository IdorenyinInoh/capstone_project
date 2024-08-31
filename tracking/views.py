from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Attendance, DutyPost, Staff

@login_required
def dashboard(request):
    attendances = Attendance.objects.filter(staff__user=request.user)
    return render(request, 'tracking/dashboard.html', {'attendances': attendances})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        duty_post = DutyPost.objects.get(id=request.POST['duty_post'])
        attendance = Attendance(staff=request.user.staff, duty_post=duty_post, status='Present')
        attendance.save()
        return redirect('dashboard')
    duty_posts = DutyPost.objects.all()
    return render(request, 'tracking/mark_attendance.html', {'duty_posts': duty_posts})

@login_required
def duty_post_list(request):
    duty_posts = DutyPost.objects.all()
    return render(request, 'tracking/duty_post_list.html', {'duty_posts': duty_posts})
