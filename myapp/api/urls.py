from django.urls import path
from .views import EmployeeCreateView,DepartmentCreateiew,EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView,AllDepartmentView,AllEmployeeView

urlpatterns = [
    path('emp/', EmployeeCreateView.as_view(), name='emp-list-create'),
    path('emp/<int:pk>/', EmployeeDetailView.as_view(), name='emp-detail'),
    path('emps/all', AllEmployeeView.as_view(), name='all-emp-list'),  
    path('emp/delete/<int:pk>/', EmployeeDeleteView.as_view(), name='emp-delete'), 
    path('emp/update/<int:pk>/', EmployeeUpdateView.as_view(), name='emp-update'), 
    
    path('dep/', DepartmentCreateiew.as_view(), name='dep-list-create'),
    path('dep/all',AllDepartmentView.as_view(), name='all-dep-list'),  
]