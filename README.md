# LittleLemon
Django Project with Javascript and HTML for FrontEnd.

# Available End Points:
  * /restaurant/    restaurant.views.index  home
  * /restaurant/booking/    rest_framework.routers.APIRootView      api-root
  * /restaurant/booking/tables/     restaurant.views.BookingViewSet booking-list
  * /restaurant/booking/tables/<pk>/        restaurant.views.BookingViewSet booking-detail
  * /restaurant/menu/       restaurant.views.MenuItemView
  * /restaurant/menu/       restaurant.views.index  home
  * restaurant/menu/<int:pk>       restaurant.views.SingleMenuItemView
  * /restaurant/menu/menu/  restaurant.views.MenuItemView
  * /restaurant/menu/menu/<int:pk>  restaurant.views.SingleMenuItemView
