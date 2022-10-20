from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from . forms import UserForm,LoginForm,ProductForm,UserUdateForm,ChangepassForm,ProdUpdateForm
from . models import MyUser, Product, User_Purchase
from datetime import datetime
from django.urls import reverse



def home(request):
    if 'email' not in request.session:
        return redirect('/')
    user = MyUser.objects.get(email=request.session['email'])
    return render(request, 'buysell/home.html', context={'user':user})

def signup(request):
    if 'email' not in request.session:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            return render(request, 'buysell/signup.html', {'form':form})
        form = UserForm(None)
        return render(request,'buysell/signup.html', {'form':form})
    return redirect('/home')



def login(request):
    if 'email' not in request.session:
        if request.method == 'POST':
            form = LoginForm(request.POST) 
            email = request.POST['email']
            password = request.POST['password']
            if form.is_valid():
                request.session['email'] = email  
                return redirect('home')          
            return render(request, 'buysell/login.html', {'form':form})
        form = LoginForm(None)
        return render(request, 'buysell/login.html', {'form':form})
    return redirect('home')


def updateprofile(request):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        if request.method == 'POST':
            form = UserUdateForm(request.POST, instance=MyUser.objects.get(email=request.session.get('email')))
            if form.is_valid():                            
                form.save()
                messages.success(request, 'Profile updated successfully')
                return redirect('/home')
            messages.error(request, ('error try updating again'))
            return render(request,'buysell/update_profile.html',{'form': form, 'user':user})
        form = UserUdateForm(instance=MyUser.objects.get(email=request.session.get('email')))
        return render(request,'buysell/update_profile.html',{'form': form, 'user':user})
    return redirect('/')

    

def changepass(request):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        if request.method == 'POST':
            form = ChangepassForm(request.POST)
            if form.is_valid():
                user = MyUser.objects.get(email=request.session.get('email'))
                old_password = form.cleaned_data.get('old_password')
                new_password = form.cleaned_data.get('new_password')                
                if old_password != user.password:
                    messages.error(request, ('incorrect old password'))
                    return render(request,'buysell/changepass.html',{'form': form, 'user':user})
                user.password = new_password
                user.save()
                messages.success(request,'Password changed successfully')
                return redirect('/home')
            return render(request,'buysell/changepass.html',{'form': form,'user':user})
        form = ChangepassForm()
        return render(request,'buysell/changepass.html',{'form': form, 'user':user})
    return redirect('/')

    

def productview(request):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        if user.user_role_id == 2:
            products = Product.objects.filter(created_by_user=user.id, is_deleted=False)
            if request.method == 'POST':    
                form = ProductForm(request.POST.copy(),request.FILES)
                form.data['created_by_user'] = user.id            
                if form.is_valid():
                    form.save()              
                    messages.success(request,'Product added successfully')
                    return redirect('/productview')
                return render(request, 'buysell/prodview.html',{'products':products,'form':form,'user':user})
            form = ProductForm(None)      
            products = {'products':products,'form':form,'user':user, 'product':Product}
            return render(request, 'buysell/prodview.html', context=products)
        else:
            products = Product.objects.filter(is_deleted=False)
            return render(request, 'buysell/prodview.html', context={'products':products, 'user':user})
    return redirect('/')

def update_product(request, id):
    if 'email' in request.session:
        if id is not None:
            user = MyUser.objects.get(email=request.session['email'])
            try:
                product = Product.objects.filter(id=id, created_by_user=user, is_deleted=False).first()
            except OverflowError:
                return redirect('/productview')
            except:
                product = None
            if product is None: 
                return redirect('productview')
            if request.method == 'POST':
                form = ProdUpdateForm(request.POST,request.FILES, instance= product)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Product Updated Successfully')
                    return redirect('/productview')
                messages.error(request, ('try again'))
                return render(request,'buysell/updateprod.html',{'form': form,'user':user})                
            form = ProdUpdateForm(instance=product)
            return render(request,'buysell/updateprod.html', context={'form':form, 'user':user})
        return redirect('/productview')
    return redirect('/')

def delprod(request, id):
    if 'email' in request.session:
        user = MyUser.objects.get(email=request.session.get('email'))
        print(id, 'product id')
        if id is not None:
            try:                
                prod = Product.objects.get(id=id, created_by_user=user)
                prod.is_deleted = True
                prod.save()
                messages.error(request, 'Product Deleted Sucessfully')
                return redirect('/productview')
            except Exception as e:
                return redirect('/productview')
                
        return redirect('/productview')
    return redirect('/')


def buyprod(request,id):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        try:
            product = Product.objects.filter(id = id, is_deleted=False).first()
        except:
            product = None
        if product is not None:
            try:
                quantity = int(request.POST['quantity'])  
            except:
                quantity = None
                return redirect('/productview')            
            if quantity > product.stock_unit or quantity < 0:
                return redirect('/productview')  
            total_price = quantity * product.prod_sell_price      
            context = {'product':product, 'quantity':quantity, 'total_price': total_price, 'user':user}
            return render(request, 'buysell/buyprod.html', context= context)
        return redirect('/productview')
    return redirect('/')

def placeorder(request, id):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        try:
            quantity = int(request.POST['quantity'])
        except:
            return redirect('/productview')
        try:
            product = Product.objects.get(id=id, is_deleted=False)
        except:
            product = None        
        if product is None:
            return redirect('/productview')
        buyer = MyUser.objects.get(email = request.session['email'])
        seller = MyUser.objects.get(id = product.created_by_user_id)
        total_price = product.prod_sell_price * quantity
        if quantity > product.stock_unit or quantity < 0:
            context = {'product':product, 'quantity':quantity, 'total_price': total_price, 'user':user}
            messages.error(request, 'Product is out of stock')
            return render(request, 'buysell/buyprod.html', context= context)
        if total_price > buyer.balance:
            context = {'product':product, 'quantity':quantity, 'total_price': total_price, 'user':user}
            messages.error(request, 'Insuffcient balance')
            return render(request, 'buysell/buyprod.html', context= context)
        if buyer.user_role_id != 1:
            return redirect('/')    
        buyer.balance -= total_price
        seller.balance += total_price
        product.stock_unit -= quantity
        buyer.save()
        seller.save()
        product.save()

        user_order = User_Purchase(product_id=product, total_unit = quantity, purchased_by_user = buyer,purchased_from_user = seller)
        user_order.save()
        order_date = datetime.today()
        return render(request,'buysell/placeorder.html', context={'product':product, 'seller':seller, 'order_date':order_date ,'quantity':quantity, 'order_total':total_price, 'user':user})
    return redirect('/')

def orderhistory(request):
    if 'email' in request.session:
        user = MyUser.objects.get(email = request.session['email'])
        if user.user_role_id == 2:
            orders = User_Purchase.objects.filter(purchased_from_user=user) 
            return render(request, 'buysell/orders.html', context={'orders':orders, 'user':user})
        else:
            orders = User_Purchase.objects.filter(purchased_by_user=user)
            return render(request, 'buysell/orders.html', context={'orders':orders, 'user':user})
    return redirect('/')

def logout(request):
    if 'email' in request.session:
        del request.session['email']
        return redirect('/')
    return redirect('/')
