from django.shortcuts import render
import psycopg2
from django.http import HttpResponse
from Student_app.models import test_score, test_status as ts
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
# Create your views here.
def student_home(request):
    if request.session.has_key('student_logged'):
        user_type=True
        student_name=request.user.email

    else:
        user_type=False
    conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
    cur = conn.cursor()
    print('hello')
    cur.execute('''select student_class from public."Admin_app_student" where student_email='{}';'''.format(student_name))
    cls=cur.fetchall()
    cls=cls[0][0]
    #cur.execute('''select test_name from public."Teacher_app_test" where test_class='{}';'''.format(cls))
    cur.execute('''select test_name from public."Student_app_test_status" where test_status='{f}' and student_email='{s}';'''.format(f=False,s=student_name))
    test=cur.fetchall()
    test_list=[]
    for t in test:
        test_list.append(t[0])
    cur.execute('''select test_name from public."Student_app_test_status" where test_status='{}' and student_email='{}';'''.format(True,student_name))
    taken_test_list=cur.fetchall()
    tt_l=[]
    for i in taken_test_list:
        tt_l.append(i[0])
    if len(tt_l)>0:
        taken_test_field=True
    else:
        taken_test_field=False
    print(test_list,tt_l)
    if len(test_list)>0:
        take_test_field=True
    else:
        take_test_field=False
    return render(request,'student.html',{'user_type':user_type,'take_test_list':test_list,'take_test_field':take_test_field,
                                          'taken_test_field':taken_test_field,'taken_test_list':tt_l})
@method_decorator(csrf_exempt)
def take_test(request):
    if request.session.has_key('student_logged'):
        user_type=True
    else:
        user_type=False
    if request.method=='POST':
        test_name=request.POST.get('testname','')
        student_name=request.user.email
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute(
            '''select question , op1 , op2 , op3 , op4 , cop, marks from public."Teacher_app_ques" where test_name='{tn}' ;'''.format(
                tn=test_name))
        q_l = cur.fetchall()
        for i in range(len(q_l)):
            q_l[i]=list(q_l[i])
            q_l[i].append(i)
        print(q_l)
        cur.execute(
            '''select test_status from public."Student_app_test_status" where test_name='{}' and student_email='{}';
            '''.format(test_name, student_name))
        test_taken=cur.fetchall()
        print(test_taken)
        test_taken=test_taken[0][0]
        return render(request,'take_test.html',{'ques_ans_list':q_l,'num_of_qsns':len(q_l),'testname':test_name,'test_taken':test_taken})
    else:
        return HttpResponse('Ruko Abhi sabar karo')
@method_decorator(csrf_exempt)
def submit_test(request):
    if request.method=='POST':
        student_email=request.user.email
        test_name=request.POST['testname']
        num_of_qsns=request.POST['num_of_qsns']
        marks=0
        score=0
        wans=0
        rans=0
        print(num_of_qsns,end=" ")
        for i in range(int(num_of_qsns)):
            selected_ans=request.POST['selected_ans_for qsn_{}'.format(i)]
            cop=request.POST['cop{}'.format(i)]
            if selected_ans==cop:
                rans+=1
                score+=int(request.POST['marks{}'.format(i)])
            else:
                wans+=1
            marks+=int(request.POST['marks{}'.format(i)])
            print(selected_ans,cop,end=' ')
        Test_score=test_score()
        Test_score.test_name=test_name
        Test_score.student_email=student_email
        Test_score.wrong_ans=wans
        Test_score.right_ans=rans
        Test_score.test_status=True
        Test_score.total_marks=marks
        Test_score.score_obtained=score
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                                port="5432")
        cur = conn.cursor()
        cur.execute(
            '''select student_class from public."Admin_app_student" where student_email='{}';'''.format(student_email))
        student_class=cur.fetchall()
        test_class=student_class[0][0]
        Test_score.test_class=test_class
        cur.execute('''update public."Student_app_test_status" set test_status=True where test_name='{}' and student_email='{}';commit;'''.format(test_name,
                                                                                                                                            student_email))
        Test_score.save()
        print(marks,wans,rans,test_name)

    return HttpResponse('you have taken the test')


def check_score(request):
    if request.session.has_key('student_logged'):
        user_type=True
    else:
        False
    if request.method=='POST':
        student_name=request.user.email
        test_name=request.POST['testname']
        conn = psycopg2.connect(database="online_exam_app", user="postgres", password="Roshan@rsr123", host="127.0.0.1",
                            port="5432")
        cur = conn.cursor()
        cur.execute(
            '''select score_obtained from public."Student_app_test_score" where test_name='{}' and student_email='{}';'''.format(test_name,
                                                                                                                             student_name)
        )
        score=cur.fetchall()
        score=score[0][0]
        cur.execute(
            '''
            select test_teacher from public."Teacher_app_test" where test_name='{}';
            '''.format(test_name)
        )
        teacher=cur.fetchall()
        teacher=teacher[0][0]
        return render(request,'student_result.html',{'test_name':test_name,'teacher_name':teacher,
                                                 'score':score,'student_name':student_name,'user_type':user_type})
    else:
        return HttpResponse('Error 404')
    
