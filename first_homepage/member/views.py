from django.shortcuts import render
from .models import User
import random

# Create your views here.


def ajax_login(req):
    return render(req, 'ajax_login.html')


def ajax_test(req):
    return render(req, 'c.html', {'p1': req.POST.get('id_'), 'p2': req.POST.get('pw_')})


# 회원가입 창 띄우기

def join(req):
    return render(req, 'join.html')


# 회원가입


def joined(req):
    newmember = User.objects.filter(userid=req.POST.get('id'))

    if newmember:
        return render(req, 'join.html', {'err': "이미 존재하는 아이디입니다."})
    else:
        newmember = User(userid=req.POST.get('id'), username=req.POST.get(
            'name'), password=req.POST.get('pw'), gender=req.POST.get('gender'))
        newmember.save()
        return render(req, 'joined.html')

    # return render(req, 'joined.html', {'info1': req.POST.get('id'), 'info2': req.POST.get('name'), 'info3': req.POST.get('gender')})


def login(req):
    return render(req, 'login.html')


def logined(req):
    logmember = User.objects.filter(
        userid=req.POST.get('id'), password=req.POST.get('pw'))

    # 로그인 성공 {'id':req.POST.get('id')}
    if logmember:
        req.session['userid'] = req.POST.get('id')
        return render(req, 'logined.html', {'total_member': logmember, 'id': req.POST.get('id'), 'sus': "환영합니다!"})
    else:
        return render(req, 'fail_login.html')


def check_logined(req):
    if req.session.get('userid'):
        return render(req, 'logined.html', {'id': req.session.get('userid'), 'sus': "환영합니다!"})
    else:
        return render(req, 'login.html')


def logout(req):
    req.session.pop('userid')
    return render(req, 'logout.html')


def change(req):
    return render(req, 'resetPW.html')


def changed(req):
    changepw = User.objects.get(
        userid=req.POST.get('id')
    )
    print(changepw)
    changepw.password = req.POST.get('newpw')
    changepw.save()

    return render(req, 'changed.html',  {'info1': req.POST.get('id')})


def signout(req):
    return render(req, 'signout.html')


def userdelete(req):
    userdelete = User.objects.filter(
        userid=req.POST.get('id'), password=req.POST.get('pw'))

    if userdelete:
        userdelete.delete()
        return render(req, 'userdelete.html')
    else:
        return render(req, 'g.html')

    #######################################################
    # 질문!!
    # delete 할 때 if userdelete, else로 넣으면 모두 else에 있는 값만 반환되게 됨
    # delete 되었을 경우에만 userdelete.html을 띄우고
    # delete 되지 않고 없는 id, 없는 pw일 경우에는 g.html(회원정보확인해라)띄우고 싶은데
    # 어떻게 하면 좋을까요?
    #######################################################


def send(req):
    return render(req, 'b.html')


def statictest(req):
    return render(req, 'f.html')

    # 일단 넘어온 frontend를 DB에 넣는 코드 삽입
    # if req.POST.get('stet') == "frontend":
    # info3 = "프론트엔드"


def rec(req):
    objects = req.POST.getlist('color')
    return render(req, 'd.html', {'colors': objects, 'info1': req.POST.get('id'), 'info2': req.POST.get('pw'), 'info3': req.POST.get('stet'), 'info4': req.POST.getlist('color')})


def novel(req, chapter, player1, player2):
    return render(req, 'c.html', {'c': chapter, 'p1': player1, 'p2': player2})
