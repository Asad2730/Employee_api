from rest_framework import generics
from .models import Department,Employee
from .serializers import DepartmentSerializer,EmployeeSerializer
from rest_framework.response import Response

# Create your views here.

class DepartmentCreateiew(generics.CreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class AllDepartmentView(generics.ListAPIView):
       queryset = Department.objects.all()
       serializer_class = DepartmentSerializer      
    
    
class EmployeeCreateView(generics.CreateAPIView):
       queryset = Employee.objects.all()
       serializer_class = EmployeeSerializer
       
class AllEmployeeView(generics.ListAPIView):
       queryset = Employee.objects.all()
       serializer_class = EmployeeSerializer       
       

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer      



class EmployeeUpdateView(generics.UpdateAPIView):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer    
      partial = True  
      

class EmployeeDeleteView(generics.DestroyAPIView):
      queryset = Employee.objects.all()
      serializer_class = EmployeeSerializer
      
      def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.delete()
            return Response(print('deleted emp'))            