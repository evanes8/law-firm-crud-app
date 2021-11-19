from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.core.paginator import Paginator
from .models import Record, Standard_Record
from .forms import InputForm
from django.forms.models import model_to_dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(LoginRequiredMixin, generic.ListView):
    login_url = '/lion/accounts/login/'
    template_name= 'lion4/index.html'
    paginate_by=100
    
    def get_queryset(self):
        return Standard_Record.objects.order_by('-matter_no')


@login_required(login_url='/lion/accounts/login/')
def detail(request,record_id):
   
    record = get_object_or_404(Standard_Record, pk=record_id)

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            for field in form.cleaned_data.keys():
               setattr(record, field, form.cleaned_data[field])# int here might mess up

            record.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('saved'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm(model_to_dict(record))


    return render(request, 'lion4/detail.html', {'form': form, 'record':record})

##when i load this form i want it to be locked by deafult but then accessible 
#with a button. that button will also display submit and cancel buttons 



@login_required(login_url='/lion/accounts/login/')
def search(request):
    query=request.GET['search_bar']
    variable_column=request.GET['field']
    if variable_column == 'id' or variable_column=='matter_no':
        search_type='exact'
    else:
        search_type = 'icontains'
    filter= variable_column + '__' + search_type
    record_list= Standard_Record.objects.order_by('-matter_no').filter(**{filter:query})
    paginator = Paginator(record_list, 100 )
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'lion4/search.html', {'page_obj':page_obj} )



@login_required(login_url='/lion/accounts/login/')
def add(request):
# if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            new_record= Standard_Record()

            for field in form.cleaned_data.keys():
               setattr(new_record, field, form.cleaned_data[field])
           
            new_record.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('saved'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InputForm()


    return render(request, 'lion4/add.html', {'form': form})




@login_required(login_url='/lion/accounts/login/')
def saved(request):
    return render(request, 'lion4/saved.html')


