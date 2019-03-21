from django.shortcuts import render
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage

from .models import RealEstateProject, SectionProject
from .forms import ProjectForm

from datetime import datetime


def indexPageView(request):
    return render(request, 'home.html')


def projectsListPageView(request):
    context = {
        'projects': RealEstateProject.objects.all()
    }
    return render(request, 'projects-list.html', context)


def projectDetailPageView(request, pk):
    sections = SectionProject.objects.filter(project=pk)
    if(sections.first() is not None):
        context = {
            'project_id': pk,
            'sections': sections,
            'project_name': sections.first().project
        }
        return render(request, 'project-detail.html', context)
    else:
        return render(request, 'project-detail-not-found.html')


def projectCreatePageView(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            # print(data['title'])
            if 'image' in request.FILES:
                newImage = request.FILES['image']
            else:
                newImage = None

            # Add new project to data
            if(newImage is not None):
                fs = FileSystemStorage()
                path = 'uploaded_images/{0:%Y/%m/%d}/{1}'.format(
                    datetime.now(), newImage)
                fs.save(path, newImage)
                project = RealEstateProject.objects.create(name=data['title'],
                                                           image=path,
                                                           description=data['\
description'])
            else:
                RealEstateProject.objects.create(name=data['title'],
                                                 image='default.jpg',
                                                 description=data['\
description'])

            return redirect('projects_list')
        else:
            print(form.errors)
    context = {
        'form': form
    }

    return render(request, 'project_new.html', context)
