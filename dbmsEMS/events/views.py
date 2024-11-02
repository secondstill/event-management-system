from django.shortcuts import render, get_object_or_404, redirect
from .models import Event, Attendance
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# List all events
def event_list(request):
    events = Event.objects.all()

    # Pass extra context for each event regarding registration and attendance status
    for event in events:
        event.is_registered = event.attendance_set.filter(student=request.user).exists() if request.user.is_authenticated else False
        if event.is_registered:
            event.attendance = event.attendance_set.get(student=request.user)
        else:
            event.attendance = None

    return render(request, 'events/event_list.html', {'events': events})

# Register for an event
@login_required
def register_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if event.attendance_set.filter(student=request.user).exists():
        return redirect('event_list')  # Already registered
    if event.attendance_set.count() >= event.registration_limit:
        return redirect('event_list')  # Event is full
    Attendance.objects.create(student=request.user, event=event)
    return redirect('event_list')

# Mark attendance
@login_required
def mark_attendance(request, event_id):
    attendance = get_object_or_404(Attendance, student=request.user, event_id=event_id)
    attendance.check_in = True
    attendance.save()
    return redirect('event_list')

# User signup view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
