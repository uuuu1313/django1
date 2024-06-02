from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.utils import timezone

from .forms import CarForm
from inventory.models import Car


# Create your views here.

class MainView(TemplateView):
    template_name = 'inventory/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Jiuk"    # key(name), value(Jiuk) 값을 생성함
        return context

class CarFormView(FormView):
    template_name = 'inventory/car_basic_form.html'
    form_class = CarForm
    # success_url = '/inventory'
    success_url = reverse_lazy("inventory:main") # urls의 name을 사용함, form검증이 마친뒤에 실행되고 object를 반환함

    def form_valid(self, form):
        # POST일 경우에만 실행됨, 아래 로직이 성공하면 success_url로 이동함
        form.do_action()
        print(form.cleaned_data)
        return super().form_valid(form)

class CarCreateView(CreateView):
    # template_name = 'inventory/car_basic_form.html'
    model = Car
    fields = ['brand', 'model', 'color', 'year']
    success_url = reverse_lazy('inventory:car-list')
    # template 이름은 <app>/<model>_form.html 형식으로 명명해야함 ex) car_form.html

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CarListView(ListView):
    model = Car
    paginate_by = 100 # 한페이지당 보여줄 갯수

    # 템플릿명 <app>/<model>_list.hrml로 명명해야함 ex) inventory/car_list.html

    # optional
    # context_object_name = 'car_list' # 기본 오브젝트명은 'object_list' 이나 해당옵션으로 'car_list'로 변경가능

    # optional
    # queryset = Car.objects.filter(brand__iexact="tesla") # all이 기본이나 queryset을 tesla만 볼수있게도 지정가능

    # optional, 템플릿으로 데이터를 보내고 싶을때
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class CarDetailView(DetailView):
    model = Car


class CarUpdateView(UpdateView):
    model = Car

    # optional
    fields = ['brand', 'model', 'color', 'year']
    success_url = reverse_lazy("inventory:car-list")

    # optional
    template_name_suffix = "_update_form" # 템플릿 이름은 <app>/<model>_form.html을 기본으로 사용하나 <model>_update_form으로 변경한다는 의미


class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy("inventory:car-list")

    # optional
    # template_name_suffix = "_check_form" # 템플릿 이름은 <app>/<model>_confirm_delete.html이 기본, <model>_check_form.html으로 변경하는 의미






