from django.shortcuts import render,redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import logout,login as Login
import psycopg2
# Create your views here.
def login_page(request):
    return render(request,'login.html')
def Logout(request):
    logout(request)
    return redirect('login_page')
@method_decorator(csrf_exempt)
def login(request):
    if request.method == 'POST':
        email = request.POST.get('useremail', '')
        password = request.POST.get('password', '')
        user_type = request.POST.get('type', '')
        user = auth.authenticate(username=email, password=password)
        print(user,email,password)
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123",
                                host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        if user_type=='admin':
            cur.execute('''
                        select count(*) from public."Admin_app_teacher" where teacher_email='{}';
                        '''.format(email))
            t_c = cur.fetchall()
            t_c = int(t_c[0][0])
            cur.execute('''
                        select count(*) from public."Admin_app_student" where student_email='{}';
                        '''.format(email))
            s_c = cur.fetchall()
            s_c = int(s_c[0][0])
            if s_c+t_c>0:
                return HttpResponse('ERROR 404')
            Login(request, user)
            request.session['admin_logged'] = True
            return redirect('main_admin')
        if user_type=='faculty':
            cur.execute('''
                        select count(*) from public."Admin_app_student" where student_email='{}';
                        '''.format(email))
            s_c = cur.fetchall()
            s_c = int(s_c[0][0])
            if s_c > 0:
                return HttpResponse('ERROR 404')

            Login(request, user)
            request.session['teacher_logged'] = True
            return redirect('teacher')
        if user_type=='student':
            cur.execute('''
                        select count(*) from public."Admin_app_teacher" where teacher_email='{}';
                        '''.format(email))
            t_c = cur.fetchall()
            t_c = int(t_c[0][0])
            if t_c > 0:
                return HttpResponse('ERROR 404')
            Login(request, user)
            request.session['student_logged'] = True
            return redirect('student_home')
        else:
            return HttpResponse('arey_tham_jaa')

    else:
        return redirect('login_page')

