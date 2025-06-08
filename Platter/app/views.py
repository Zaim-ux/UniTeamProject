from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import MenuItem, Orders, Ingredient, IngredientInclusion, WaiterCall, PaymentAuthorization
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse

#Info on a specific item, in its detailed view page
def item_info(request, item_id):
    item = MenuItem.objects.get(pk=item_id)
    ingredientInclusions = IngredientInclusion.objects.filter(dish=item)
    context = {
        "item": item,
        "ingredientInclusions": ingredientInclusions,
    }

    return render(request, "itemInfo.html", context)
    
#For main menu page    
def filteredItems(request):
    # get the filter parameters from the URL
    allergy = request.GET.get('allergy', '')
    category = request.GET.get('category', '')
    spice = request.GET.get('spice', '')

    # get all menu items then filter down
    menu_items = MenuItem.getAvailable()
    itemsNotOnMenu = MenuItem.getNotAvailable()

    if allergy:
        menu_items = menu_items.exclude(allergy__icontains=allergy)
        itemsNotOnMenu = itemsNotOnMenu.exclude(allergy__icontains=allergy)

    if category:
        menu_items = menu_items.filter(category__icontains=category)
        itemsNotOnMenu = itemsNotOnMenu.filter(category__icontains=category)

    if spice:
        menu_items = menu_items.filter(spice__icontains=spice)
        itemsNotOnMenu = itemsNotOnMenu.filter(spice__icontains=spice)


    context = {
        "itemsOnMenu": menu_items,
        "itemsNotOnMenu" : itemsNotOnMenu
        }


    return render(request, "MenuPage.html", context)


#Add a specifc item to the browsers cart
def addItem(request, item_id):
    cart = request.session.get('cart', {})
    if (str(item_id) in cart.keys()):
        cart[item_id] = cart[str(item_id)] + 1
    else:
        cart[item_id] = 1
    request.session['cart'] = cart
    return redirect(checkout)

#Checkout page shows the user the items in their "cart"
def checkout(request):
    # Retrieve cart items from the session
    cart = request.session.get('cart', {})
    formattedCart = {}
    for itemID in list(cart.keys()):
        itemName = MenuItem.objects.get(pk=itemID).name
        formattedCart[itemName] = cart[itemID]

    # Prepare data to pass to the template
    context = {'cart': formattedCart}
    
    return render(request, 'checkout.html', context)

#Creates the actual database object order from the request of a cart
#redirects to thank you page while sending order ids to it
def sendOrder(request):
    try:
        cart = request.session.get('cart', {})
        order_ids = []
        for itemID in list(cart.keys()):
            order = Orders.objects.create(menuItem=MenuItem.objects.get(pk=itemID), table=request.POST["tableID"], quantity=cart[itemID], status=request.POST["status"])
            order_ids.append(order.orderID)

        request.session.pop('cart', None)
        #builds url and redirects to it, if any orders were placed
        #goes back to menu if cart is empty, and an error if it fails for another reason
        thankYou_url = reverse('thankYou')
        if order_ids:
            thankYou_url += '?order_ids=' + ','.join(map(str, order_ids))
            return redirect(thankYou_url)
        else:
            return redirect(filteredItems)
    except:
        return redirect('error')

#view for thank you page. takes order ids from urls and renders them.
def thankYouView(request):
    order_ids = request.GET.get('order_ids', '')
    id_array = order_ids.split(',')
    orders = Orders.objects.filter(orderID__in=id_array)
    context = {'orders' : orders}

    return render(request, "thankYou.html", context)

#Not used. This was for testing. - see waiterCalls or kitchen template
def viewOrders(request):
    orders = Orders.objects.all()
    context = {'orders': orders}
    return render(request, 'orderMenu.html', context)

#Staff login, waiting for General staff landing page to be implemented by assigned group members
#then redirect to that instead of waiterCalls
def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('staffPick')
            
            
        else:
            messages.success(request, ("Error logging in"))
            return redirect('login')
        
        
    else:
        return render(request, 'login.html', {})

def logout(request):
    return render(request, 'logout.html')

#Get menu items so their avaliablility can be toggled
def editMenu(request):
    itemsOnMenu = MenuItem.objects.all()
    context = {"itemsOnMenu": itemsOnMenu}
    return render(request, 'editMenu.html', context)

#Swap if a menu item is avaliable or not
def toggleAvailibility(request, itemID):
    item = MenuItem.objects.get(menuItemID=itemID)
    item.available = not item.available
    item.save()
    return redirect(editMenu)

