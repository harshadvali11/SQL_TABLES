from django.shortcuts import render

# Create your views here.
from app.models import *

def empdept(request):
    LEDO=Emp.objects.select_related('deptno').all()
    #LEDO=Emp.objects.select_related('deptno').filter(job='SALESMAN')
    LEDO=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    LEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    LEDO=Emp.objects.select_related('deptno').filter(mgr__isnull=True,ename__startswith='j')
    LEDO=Emp.objects.select_related('deptno').all()
    LEDO=Emp.objects.select_related('deptno').filter(deptno__dname='Development')    
    d={'LEDO':LEDO}
    return render(request,'empdept.html',d)

def empmgr(request):
    LEMO=Emp.objects.select_related('mgr').all()
    LEMO=Emp.objects.select_related('mgr').filter(mgr__isnull=False)
    LEMO=Emp.objects.select_related('mgr').filter(deptno=30)
    LEMO=Emp.objects.select_related('mgr').filter(sal__gt=20000)
    LEMO=Emp.objects.select_related('mgr').filter(mgr__sal__gt=20000)
    
    
    d={'LEMO':LEMO}
    return render(request,'empmgr.html',d)

def empdeptmgr(request):
    LEDMO=Emp.objects.select_related('deptno','mgr').all()
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='RESEARCH')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Rama Chilaka')
    LEDMO=Emp.objects.select_related('deptno','mgr').filter(comm__isnull=False)
    
    
    d={'LEDMO':LEDMO}
    return render(request,'empdeptmgr.html',d)






