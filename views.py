from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages


from .models import Tender
from .forms import RegistrationForm, TenderForm


def index(request):
    return render(request, "tenders/index.html")

def tender_list(request):
    now = timezone.now()
    tenders = (
        Tender.objects
        .filter(status=Tender.Status.OPEN, closing_date__gte=now)
        .select_related("category", "created_by")
        .order_by("closing_date")
    )
    return render(request, "tenders/tender_list.html", {"tenders": tenders})


def contact(request):
    return render(request, "tenders/contact.html")

def reports(request):
    return render(request, "tenders/reports.html")

def suppliers(request):
    return render(request, "tenders/suppliers.html")

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")
    else:
        form = RegistrationForm()

    return render(request, "tenders/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_staff:
                return redirect("/admin/")
            
            return redirect("tender_list")
        
        messages.error(request, "Invalid username or password.")

    return render(request, "tenders/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")  



def create_tender(request):
    if request.method == "POST":
        form = TenderForm(request.POST, request.FILES)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.created_by = request.user
            tender.save()
            messages.success(request, "Tender created successfully!")
            return redirect("tender_list")
    else:
        form = TenderForm()

    return render(request, "tenders/create_tender.html", {"form": form})


def edit_tender(request, tender_id):
    tender = get_object_or_404(Tender, id=tender_id)

    if request.method == "POST":
        form = TenderForm(request.POST, request.FILES, instance=tender)
        if form.is_valid():
            form.save()
            messages.success(request, "Tender updated successfully!")
            return redirect("tender_list")
    else:
        form = TenderForm(instance=tender)

    return render(request, "tenders/edit_tender.html", {"form": form, "tender": tender})        
        