#Load relevant data for the waiters to view
def waiterCalls(request):
    waiterCalls = WaiterCall.objects.all()
    MenuItems = MenuItem.objects.all()

    RTCOrders = Orders.objects.filter(status="RTC")#27.02.24 - waiters should see orders to take to customers
    UPDOrders = Orders.objects.filter(status="UPD")#19.03.24 - waiters should see orders that haven't been paid for

    context = {
        'waiterCalls': waiterCalls,
        'RTCOrders': RTCOrders,
        'UPDOrders': UPDOrders,
        'MenuItems': MenuItems
    }

    return render(request, 'waiterCalls.html', context)

#Information for page customer sees when submitting a call to waiters
def callWaiter(request):
    waiterCalls = WaiterCall.objects.all()
    context = {
        'waiterCalls': waiterCalls,
    }

    return render(request, 'callWaiter.html', context)

#Info seen by kitchen to call waiter
def kitchenCallWaiter(request):

    return render(request, 'kitchenCallWaiter.html')

def staffPick(request):
    return render(request, 'staffPick.html')

# https://docs.djangoproject.com/en/5.0/ref/models/instances/
#create database object waiterCall from request
#handles from all origin (customer, kitchen...)
def sendWaiterCall(request):
    try:
        if request.method == 'POST':
            tableID = request.POST.get('table')
            message = request.POST.get('message')
            originIncoming = request.POST.get('origin')

            #id should be determined automatically
            waiter_call = WaiterCall(table=tableID, message=message, origin=originIncoming)
            waiter_call.save()

        return redirect(filteredItems)

    except:
        return redirect('error')

#https://www.geeksforgeeks.org/get_object_or_404-method-in-django-models/
#Once a call is resolved, remove it.
#both of these do the same thing, perhaps merge
def clearWaiterCall(request, waiter_call_id):
    waiter_call = get_object_or_404(WaiterCall, pk=waiter_call_id)
    waiter_call.delete()
    return redirect(waiterCalls)

def cancelWaiterCall(request, waiter_call_id):
    waiter_call = get_object_or_404(WaiterCall, pk=waiter_call_id)
    waiter_call.delete()
    return redirect(waiterCalls)





#Order is finished with
#These 2 functions do the same thing, ambiguity,
#I think one should move the order back to the kitchen
def clearOrder(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    order.delete()
    return redirect('waiterCalls')

def cancelOrder(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    order.delete()
    return redirect('waiterCalls')



#General method for updating status of order.
def changeOrderStatus(request, order_id, new_status):
    order = get_object_or_404(Orders, pk=order_id)
    order.status = new_status
    order.save()
    print("changing order:{} to {}".format(order_id, new_status))
    return redirect('waiterCalls')

#Load error page
def error(request):
    return render(request, 'error.html')

#99% confident this is not used, is not used in urls.py
def menu_categories(request):
    categories = [{
        "id": "startersToggle",
        "value": "Starter"
    }]
    return render(request, 'MenuPage.html', {"categories": categories})

#Orders visible to kithcen
def kitchen(request):
    RECOrders = Orders.objects.filter(status="REC")
    CKGOrders = Orders.objects.filter(status="CKG")


    context = {
        'RECOrders': RECOrders,
        'CKGOrders': CKGOrders,
    }  

    return render(request, 'kitchen.html', context)

#Kitchen moving the order from one grid to another to mark progress
def moveToCooking(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    order.status = "CKG"
    order.save()
    return redirect('kitchen')

#sends order from kitchen to waiter.
def sendToWaiter(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    order.status = "RTC"
    order.save()
    return redirect('kitchen')

def debug(request):
    waiterCalls = WaiterCall.objects.all()
    context = {'waiterCalls': waiterCalls}
    return render(request, 'debug.html', context)

#Information to be shown in the payment form.
def authorizePayment(request):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        expiration_date = request.POST.get('expiration_date')
        cvv = request.POST.get('cvv')
        payment_method = request.POST.get('payment_method')

        payment_auth = PaymentAuthorization(
            card_number=card_number,
            expiration_date=expiration_date,
            cvv=cvv,
            payment_method=payment_method
        )
        if payment_auth.authorize_payment():
            return redirect('paymentSuccess')
        else:
            return redirect('paymentFailure')
    else:
        return render(request, 'authorizePayment.html')  
    
#gets entered order object from id in url
def orderStatus(request):
    try:
        order_id = request.GET.get('order_id', '')
        order = Orders.objects.filter(orderID = order_id)
        context = {
            'order': order,
        }
        return render(request, 'orderStatus.html', context)
    except:
        return render(request, 'orderStatus.html', {'error_message': 'Please enter a valid order ID.'})

  


