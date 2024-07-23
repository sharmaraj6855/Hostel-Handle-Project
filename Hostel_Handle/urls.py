from django.contrib import admin
from django.urls import path
from SellPurchase.views.old import *
from SellPurchase.views.lostItem import *
 
from django.conf import settings
from django.conf.urls.static import static
from SellPurchase.views import signup,student_login,index,addproduct,product,seller,myproducts



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index.index, name='index'),

    path('products', product.Products.as_view(), name='product'),
    path('lostItem', lostItem, name='lostItem'),
    path('addLostItem',addLostItem, name='addLostItem'),
    path('searchItem',searchItem, name='searchItem'),
      
    path('product/<int:category_id>/', product.Products.as_view(), name='product'), # ye line add k hai
    path('addproduct', addproduct.Addproduct.as_view(), name='addproduct'),
    path('student_login',student_login.Login.as_view(), name='student_login'),
    path('logout/',student_login.logout,name='logout'),
    path('signup',signup.Signup.as_view(),name='signup'),

    path('seller',seller.Seller.as_view(),name='seller'),
    path('myproducts', myproducts.Myproducts.as_view() ,name='myproducts'),


    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('addcategory', addcategory, name='addcategory'),
    path('managecategory', managecategory, name='managecategory'),
    path('editcategory<int:pid>', editcategory, name='editcategory'),
    path('deletecategory<int:pid>', deletecategory, name='deletecategory'),



    path('regstudents', regstudents, name='regstudents'),
    path('deletestudent<int:pid>', deletestudent, name='deletestudent'),
    path('listedproducts', listedproducts, name='listedproducts'),
    path('deleteproduct<int:pid>', deleteproduct, name='deleteproduct'),


   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
