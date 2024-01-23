from django.shortcuts import render
from .forms import UserRegistrationForm
from .forms import ProfileEditForm, UserEditForm

# Create your views here.
def dashboardview(request):
    user = request.user
    context = {
        "user": user,
    }
    return render(request, "pages/user_profile.html", context=context)

def password_change_view(request):
    return render(request, "password_change_form.html", context={})

def user_register(request):
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(
            user_form.cleaned_data["password"]
        )
        new_user.save()
        context = {
            "new_user": new_user,
        }
        return render(request, "account/register_done.html", context)
    else:
        user_form = UserRegistrationForm()
        context = {
            "user_form": user_form,
        }
        return render(request, "account/register.html", context)


def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()


    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/profile_edit.html', {"user_form": user_form, "profile_form": profile_form})