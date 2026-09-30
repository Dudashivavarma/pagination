import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Student
from random import randint
from django.core.paginator import Paginator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.

def create(req):
    students=[]
    for i in range(1,101):
        student=Student(
            name=f'Student {i}',
            age=randint(18,70),
            marks=randint(35,80)
        )
        students.append(student)
    Student.objects.bulk_create(students)
    return JsonResponse({'status':'Students Added'})



def display(req):
    all_students=Student.objects.all()
    paginator=Paginator(all_students,10)
    page_no=req.GET.get('page')
    stu_obj=paginator.get_page(page_no)
    return render(req,'home.html',{'students':stu_obj})


@method_decorator(csrf_exempt,name='dispatch')
class getStudent(View):
    def get(self,req):
        return HttpResponse('THIS IS GET')
    def post(self,req):
        return HttpResponse("This is post")
    def put(self,req):
        return HttpResponse("This is put")
    def delete(self,req):
        return HttpResponse('This is delete')

@method_decorator(csrf_exempt,name='dispatch')
class crudOperation(View):
    def post(self,req):
        jsondata=json.loads(req.body)
        Student.objects.create(
            name=jsondata.get('name'),
            age=jsondata.get('age'),
            marks=jsondata.get('marks')
        )
        return JsonResponse({'status':'Studentsadded'})
    def get(self,req):
        data=Student.objects.values()
        
        return JsonResponse({'students':list(data)})


@method_decorator(csrf_exempt,name='dispatch')
class getData(View):
    # def get(self,req,id):
    #     stuobj=Student.objects.get(id=id)
    #     res={
    #         'name':stuobj.name,
    #         'age':stuobj.age,
    #         'marks':stuobj.marks
    #     }
    #     return JsonResponse({'Students':res})
    def patch(self,req,id):
        jsondata=json.loads(req.body)
        stuobj=Student.objects.get(id=id)
        stuobj.name=jsondata.get('name')
        stuobj.age=jsondata.get('age')
        stuobj.marks=jsondata.get('marks')
        stuobj.save()
        return JsonResponse({'status':'updatd successfully'})
    def delete(self,req,id):
        Student.objects.get(id=id).delete()
        return JsonResponse({'status':'deleted'})
    def get(self,req):
        data=Student.objects.all()
        students=[]
        for student in data:
            students.append(student)
        return JsonResponse({'students':students})
