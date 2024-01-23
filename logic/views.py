from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import B_cake, Wedding, Custom, Category, Team, Testimonial
from .forms import ContactForm, NewsletterForm
# Create your views here.
def index(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method=="POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    b_cake = B_cake.objects.all()
    wedding = Wedding.objects.all()
    custom = Custom.objects.all()
    category = Category.objects.all()
    team = Team.objects.all()
    test = Testimonial.objects.all()
    context = {
        "newsletter": newsletter,
        "team": team,
        "test": test,
        "category": category,
        "b_cake": b_cake,
        "wedding": wedding,
        "custom": custom,
    }
    return render(request, "index.html", context=context)

def base(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    context = {
        "newsletter": newsletter,
    }
    return render(request, "base.html", context=context)
def about(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    context = {
        "newsletter": newsletter,
    }
    return render(request, "about.html", context=context)

def contact(request):
    contact = ContactForm(request.POST or None)
    if request.method == "POST" and contact.is_valid():
        contact.save()
        return HttpResponse("<h2>Ma'lumotlaringiz muvaffaqiyatli tarzda yuborildi!")
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    context = {
        "contact": contact,
        "newsletter": newsletter,
    }
    return render(request, "contact.html", context=context)

def menu(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    b_cake = B_cake.objects.all()
    wedding = Wedding.objects.all()
    custom = Custom.objects.all()
    context = {
        "newsletter": newsletter,
        "b_cake": b_cake,
        "wedding": wedding,
        "custom": custom,
    }
    return render(request, "menu.html", context=context)

def service(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    category = Category.objects.all()
    context = {
        "newsletter": newsletter,
        "category": category,
    }
    return render(request, "service.html", context=context)

def team(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    team = Team.objects.all()
    context = {
        "newsletter": newsletter,
        "team": team,
    }
    return render(request, "Team/team.html", context=context)

def testimonial(request):
    newsletter = NewsletterForm(request.POST or None)
    if request.method == "POST" and newsletter.is_valid():
        newsletter.save()
        return HttpResponse("<h2>Emailingiz muvaffaqiyatli tarzda yuborildi!")
    test = Testimonial.objects.all()
    context = {
        "newsletter": newsletter,
        "test": test,
    }
    return render(request, "testimonial/testimonial.html", context=context)



def birthdaydetailview(request, birthday):
    birthday = get_object_or_404(B_cake, slug=birthday)
    context = {
        "birthday": birthday,
    }
    return render(request, "birthday/birthdaydetail.html", context=context)

class birthdayUpdateView(UpdateView):
    model = B_cake
    fields = "__all__"
    template_name = "birthday/birthdayEdit.html"

class birthdayDeleteView(DeleteView):
    model = B_cake
    template_name = "birthday/birthdayDelete.html"
    success_url = reverse_lazy('index')

class birthdayCreateView(CreateView):
    model = B_cake
    fields = "__all__"
    template_name = "birthday/birthdayCreate.html"

def weddingdetailview(request, wedding):
    wedding = get_object_or_404(Wedding, slug=wedding)
    context = {
        "wedding": wedding,
    }
    return render(request, "wedding/weddingdetail.html", context=context)

class weddingUpdateView(UpdateView):
    model = Wedding
    fields = "__all__"
    template_name = "wedding/weddingEdit.html"

class weddingDeleteView(DeleteView):
    model = Wedding
    template_name = "wedding/weddingDelete.html"
    success_url = reverse_lazy('index')

class weddingCreateView(CreateView):
    model = Wedding
    fields = "__all__"
    template_name = "wedding/weddingCreate.html"

def customdetailview(request, custom):
    custom = get_object_or_404(Custom, slug=custom)
    context = {
        "custom": custom,
    }
    return render(request, "custom/customdetail.html", context=context)

class customUpdateView(UpdateView):
    model = Custom
    fields = "__all__"
    template_name = "custom/customEdit.html"

class customDeleteView(DeleteView):
    model = Custom
    template_name = "custom/customDelete.html"
    success_url = reverse_lazy('index')

class customCreateView(CreateView):
    model = Custom
    fields = "__all__"
    template_name = "custom/customCreate.html"

def teamdetailview(request, team):
    team = get_object_or_404(Team, slug=team)
    context = {
        "team": team,
    }
    return render(request, "Team/teamdetail.html", context=context)
class teamUpdateView(UpdateView):
    model = Team
    fields = "__all__"
    template_name = "Team/teamEdit.html"

class teamDeleteView(DeleteView):
    model = Team
    template_name = "Team/teamDelete.html"
    success_url = reverse_lazy('index')

class teamCreateView(CreateView):
    model = Team
    fields = "__all__"
    template_name = "Team/teamCreate.html"
def categorydetailview(request, category):
    category = get_object_or_404(Category, slug=category)
    context = {
        "category": category,
    }
    return render(request, "Category/categorydetail.html", context=context)

class categoryUpdateView(UpdateView):
    model = Category
    fields = "__all__"
    template_name = "Category/categoryEdit.html"

class categoryDeleteView(DeleteView):
    model = Category
    template_name = "Category/categoryDelete.html"
    success_url = reverse_lazy('index')

class categoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    template_name = "Category/categoryCreate.html"
def testimonialdetailview(request, testimonial):
    testimonial = get_object_or_404(Testimonial, slug=testimonial)
    context = {
        "testimonial": testimonial,
    }
    return render(request, "testimonial/testimonialdetail.html", context=context)
class testimonialUpdateView(UpdateView):
    model = Testimonial
    fields = "__all__"
    template_name = "testimonial/testimonialEdit.html"

class testimonialDeleteView(DeleteView):
    model = Testimonial
    template_name = "testimonial/testimonialDelete.html"
    success_url = reverse_lazy('index')

class testimonialCreateView(CreateView):
    model = Testimonial
    fields = "__all__"
    template_name = "testimonial/testimonialCreate.html"