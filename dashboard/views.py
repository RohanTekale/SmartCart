# from django.shortcuts import render
# from django.db.models import Count, Sum, F
# from django.contrib.auth import get_user_model
# from orders.models import Order
# from products.models import Product
# from cart.models import CartItem

# User = get_user_model()  # ✅ Correct way to get the User model

# def dashboard_view(request):
#     total_users = User.objects.count()
#     total_products = Product.objects.count()
#     total_orders = Order.objects.count()
#     total_revenue = Order.objects.aggregate(total_revenue=Sum(F('quantity') * F('product__price')))['total_revenue'] or 0

#     # ✅ Fix total cart items
#     total_cart_items = CartItem.objects.aggregate(Sum('quantity'))['quantity__sum'] or 0

#     # ✅ Fix total cart value calculation
#     total_cart_value = CartItem.objects.annotate(
#         total_price=F('quantity') * F('product__price')
#     ).aggregate(total_cart_value=Sum('total_price'))['total_cart_value'] or 0

#     # ✅ Fix for active carts (Check if CartItem has a 'user' field)
#     if hasattr(CartItem, 'user'):
#         active_carts = CartItem.objects.values('user').distinct().count()
#     else:
#         active_carts = CartItem.objects.count()  # Fallback: count total cart items

#     context = {
#         'total_users': total_users,
#         'total_products': total_products,
#         'total_orders': total_orders,
#         'total_revenue': total_revenue,
#         'total_cart_items': total_cart_items,
#         'active_carts': active_carts,
#         'total_cart_value': total_cart_value,
#     }

#     return render(request, 'dashboard/dashboard.html', context)

from django.shortcuts import render
from django.db.models import Count, Sum, F
from django.contrib.auth import get_user_model
from orders.models import Order
from products.models import Product
from cart.models import CartItem  # Ensure you import Cart if needed

User = get_user_model()

def dashboard_view(request):
    total_users = User.objects.count()
    total_products = Product.objects.count()
    total_orders = Order.objects.count()
    total_revenue = Order.objects.aggregate(
        total_revenue=Sum(F("quantity") * F("product__price"))
    )["total_revenue"] or 0

    total_cart_items = CartItem.objects.aggregate(Sum("quantity"))["quantity__sum"] or 0
    total_cart_value = (
        CartItem.objects.annotate(total_price=F("quantity") * F("product__price"))
        .aggregate(total_cart_value=Sum("total_price"))["total_cart_value"]
        or 0
    )

    # ✅ Fix Active Carts Calculation
    if hasattr(CartItem, "cart") and hasattr(CartItem, "user"):
        active_carts = CartItem.objects.filter(user__isnull=False).count()
    else:
        active_carts = CartItem.objects.count()  # Fallback: Count total cart items

    context = {
        "total_users": total_users,
        "total_products": total_products,
        "total_orders": total_orders,
        "total_revenue": total_revenue,
        "total_cart_items": total_cart_items,
        "active_carts": active_carts,
        "total_cart_value": total_cart_value,
    }

    return render(request, "dashboard/dashboard.html", context)
