from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import Career
from .models import Award
from .form import AwardForm
from django.contrib import messages
from django.forms.models import model_to_dict

def index(request):
	try:
		content_list = Career.objects.order_by('-career_date')[:5]
		award_list =Award.objects.order_by('-award_date')[:5]
	except Career.DoesNotExist:
		raise Http404('No Content')
	return render(request,'kik_profile/index.html',\
							{'content_list':content_list,'award_list':award_list})

def career_list(request):
	try:
		content_list = Career.objects.order_by('-career_date')[:5]
	except Career.DoesNotExist:
		raise Http404('No Content')
	return render(request,'kik_profile/list.html',\
							{'content_list':content_list})

def award_list(request):
	try:
		content_list =Award.objects.order_by('-award_date')[:5]
	except Award.DoesNotExist:
		raise Http404('No Content')
	return render(request,'kik_profile/award.html',\
							{'content_list':content_list})

def award_create(request):
    if request.method=='POST':
        award_form = AwardForm(request.POST)
        if award_form.is_valid():
            award_form.save()
        return redirect('/award/')
    else:
        award_form = AwardForm()
    return render(request, 'kik_profile/award_form.html', {'award_form': award_form})

def award_read(request, pk):
    award_instance = get_object_or_404(Award, id=pk)
    printmsg = "";
    printmsg = model_to_dict(award_instance)
    messages.info(request, printmsg)
    return render(request, 'kik_profile/award_read.html', {'award_instance': award_instance})

def award_update(request, pk):
    award_instance = get_object_or_404(Award, id=pk)
    if request.method=='POST':
        award_form = AwardForm(request.POST, instance=award_instance)
        if award_form.is_valid():
            award_form.save()
        return redirect('/award/')
    else:
        award_form = AwardForm(instance=award_instance)
    return render(request, 'kik_profile/award_form.html', {'award_form': award_form})

def award_delete(request, pk):
    award_instance = get_object_or_404(Award, id=pk)
    award_instance.delete()
    return redirect('/award/')