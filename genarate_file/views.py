from django.views.generic.edit import FormView
from django.views.generic import ListView
from .form import GenerateRandomCSVForm
from django.shortcuts import redirect
from .tasks import generate_file
from .models import FileCSVModel
from django.core.files import File


# Create your views here.

class GenerateRandomCSVView(FormView):
    template_name = 'task/generate_csv.html'
    form_class = GenerateRandomCSVForm

    def form_valid(self, form):
        filename = form.cleaned_data.get('filename')
        data_count = form.cleaned_data.get('data_count')
        generate_file.delay(filename, data_count)
        with open('media/temp.csv', mode='r') as file:
            newfile = FileCSVModel(file=File(file, name=f'{filename}.csv'),filename=filename)
            newfile.save()
        return redirect('home')


class ShowFiles(ListView):
    template_name = 'files.html'
    model = FileCSVModel
    context_object_name = 'files'
