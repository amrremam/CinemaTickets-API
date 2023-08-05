from django.contrib import admin
from tickets import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('guests', views.ViewSets_guest)
router.register('movies', views.ViewSets_movie)
router.register('reservations', views.ViewSets_reservation)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('noRest/', views.no_rest_model),

    path('with_model/', views.with_model),

    path('rest/', views.FBV_list),

    path('fbv/<int:pk>', views.FBV_pk),

    path('mix/', views.Mixins_list.as_view()),
    path('mix/<int:pk>', views.Mixins_pk.as_view()),

    path('gene', views.Generics_list.as_view()),
    path('gene/<int:pk>', views.Generics_pk.as_view()),

    path('viewSet/', include(router.urls)),

    # find movie
    path('findMovie/', views.find_movie),

    # New Reservation
    path('newReservation/', views.new_reservation),
    # Test it with postman

    # Rest-Auth URLs Give me login and logout option
    path('api-auth', include('rest_framework.urls')),

    # Token-Authentication
    path('api-token-auth', obtain_auth_token)

]
