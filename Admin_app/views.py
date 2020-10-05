from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
import psycopg2
from Admin_app.models import Class,teacher as Teacher,student
# Create your views here.
def main_admin(request):
    if request.session.has_key('admin_logged'):
        return render(request, 'main_admin.html')
    else:
        return HttpResponse('''you can't access this page''')
def create_class(request):
    if request.session.has_key('admin_logged')==False:
        return HttpResponse('''you can't access this page''')
    return render(request,'add_class.html')
def add_class(request):
    if request.session.has_key('admin_logged'):
        a_class = Class()
        a_class.class_name = request.POST['class_name']
        a_class.save()
        return HttpResponse('class {} has been created'.format(
            a_class.class_name) + "<br><br><a href='/main_admin'><button>Go To Main Page</button></a>")
    else:
        return HttpResponse('''you can't access this page''')
    #a_class=Class()
    #a_class.class_name=request.POST['class_name']
    #a_class.save()
    #return HttpResponse('class {} has been created'.format(a_class.class_name) + "<br><br><a href='/main_admin'><button>Go To Main Page</button></a>")
def create_teacher(request):
    if request.session.has_key('admin_logged')==False:
        return HttpResponse('''you can't access this page''')
    conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    cur.execute('''select distinct(class_name) from public."Admin_app_class";''')
    class_list=cur.fetchall()
    class_name=[]
    print(class_list)
    for i in class_list:
        class_name.append(i[0])
    print(tuple(class_name))
    return render(request,'create_teacher.html',{'class_name':class_name,'user_type':True})
def add_teacher(request):
    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            return render(request,'create_teacher.html',{'error':'Password Not Matching'})
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=username
        x = User.objects.create_user(username=username,
                                     first_name=firstname,
                                     last_name=lastname,
                                     email=email,
                                     password=password1,
                                     )
        x.save()
        teacher=Teacher()
        teacher.teacher_name=username
        teacher.teacher_email=email
        teacher.class1=request.POST['class1']
        teacher.class2=request.POST['class2']
        teacher.class3=request.POST['class3']
        teacher.class4=request.POST['class4']
        teacher.class5=request.POST['class5']
        teacher.save()
        return HttpResponse("Teacher {} has been created".format(teacher.teacher_name)+"<br><br><a href='/main_admin'><button>Go To Main Page</button></a>")
    else:
        return redirect('create_teacher')
def create_student(request):
    if request.session.has_key('admin_logged')==False:
        return HttpResponse('''you can't access this page''')
    conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    cur.execute('''select distinct(class_name) from public."Admin_app_class";''')
    class_list=cur.fetchall()
    return render(request,'create_student.html',{'class_name':class_list,'user_type':True})
def add_student(request):
    if request.method=='POST':
        print('yes')
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1 != password2:
            return render(request,'create_student.html',{'error':'Password Not Matching','user_type':True})
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=username
        x = User.objects.create_user(username=username,
                                     first_name=firstname,
                                     last_name=lastname,
                                     email=email,
                                     password=password1,
                                     )
        Student=student()
        Student.student_name=firstname+' '+lastname
        Student.student_email=email
        Student.student_class=request.POST['class']
        Student.save()
        x.save()
        print('no error')
        return HttpResponse("student {} has been created".format(Student.student_name)+"<br><br><a href='/main_admin'><button>Go To Main Page</button></a>")
    else:
        print('error')
        return redirect('create_student')
