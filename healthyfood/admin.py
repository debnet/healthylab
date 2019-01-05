# coding: utf-8
from common.admin import EntityTabularInline, create_admin
from django.contrib import admin
from django.db.models import Prefetch
from healthyfood.models import Meal, Order, OrderItem, FoodGroup, Food, Gym, MealConsumption, MealPortion, MealReview, \
    Message, Relation, WaterConsumption


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'group', 'energy_eu', 'protein', 'carb', 'lipid', 'sugar')


class OrderItemInline(EntityTabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'price', 'status')
    inlines = (OrderItemInline, )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related(
            Prefetch('items', queryset=OrderItem.objects.select_related('meal')))


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'meal')

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('order').prefetch_related(
            Prefetch('order__items', queryset=OrderItem.objects.select_related('meal')))


create_admin(FoodGroup, Gym, Meal, MealConsumption, MealPortion, MealReview, Message, Relation, WaterConsumption, )
