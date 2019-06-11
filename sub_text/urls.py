from django.urls import path, include
from .import views
from django.contrib.auth import views as auth_views



urlpatterns = [
	
	path('', views.home, name='home'),
	path('index2', views.index2, name='index2'),
	path('signup/', views.signup, name='signup' ),
	path('accounts/', include('django.contrib.auth.urls')),
	#path('userform/', views.userfrm, name='usrfrm'),
	#path('log/', views.log, name='log1'),
	#path('logout/', views.logout1, name='logout'),
	path('welcome/', views.welcome, name='w1'),
	path('profile/', views.profile, name='profile'),
	path('about/', views.about, name='about'), 
	path('contact/', views.contact1, name='contact'),
	path('news/', views.news, name='news'),
	path('recipes/', views.recipes, name='recipes'),
	path('services/', views.services, name='services'),
	path('single/', views.single, name='single'),
	path('image/', views.img, name='showimg'),
	path('blocktry/', views.blocktry, name='blocktry'),	
	path('blocktry2/', views.blocktry2, name='blocktry2'),
	path('<int:ppid>', views.qv1, name='qv1'),
	path('<int:aid>/', views.addtocart, name='atc'),																
	path('userdata/', views.alldata, name='alldata1'),
	path('delete item/<int:did>/', views.delete, name='del'),
	#---payment--------------
    path('pp/', views.home1, name='home1'),
    path('paypal-return/', views.paypal_return, name='paypal-return'),
    path('paypal-cancel/', views.paypal_cancel,name='paypal-cancel'),
    path('a-very-hard-to-guess-url/', include('paypal.standard.ipn.urls')),
    #-----------------------------
  
]

