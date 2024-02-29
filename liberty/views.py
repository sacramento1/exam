from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import ListView
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from liberty.forms import ItemCreateForm, ItemUpdateForm, UserLoginForm, UserRegisterForm


from liberty.models import Category, Item, Author

class ExploreView(View):
    def get(self, request):
        items = Item.objects.all()
        authors = Author.objects.all()
        categories = Category.objects.all()
        return render(request, 'explore.html', context={"items":items, "authors":authors, "categories":categories})
    
    
class DetailsView(View):
    def get(self, request, pk):
        items = Item.objects.all()
        authors = Author.objects.all()
        return render(request, 'details.html', context={"items":items, "authors":authors})
    
class AuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        items = Item.objects.all()
        return render(request, 'author.html', {'authors': authors, "items":items})
    

def home_page(request):
    items = Item.objects.all().order_by("ends_in")
    size = request.GET.get("size", 2)
    page = request.GET.get("page", 1)
    paginator = Paginator(items, size)
    page_obj = paginator.page(page)
    context = {
        "items": page_obj.object_list, 
        "page_obj": page_obj, 
        "num_pages": paginator.num_pages
    }
    return render(request, "index.html", context=context)


class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render (request, "register.html", {'form': form})
    
    def post (self, request):
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Sucessfully registered")
            return redirect("liberty:login")
        else:
            return render(request, "register.html", {'form':form})

class UserLoginview(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "login.html", {'form': form})
    
    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, f"you have logged in as {username}")
                return redirect ('liberty:create')
            else:
                messages.erorr(request, "Wrong username or password")
                return render(request, "login.html", {"form": form})
        else:
            return render(request, "login.html", {"form": form})

class UserLogout(View):
    def get(self, request):
        logout(request)
        messages.success(request, "user successfully logged out!")
        return redirect ('liberty:home')
    
class CreateView(View):
    def get(self, request):
        form = ItemCreateForm() 
        return render(request, 'create.html', {'form' : form})
    
    def post(self, request):
       form = ItemCreateForm(request.POST, request.FILES)
       if form.is_valid():
            item = form.save(commit=False)
            
            item.save()
            return redirect ('liberty:home')
       else:
           return render (request, 'create.html', {'form' : form})
       
def item_updateView(request, pk: int):
    item = Item.objects.get(pk=pk)
    if request.method == "POST":
        form = ItemUpdateForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "post successfully updated")
            return redirect('liberty:details', pk=pk)
    else:
        form = ItemUpdateForm(instance=item)
    return render(request, "update.html", {"form": form, "item":item})

def filter_items(request):
    keyword = request.POST.get('keyword')
    category = request.POST.get('category')

    items = Item.objects.all()

    if keyword:
        items = items.filter(title=keyword)

    if category:
        items = items.filter(category=category)

    return render(request, 'filtered_items.html', {'products': items})