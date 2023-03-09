from django.shortcuts import render,redirect,get_object_or_404
import csv
from django.views.generic.edit import DeleteView
from django.http import HttpResponse
from django.shortcuts import render
from faker import Faker
from django.urls import reverse_lazy
from .forms import CSVDataForm, UserLoginForm, CSVDataForm_e
from .models import CSVData
from django.contrib.auth import login, logout
from django.utils import  timezone


def edit_csvdata(request, pk):
    csvdata = get_object_or_404(CSVData, pk=pk)

    if request.method == 'POST':
        form = CSVDataForm_e(request.POST, instance=csvdata)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CSVDataForm_e(instance=csvdata)

    return render(request, 'gen/edit_cvsdata.html', {'form': form})


class MyModelDeleteView(DeleteView):
    model = CSVData
    success_url = reverse_lazy('main')

def main(request):
    obj = CSVData.objects.all()
    context = {
        'obj':obj
    }
    return render(request,'gen/landing.html',context=context)


def user_logout(requset):
    user = requset.user
    logout(user)
    redirect('main')



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('main')
    else:
            form = UserLoginForm()
    return render(request, 'gen/login.html',{"form":form})





def generate_csv(request):
    form = CSVDataForm()
    if request.method == 'POST':
        form = CSVDataForm(request.POST)
        if form.is_valid():
            min_value = form.cleaned_data['min_value']
            max_value = form.cleaned_data['max_value']
            name = form.cleaned_data['name']
            num_rows = form.cleaned_data['num_rows']
            fake = Faker()
            data = []
            for i in range(num_rows):
                row = [
                    fake.name(),
                    fake.job(),
                    fake.email(),
                    fake.domain_name(),
                    fake.phone_number(),
                    fake.company(),
                    fake.text(),
                    fake.random_int(min=min_value, max=max_value),
                    fake.address(),
                    fake.date_this_century()
                ]
                data.append(row)
            csv_data = CSVData(name=name,date=timezone.now())
            csv_data.save()
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{name}.csv"'
            writer = csv.writer(response)
            input_f = 'Full Name, Job, Email, Domain,Phone,Company,Text,Int,Address,Date'
            split_field = input_f.split(',')

            writer.writerow(split_field)
            writer.writerows(data)

            return response
    return render(request, 'gen/csv_form.html', {'form': form})
