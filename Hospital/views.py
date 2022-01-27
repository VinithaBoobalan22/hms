from django.shortcuts import render,redirect
from django.http import HttpResponse
import mysql.connector as mysql
from django.middleware import csrf

def home(request):
	return render(request,'home.html')

def admin_login(request):
	return render(request,'admin_login.html')

def admin_login_data(request):
	Emailid=request.POST.get("Email")
	Password=request.POST.get("pass")
	if Emailid == 'vinitha123@gmail.com' and Password == 'vinitha123':
		return render(request,'admin_home.html')
	else:
		return render(request,'admin_login.html')

def admin_home(request):
	return render(request,'admin_home.html')
	
def admin_doctor_home(request):
	return render(request,'admin_doctor_home.html')

def admin_add_doctor(request):
	return render(request,'admin_add_doctor.html')

def admin_add_doctor_data(request):
	Firstname=request.POST.get("fname")
	Lastname=request.POST.get("lname")
	Username=request.POST.get("Email")
	Password=request.POST.get("pass")
	Contact=request.POST.get("num")
	Department=request.POST.get("sec")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="insert into doctor_reg_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(Firstname,Lastname,Username,Password,Contact,Department)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'admin_doctor_home.html')

def admin_update_doctor(request):
	return render(request,'admin_update_doctor.html')

def admin_update_doctor_success(request):
	Username=request.POST.get("Email")
	Password=request.POST.get("pass")
	Contact=request.POST.get("num")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="update doctor_reg_data set Contact='{2}',Username='{0}' where Password='{1}'".format(Username,Password,Contact)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'admin_doctor_home.html')
	
def admin_doctor_record(request):
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="select * from doctor_reg_data"
	cr.execute(query)
	result = cr.fetchall()
	conn.commit()
	conn.close()
	return render(request,'admin_doctor_record.html',{'result':result})
	
def admin_patient_home(request):
	return render(request,'admin_patient_home.html')

def admin_add_patient(request):
	return render(request,'admin_add_patient.html')

def admin_add_patient_data(request):
	Username=request.POST.get("name")
	Password=request.POST.get("pass")
	Contact=request.POST.get("num")
	Symptoms=request.POST.get("symptoms")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="insert into patient_reg_data values('{0}','{1}','{2}','{3}')".format(Username,Password,Contact,Symptoms)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'admin_patient_home.html')

def admin_remove_patient(request):
	return render(request,'admin_remove_patient.html')

def admin_remove_patient_success(request):
	Username=request.POST.get('name')
	Password=request.POST.get('pass')
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	cr.execute("delete from patient_reg_data where Username='{0}' and Password='{1}'".format(Username,Password))
	conn.commit()
	conn.close()
	return render(request,'admin_patient_home.html')

def admin_patient_record(request):
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="select * from patient_reg_data"
	cr.execute(query)
	result=cr.fetchall()
	conn.commit()
	conn.close()
	return render(request,'admin_patient_record.html',{'result':result})
	
def admin_logout(request):
	return render(request,'admin_login.html')
	
def admin_doctor_logout(request):
	return render(request,'admin_home.html')
	
def admin_patient_logout(request):
	return render(request,'admin_home.html')
	
def doctor_login(request):
	return render(request,'doctor_login.html')

def doctor_forget_password(request):
	return render(request,'doctor_forget_password.html')

def doctor_change_password(request):
	Username=request.POST.get("Email")
	Password=request.POST.get("pass")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="update doctor_reg_data set Password='{1}' where Username='{0}'".format(Username,Password)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'doctor_login.html')
	
def doctor_register(request):
	return render(request,'doctor_register.html')
	
def doctor_reg_data(request):
	Firstname=request.POST.get("fname")
	Lastname=request.POST.get("lname")
	Username=request.POST.get("Email")
	Password=request.POST.get("pass")
	Contact=request.POST.get("num")
	Department=request.POST.get("sec")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="insert into doctor_reg_data values('{0}','{1}','{2}','{3}','{4}','{5}')".format(Firstname,Lastname,Username,Password,Contact,Department)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'doctor_login.html')

def doctor_login_data(request):
	Username=request.POST.get("Email")
	Password=request.POST.get("pass")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	cr.execute("select * from doctor_reg_data")
	while True:
		row=cr.fetchone()
		if row is None:
			break;
		elif row[2]==Username and row[3]==Password:		
			return render(request,'doctor_home.html')
	return render(request,'doctor_login.html')

def doctor_home(request):
	return render(request,'doctor_home.html')
 
def doctor_logout(request):
	return render(request,'doctor_login.html')
	
def patient_login(request):
	return render(request,'patient_login.html')

def patient_forgot_password(request):
	return render(request,'patient_forgot_password.html')

def patient_change_password(request):
	Username=request.POST.get("name")
	Password=request.POST.get("pass")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="update patient_reg_data set Password='{1}' where Username='{0}'".format(Username,Password)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'patient_login.html')

def patient_register(request):
	return render(request,'patient_register.html')
	
def patient_reg_data(request):
	Username=request.POST.get("name")
	Password=request.POST.get("pass")
	Contact=request.POST.get("num")
	Symptoms=request.POST.get("symptoms")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	query="insert into patient_reg_data values('{0}','{1}','{2}','{3}')".format(Username,Password,Contact,Symptoms)
	cr.execute(query)
	conn.commit()
	conn.close()
	return render(request,'patient_login.html')
	
def patient_login_data(request):	
	Username=request.POST.get("name")
	Password=request.POST.get("pass")
	conn=mysql.connect(host="localhost",user="root",password="Vini!123",database="hospital")
	cr=conn.cursor()
	cr.execute("select * from patient_reg_data")
	while True:
		row=cr.fetchone()
		if row is None:
			break;
		elif row[0]==Username and row[1]==Password:
			return render(request,'patient_home.html')
	return render(request,'patient_login.html')
	
def patient_home(request):
	return render(request,'patient_home.html')

def patient_logout(request):
	return render(request,'patient_login.html')
	
def patient_book_appointment(request):
	return render(request,'patient_book_appointment.html')

def contact(request):
	return render(request,'contact.html')
