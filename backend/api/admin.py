from django.contrib import admin

from api.address.models import Address
from api.cart.models import Cart, CartItem
from api.customers.models import Customer
from api.genres.models import Genre
from api.orders.models import Order, OrderItem
from api.payments.models import Payment
from api.product_tagging.models import ProductTagging
from api.products.models import Product, ProductImage
from api.tags.models import Tag
from api.user.models import User

admin.site.register(Address)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Customer)
admin.site.register(Genre)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Payment)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductTagging)
admin.site.register(Tag)
admin.site.register(User)
