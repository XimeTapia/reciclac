from django.views.generic.edit import FormView
from django.views.generic import ListView

from .models import Departamento
from .forms import NewDepartamentoForm


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
    context_object_name = 'departamentos'


class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'

    def form_valid(self, form):
        Departamento.objects.create(
            nombre=form.cleaned_data['departamento'],
            subnombre=form.cleaned_data['shorname'],
            activo=True
        )
        return super().form_valid(form)
