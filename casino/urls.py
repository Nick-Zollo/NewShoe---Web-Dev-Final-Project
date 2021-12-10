from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index/', views.indexLogged, name="indexLogged"),
    path('fruitspin/', views.fruitSpin, name="FruitSpin"),
    path('updateBalFromSlot/', views.updateBalFromSlot, name="updateBalFromSlot"),
    path('hiddentreasure/', views.hiddenTreasure, name="HiddenTreasure"),
    path('explosivereels/', views.explosiveReels, name="ExplosiveReels"),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('deposit/', views.deposit, name='deposit'),
    path('depositCustom/', views.depositCustom, name='depositCustom'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('withdrawCustom/', views.withdrawCustom, name='withdrawCustom'),
    path('allDeposits/', views.allDeposits, name='allDeposits'),
    path('allWithdraws/', views.allWithdraws, name='allWithdraws')
]
