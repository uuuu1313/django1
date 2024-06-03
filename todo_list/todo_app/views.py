from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import ToDoItem, ToDoList
# Create your views here.

class ListListView(ListView):
    model = ToDoList
    template_name = "todo_app/index.html"

class ItemListView(ListView):
    model = ToDoItem
    template_name = "todo_app/todo_list.html"

    def get_queryset(self): # ListView에 Resolve 되있는 함수
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])  # list_id로 filter함

    def get_context_data(self): # ListView에 resolve되어 있는 함수 (오버라이드)
        context = super().get_context_data()
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])  # list_id로 get 함
        print("=!@#")
        # print(self.object_list.get().id)
        return context

class ListCreate(CreateView):
    model = ToDoList
    fields = ["title"]  # 해당 필드만 이용자가 입력 가능

    success_url = reverse_lazy("index")

    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()
        context["title"] = "Add a new List"
        return context

class ItemCreate(CreateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_initial(self):   # GET, POST 둘에 공통된 작업을 수행
        initial_data = super(ItemCreate, self).get_initial()
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        initial_data["todo_list"] = todo_list
        return initial_data

    def get_context_data(self, **kwargs):
        context = super(ItemCreate, self).get_context_data(**kwargs)
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])
        context["todo_list"] = todo_list
        context["title"] = "Create a new Item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list.id])

class ItemUpdate(UpdateView):
    model = ToDoItem
    fields = [
        "todo_list",
        "title",
        "description",
        "due_date",
    ]

    def get_context_data(self, **kwargs):
        context = super(ItemUpdate, self).get_context_data()
        context["todo_list"] = self.object.todo_list    # self는 현재 클래스의 인스턴스, object는 TodoItem 객체가 됨
        context["title"] = "Edit Item"
        return context

    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list.id])

class ListDelete(DeleteView):
    model = ToDoList

    success_url = reverse_lazy("index")

class ItemDelete(DeleteView):
    model = ToDoItem

    def get_success_url(self):
        return reverse("list", args=[self.kwargs["list_id"]])

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["todo_list"] = self.object.todo_list
        return context





