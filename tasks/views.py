from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .forms import TaskForm
from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"
    paginate_by = 6
    
    
    def get_queryset(self):
        qs = Task.objects.filter(owner=self.request.user)

        # --- Filtering ---
        status = self.request.GET.get("status")
        if status == "completed":
            qs = qs.filter(completed=True)
        elif status == "open":
            qs = qs.filter(completed=False)

        # --- Sorting ---
        sort = self.request.GET.get("sort")
        
        if sort == "due":
            qs = qs.order_by("completed", "due_date")
        elif sort == "title":
            qs = qs.order_by("completed", "title")
        elif sort == "created":
            qs = qs.order_by("completed", "-created_at")
        else:
            # Default sort: completed at bottom, soonest due at top
            qs = qs.order_by("completed", "due_date")

        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["today"] = timezone.now().date()
        ctx["current_status"] = self.request.GET.get("status", "")
        ctx["current_sort"] = self.request.GET.get("sort", "")
        return ctx


def task_detail(request, pk):
    # Use pk (primary key) to fetch the task
    task = get_object_or_404(Task, pk=pk)

    # Deny access if the current user is not the owner
    if task.owner != request.user:
        return render(
            request,
            '403.html',
            {'message': "You do not have permission to view this task."},
            status=403
        )
    
    return render(request, "tasks/task_detail.html", {"task": task})


@login_required
def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            messages.success(request, "Task created successfully.")
            return redirect('tasks:task_list')
        
    else:
        form = TaskForm()
    
    return render(request, 'tasks/task_form.html', {'form': form})


@login_required
def task_edit(request, pk):
    """
    POST > validate and save (owner remains)
    GET > show task form with instance populated (owner must match)
    """
    task = get_object_or_404(Task, pk=pk)

    # Owner check
    if task.owner != request.user:
        return render(
            request,
            '403.html',
            {'message': "You do not have permission to edit this task."},
            status=403
        )
        
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Task updated successfully.")
            return redirect('tasks:task_detail', pk=task.pk)
        else:
            messages.error(request, "Task not updated. Please correct the errors below.")
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})


@login_required
def task_delete(request, pk):
    """
    POST > delete and redirect
    GET > show confirmation page
    """
    task = get_object_or_404(Task, pk=pk)

    if task.owner != request.user:
        return render(
            request,
            '403.html',
            {'message': "You do not have permission to delete this task."},
            status=403
        )

    if request.method == "POST":
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect('tasks:task_list')
    
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})


@login_required
@require_POST
def task_toggle_complete(request, pk):
    """"
    Toggle the completed flag for a task (POST only).
    Only the task owner can toggle.
    Redirect to task list.
    """
    task = get_object_or_404(Task, pk=pk)

    if task.owner != request.user:
        return render(
            request,
            '403.html',
            {'message': "You do not have permission to modify this task."},
            status=403
        )
    
    #Toggle and save
    task.completed = not task.completed
    task.save()

    if task.completed:
        messages.success(request, "Task marked as completed.")
    else:
        messages.success(request, "Task marked as incomplete.")
    
    return redirect('tasks:task_list')
