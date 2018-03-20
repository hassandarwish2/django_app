from datetime import datetime, timedelta, date, timezone
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, reverse
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,UpdateView
from tracks_jogging.forms import  UserSignupForm,TodoListCreateForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import logout

# Create your views here.
from tracks_jogging.models import TrackList, TodoItem, Track
from django.db.models import Sum,Count


class SignupView(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('login')

class MyLogin(LoginView):
    template_name = 'login.html'


def signout(request):
    logout(request)

    return render(request, 'base.html')


class ListOwnerOrAdminMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        qs = super().get_queryset()

        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        if not self.request.user.is_staff:
            qs = qs.filter(user=self.request.user)
            if start_date and end_date and not self.request.user.is_staff:
                qs = qs.filter(date__gte=start_date,date__lte=end_date,user=self.request.user)
        return qs


class MyLists(ListOwnerOrAdminMixin, ListView):
    model = Track








class TodoListUpdateView(ListOwnerOrAdminMixin, UpdateView):
        model = Track
        fields = ('time','distance','date')

        def get_success_url(self):
            return reverse('mylists')


class AddTodoListView(CreateView):
    model = Track
    form_class = TodoListCreateForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('mylists')



class DeleteTodoListView(ListOwnerOrAdminMixin, DeleteView):
    model = Track
    success_url = reverse_lazy('mylists')




def trackweek(request):
    context={}

    some = datetime.now().date() - timedelta(days=7)
    context['total']= Track.objects.all().aggregate(Sum('time'))
    if not request.user.is_staff:
        context['weeks'] = Track.objects.filter(date__gte=some, user=request.user)
    else:
        context['weeks'] = Track.objects.filter(date__gte=some)

    return render(request,'filter7.html',context)


def trackmonth(request):
    context={}
    some = datetime.now().date() - timedelta(days=30)
    if not request.user.is_staff:
        context['months'] = Track.objects.filter(date__gte=some, user=request.user)
    else:
        context['months'] = Track.objects.filter(date__gte=some)

    return render(request,'filter7.html',context)

