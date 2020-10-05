from django.shortcuts import render
from django.http import HttpResponse
from Teacher_app.models import test,ques
from Student_app.models import test_status as ts
from django.contrib.auth.models import User
import psycopg2
# Create your views here.
def teacher(request):
    if request.session.has_key('teacher_logged')==False:
        return HttpResponse("you can't access this page")
    conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    t=request.user.email
    cur.execute(
        '''
        select test_name from public."Teacher_app_test" where test_teacher='{}';
        '''.format(t)
    )
    t_l=cur.fetchall()
    test_list=[]
    for i in t_l:
        test_list.append(i[0])
    print(test_list)
    return render(request,'teacher.html',{'test_list':test_list})
def create_test(request):
    email=request.user.email
    conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    cur.execute('''select class1,class2,class3,class4,class5 from public."Admin_app_teacher" where teacher_email='{}';'''.format(email))
    class_list=[]
    li=cur.fetchall()
    for i in li[0]:
        if i!='None':
            class_list.append(i)
    print(class_list,li)
    return render(request,'ques1.html',{'class_list':class_list})
def creating_test(request):
    if request.method=="POST":
        test_name=request.POST['title'].replace(' ','_')
        test_class=request.POST['cls']
        test_teacher=request.user.email
        Test=test()
        Test.test_name=test_name
        Test.test_class=test_class
        Test.test_teacher=test_teacher
        try:
            Test.save()
        except Exception:
            return HttpResponse('Test already created')
        n=0
        for i in range(1,100):
            Quest=ques()
            Quest.question=request.POST['q{}'.format(i)]
            Quest.marks = request.POST['m{}'.format(i)]
            n+=1
            Quest.op1=request.POST['a{}'.format(n)]
            n+=1
            Quest.op2=request.POST['a{}'.format(n)]
            n+=1
            Quest.op3=request.POST['a{}'.format(n)]
            n+=1
            Quest.op4=request.POST['a{}'.format(n)]
            cop_num=request.POST['c_a{}'.format(i)]
            op={'1':Quest.op1,'2':Quest.op2,'3':Quest.op3,'4':Quest.op4,'':None}
            Quest.cop=op[cop_num]
            Quest.test_name=test_name
            if Quest.question=='':
                break
            Quest.save()
        Test.save()
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute('''select student_email from public."Admin_app_student" where student_class='{}';'''.format(test_class))
        s_l=cur.fetchall()
        print(s_l)

        for i in s_l:
            print(i[0])
            test_st = ts()
            test_st.test_name=test_name
            test_st.student_email=i[0]
            test_st.test_status=False
            test_st.save()
        return HttpResponse('test {} created <br><br><a href="teacher"><button>Main page</button></a>'.format(test_name))



def teacher_profile(request):
    return None
def check_result(request):
    if request.session.has_key('teacher_logged'):
        user_type=True
    else:
        user_type=False
    if request.method=='POST':
        test_name=request.POST['test_name']
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute('''
        select test_status, student_email from public."Student_app_test_status" where test_name='{}';
        '''.format(test_name))
        s_d=cur.fetchall()
        s_details=[]
        for i in s_d:
            if i[0]==True:
                cur.execute('''
                select score_obtained from public."Student_app_test_score" where student_email='{}';
                '''.format(i[1]))
                score=cur.fetchall()
                score=int(score[0][0])
            else:
                score=0
            s_details.append([i[1],score,i[0]])
        return render(request,'class_result.html',{'student_list':s_details,'user_type':user_type})






    return None