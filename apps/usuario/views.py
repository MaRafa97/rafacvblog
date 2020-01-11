from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

def Inicio(request):
    #template_name = 'index.html'
    intro = Introduction.objects.filter(active = True)
    accomplishment = Accomplishments.objects.all()
    experience = Experience.objects.all()
    degree = Degree.objects.all()
    education = Education.objects.all()
    softskill = SoftSkill.objects.all()
    language = Language.objects.all()
    skill = Skill.objects.all()
    contact = Contact.objects.all()
    generalinfo = GeneralInfo.objects.all()

    return render(request,'index.html',{
                'intro':intro,
                'accomplishment':accomplishment,
                'experience':experience,
                'degree':degree,
                'education':education,
                'softskill':softskill,
                'language':language,
                'skill':skill,
                'contact':contact,
                'generalinfo':generalinfo})
