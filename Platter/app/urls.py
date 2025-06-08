from django.urls import path, include
from .views import item_info, checkout, addItem, sendOrder, viewOrders, login, editMenu, toggleAvailibility, kitchen, moveToCooking, sendToWaiter
from .views import item_info, checkout, addItem, sendOrder, viewOrders, login_user, filteredItems, callWaiter, sendWaiterCall, clearWaiterCall, debug, authorizePayment, orderStatus, thankYouView
from django.conf.urls import handler500
from . import views

#URL pattern defined with:
# actual URL you are typing in, the VIEW, defined in views.py to get context.
# then the name of the template that it renders
urlpatterns = [
    path('debug/', debug, name='debug'),


    path('', filteredItems, name='filteredItems'),
    path('item/<int:item_id>/', item_info, name='itemInfo'),
    path('checkout/', checkout, name='checkout'),
    path('addItem/<int:item_id>/', addItem, name="addItem"),
    path('sendOrder/', sendOrder, name="sendOrder"),
    path('viewOrders/', viewOrders, name="viewOrders"),
    path('logout/', views.logout, name="logout"),
    path('login_user/', views.login_user, name="login"),
    path('editMenu', editMenu, name="editMenu"),
    path('toggleAvailability/<int:itemID>', toggleAvailibility, name="toggleAvailability"),
    path('filteredItems/', filteredItems, name="filteredItems"),
    path('callWaiter', views.callWaiter, name="callWaiter"),
    path('kitchenCallWaiter', views.kitchenCallWaiter, name="kitchenCallWaiter"),
    path('sendWaiterCall', views.sendWaiterCall, name="sendWaiterCall"),
    path('waiterCalls/', views.waiterCalls, name="waiterCalls"),#also encapsulates RTCOrders - since both are shown on same page.
    path('clear/<int:waiter_call_id>/', clearWaiterCall, name='clearWaiterCall'),
    path('clearOrder/<int:order_id>/', views.clearOrder, name='clearOrder'),
    path('kitchen/', kitchen, name='kitchen'),
    path('moveToCooking/<int:order_id>/', views.moveToCooking, name='moveToCooking'),
    path('sendToWaiter/<int:order_id>/', views.sendToWaiter, name='sendToWaiter'),
    path('cancelOrder/<int:order_id>/', views.cancelOrder, name='cancelOrder'),
    path('authorizePayment/', authorizePayment, name='authorizePayment'),
    path('changeOrderStatus/<int:order_id>/<str:new_status>', views.changeOrderStatus, name='changeOrderStatus'),
    path('error/', views.error, name='error'),
    path('orderStatus/', views.orderStatus, name='orderStatus'),
    path('thankYou/', views.thankYouView, name='thankYou'),
    path('staffPick/', views.staffPick, name='staffPick'),
]

handler500 = views.error