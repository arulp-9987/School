from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.urls import reverse_lazy
from .models import Teacher


# READ - ALL TEACHERS
class TeacherListView(ListView):

    model = Teacher

    template_name = 'teachers/teacher_list.html'

    context_object_name = 'teachers'


# READ - SINGLE TEACHER
class TeacherDetailView(DetailView):

    model = Teacher

    template_name = 'teachers/teacher_detail.html'

    context_object_name = 'teacher'


# CREATE TEACHER
class TeacherCreateView(CreateView):

    model = Teacher

    fields = [
        'name',
        'email',
        'phone',
        'subject',
        'qualification',
        'experience',
        'joining_date',
        'salary'
    ]

    template_name = 'teachers/teacher_form.html'

    success_url = reverse_lazy('teacher_list')


# UPDATE TEACHER
class TeacherUpdateView(UpdateView):

    model = Teacher

    fields = [
        'name',
        'email',
        'phone',
        'subject',
        'qualification',
        'experience',
        'joining_date',
        'salary'
    ]

    template_name = 'teachers/teacher_form.html'

    success_url = reverse_lazy('teacher_list')


# DELETE TEACHER
class TeacherDeleteView(DeleteView):

    model = Teacher

    template_name = 'teachers/teacher_confirm_delete.html'

    success_url = reverse_lazy('teacher_list')
