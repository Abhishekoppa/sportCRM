from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q,Sum,Count
from .models import *
from .fitness_celebrities import FITNESS_CELEBRITIES

def ctx(request):
 c=Cart.objects.filter(user=request.user).first() if request.user.is_authenticated else None
 return {'cart_count':sum(i.quantity for i in c.items.all()) if c else 0}
def home(request): return render(request,'store/home.html',{'categories':Category.objects.prefetch_related('products').all(),'featured':Product.objects.filter(featured=True)[:12],'products':Product.objects.order_by('-created_at')[:12],'celebrities':FITNESS_CELEBRITIES,**ctx(request)})
def products(request):
 qs=Product.objects.select_related('category').all(); q=request.GET.get('q',''); cat=request.GET.get('category'); sort=request.GET.get('sort','-created_at')
 if q: qs=qs.filter(Q(name__icontains=q)|Q(description__icontains=q))
 if cat: qs=qs.filter(category__slug=cat)
 if sort in ['price','-price','name','-created_at']: qs=qs.order_by(sort)
 from django.core.paginator import Paginator
 page=Paginator(qs,12).get_page(request.GET.get('page'))
 return render(request,'store/products.html',{'page':page,'categories':Category.objects.all(),'q':q,'active_cat':cat,**ctx(request)})
def product(request,slug): return render(request,'store/product.html',{'product':get_object_or_404(Product,slug=slug),'related':Product.objects.filter(category=get_object_or_404(Product,slug=slug).category).exclude(slug=slug)[:4],**ctx(request)})
@login_required
def add_cart(request,pk):
 p=get_object_or_404(Product,pk=pk); c,_=Cart.objects.get_or_create(user=request.user); item,_=CartItem.objects.get_or_create(cart=c,product=p); item.quantity+=1 if item.pk else 0; item.save(); return redirect(request.META.get('HTTP_REFERER','cart'))
@login_required
def cart(request):
 c,_=Cart.objects.get_or_create(user=request.user); return render(request,'store/cart.html',{'cart':c,**ctx(request)})
@login_required
def update_cart(request,pk):
 item=get_object_or_404(CartItem,pk=pk,cart__user=request.user); qty=max(0,int(request.POST.get('quantity',1))); item.delete() if qty==0 else (setattr(item,'quantity',qty),item.save()); return redirect('cart')
@login_required
def checkout(request):
 c=get_object_or_404(Cart,user=request.user); items=list(c.items.select_related('product')); total=sum(i.total for i in items)
 if request.method=='POST' and items:
  o=Order.objects.create(user=request.user,total=total,address=request.POST.get('address','')); [OrderItem.objects.create(order=o,product=i.product,quantity=i.quantity,price=i.product.price) for i in items]; c.items.all().delete(); return redirect('order_detail',o.pk)
 return render(request,'store/checkout.html',{'cart':c,'total':total,**ctx(request)})
@login_required
def orders(request): return render(request,'store/orders.html',{'orders':request.user.orders.all(),**ctx(request)})
@login_required
def order_detail(request,pk): return render(request,'store/order_detail.html',{'order':get_object_or_404(Order,pk=pk,user=request.user),**ctx(request)})
@login_required
def wishlist(request): return render(request,'store/wishlist.html',{'items':request.user.wishlist.select_related('product'),**ctx(request)})
@login_required
def toggle_wishlist(request,pk):
 p=get_object_or_404(Product,pk=pk); x=Wishlist.objects.filter(user=request.user,product=p); x.delete() if x.exists() else Wishlist.objects.create(user=request.user,product=p); return redirect(request.META.get('HTTP_REFERER','wishlist'))
@login_required
def dashboard(request):
 return render(request,'store/dashboard.html',{'orders':request.user.orders.all()[:5],'requests':ServiceRequest.objects.filter(user=request.user)[:5],'reminders':MaintenanceReminder.objects.filter(user=request.user),**ctx(request)})
@login_required
def support(request):
 if request.method=='POST': ServiceRequest.objects.create(user=request.user,request_type=request.POST['request_type'],subject=request.POST['subject'],description=request.POST['description']); return redirect('support')
 return render(request,'store/support.html',{'requests':ServiceRequest.objects.filter(user=request.user),**ctx(request)})
def register(request):
 if request.method=='POST':
  u=User.objects.create_user(request.POST['username'],request.POST.get('email',''),request.POST['password']); Profile.objects.create(user=u); login(request,u); return redirect('home')
 return render(request,'registration/register.html')
@login_required
def admin_dashboard(request):
 if not request.user.is_staff: return redirect('home')
 stats={'products':Product.objects.count(),'customers':User.objects.count(),'orders':Order.objects.count(),'sales':Order.objects.aggregate(Sum('total'))['total__sum'] or 0}; return render(request,'store/admin_dashboard.html',{'stats':stats,'orders':Order.objects.order_by('-created_at')[:8],**ctx(request)})
