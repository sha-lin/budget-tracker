from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Budget

# Create your views here.
@login_required(login_url='/login/')
def budgets(request):
    salary = 0
    if request.method == 'POST':
        data = request.POST
        earnings = int(data.get('salary', 0))
        name = data.get('name')
        price = int(data.get('price', 0))
 
        Budget.objects.create(
            earnings=earnings,
            name=name,
            price=price,
        )
        return redirect('/')
 
    queryset = Budget.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))
 
    # Calculate the total sum
    total_sum = sum(budget.price for budget in queryset)
     
    context = {'budgets': queryset, 'total_sum': total_sum}
    return render(request, 'budget.html', context)
 
# Update the budgets data
@login_required(login_url='/login/')
def update_budget(request, id):
    queryset = Budget.objects.get(id=id)
 
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        price = int(data.get('price', 0))
 
        queryset.name = name
        queryset.price = price
        queryset.save()
        return redirect('/')
 
    context = {'budget': queryset}
    return render(request, 'update_budget.html', context)
 
# Delete the budgets data
@login_required(login_url='/login/')
def delete_budget(request, id):
    queryset = Budget.objects.get(id=id)
    queryset.delete()
    return redirect('/')
 
# Login page for user
def login_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username).first()
            if not user_obj:
                messages.error(request, "Username not found")
                return redirect('/login/')
            user_auth = authenticate(username=username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('budget')
            messages.error(request, "Wrong Password")
            return redirect('/login/')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register/')
    return render(request, "login.html")
 
# Register page for user
def register_page(request):
    if request.method == "POST":
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, "Username is taken")
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, "Account created")
            return redirect('/login')
        except Exception as e:
            messages.error(request, "Something went wrong")
            return redirect('/register')
    return render(request, "register.html")
 
# Logout function
def custom_logout(request):
    logout(request)
    return redirect('login')
 
# Generate the Bill
@login_required(login_url='/login/')
def format(request):
    if request.method == 'POST':
        data = request.POST
        earnings = int(data.get('earnings'))
        name = data.get('name')
        price = int(data.get('price', 0))
 
        Budget.objects.create(
            earnings=earnings,
            name=name,
            price=price,
        )
        return redirect('format')
 
    queryset = Budget.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            name__icontains=request.GET.get('search'))
 
    # Calculate the total sum
    total_sum = sum(budget.price for budget in queryset)
    # Get the username
    username = request.user.username
 
    context = {'budget': queryset, 'total_sum': total_sum, 'username':username}
    return render(request, 'format.html', context)
