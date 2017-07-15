from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse
from website.settings import STATIC
from website.models import *
from django.shortcuts import get_object_or_404
import os, pdb

def project(request):
    projects = Project.objects.all()
    return render(request, 'project.html', {'projects': projects})

def sub_project(request, name):
    project = get_object_or_404(Project, name=name)
    return render(request, 'sub_project.html', {'title': project.name, 'description': project.description, 'logo': project.main_img, 'images': project.images.all()})
