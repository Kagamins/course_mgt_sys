from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView
from django.db.models import Q

from .forms import StudentEditForm
from .models import Student


@login_required
def student_profile(request, pk):
    qs = Student.objects.get(pk=pk)
    return render(
        request,
        'student_profile.html',
        {
            'student': qs,
        })


class StudentRegister(CreateView):
    # to use the models variable
    model = Student
    # we require all fields since students will need register him/her self
    fields = '__all__'
    template_name = 'student_profile_create.html'


def edit_profile(request, student_id):
    obj = Student.objects.get(pk=student_id)
    if request.method == 'POST':
        form = StudentEditForm(request.POST, instance=obj)
        if form.is_valid():

            form.save()

            return redirect('student_view')
    else:
        form = StudentEditForm(instance=obj)
    return render(request,
                  'student_profile_edit.html',
                  {
                      'student': obj,
                      'form': form,
                  })

def student_search(request, search_text):
    qs = Students.objects.filter(Q(name=search_text) | Q(university_id=search_text))
    return render(requst,'student_list.html',{'students' : qs})
