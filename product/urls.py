from django.urls import path
from product.views import UserLogin,UserLogout,Home,ProductCreate,ProductList,ProductUpdate,ProductDelete,ExportProducts,ImportProducts,OrderCreate,OrderList,OrderDetailView,OrderUpdate,OrderDelete

urlpatterns = [
    path('', UserLogin.as_view(), name='login'),
    path('logout/', UserLogout.as_view(), name='logout'),
    path('home/', Home.as_view(), name='home'),
    path('pcreate/', ProductCreate.as_view(), name='product_create'),
    path('plist/', ProductList.as_view(), name='product_list'),
    path('pupdate/<int:id>/', ProductUpdate.as_view(), name='product_update'),
    path('pdelete/<int:id>/', ProductDelete.as_view(), name='product_delete'),
    path('export/', ExportProducts.as_view(), name='export_products_excel'),
    path('import/', ImportProducts.as_view(), name='import_products'),
    path('ocreate/', OrderCreate.as_view(), name='order_create'),
    path('olist/', OrderList.as_view(), name='order_list'),
    path('order/<int:id>/', OrderDetailView.as_view(), name='order_detail'),      
    path('order/update/<int:id>/', OrderUpdate.as_view(), name='order_update'), 
    path('order/delete/<int:id>/', OrderDelete.as_view(), name='order_delete'), 
    
    
]