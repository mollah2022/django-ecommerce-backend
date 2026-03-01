from rest_framework import serializers
from .models import *
from user_api.models import SiteUser




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name','description','price','photo')
        extra_kwargs = {'photo':{'required':False}}
        depth = 1

        def create(self,validated_data):
            product = Product.objects.create(**validated_data)
            return product
        

        def update(self,instance,validated_data):
            instance.name = validated_data.get('name',instance.name)
            instance.description = validated_data.get('description',instance.description)
            instance.price = validated_data.get('price',instance.price)
            instance.photo = validated_data.get('photo',instance.photo)
            instance.save()
            return instance
        
        def delete(self,instance):
            instance.delete()
            return instance
        
class CartItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = CartItem
        fields = ('product','quantity')
        depth = 1

    def create(self,validated_data):
        cart_item = CartItem.objects.create(**validated_data)
        return cart_item
        

    def update(self,instance,validated_data):
        instance.product = validated_data.get('product',instance.product)
        instance.quantity = validated_data.get('quantity',instance.quantity)
        instance.save()
        return instance
        
    def delete(self,instance):
        instance.delete()
        return instance
    

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=SiteUser.objects.all())
    items = CartItemSerializer(many=True)
    extra_kwargs = {'status':{'required':False},'total':{'read_only':True}}

    class Meta:
        model = Orders
        fields = ('id','user','items','address','date','status','total')
        depth = 1

    def create(self,validated_data):
        user = validated_data.get('user')
        items = validated_data.get('items')
        address = validated_data.get('address')
        order = Orders.objects.create(user=user,address=address)
        for item in items:
            product = item.get('product')
            quantity = item.get('quantity')
            cart_item = CartItem.objects.create(product=product,quantity=quantity)
            order.items.add(cart_item)
        order.set_order_total()
        order.save()
        return order
    
    def update(self,instance,validated_data):
        instance.status = validated_data('status',instance.status)
        instance.save()
        return instance
    
    def delete(self,instance):
        instance.save()
        return instance