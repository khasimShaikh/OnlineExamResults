from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
from datetime import date
import json
from web3 import Web3, HTTPProvider
from datetime import datetime

global username
global contract, web3
global usersList, studentList, start

#function to call contract
def getContract():
    global contract, web3
    blockchain_address = 'http://127.0.0.1:9545'
    web3 = Web3(HTTPProvider(blockchain_address))
    web3.eth.defaultAccount = web3.eth.accounts[0]
    compiled_contract_path = 'ExamContract.json' #ExamContract contract file
    deployed_contract_address = '0x3358Fd5432159A56a2f7aE03c8781d15f8A0aab0' #contract address
    with open(compiled_contract_path) as file:
        contract_json = json.load(file)  # load contract info as JSON
        contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
    file.close()
    contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
getContract()

def getUsersList():
    global usersList, contract
    usersList = []
    count = contract.functions.getUserCount().call()
    for i in range(0, count):
        user = contract.functions.getUsername(i).call()
        password = contract.functions.getPassword(i).call()
        usersList.append([user, password])

def getStudentList():
    global studentList, contract
    studentList = []
    count = contract.functions.getStudentCount().call()
    for i in range(0, count):
        sid = contract.functions.getStudentId(i).call()
        name = contract.functions.getName(i).call()
        first = contract.functions.getFirstQuestion(i).call()
        second = contract.functions.getSecondQuestion(i).call()
        third = contract.functions.getThirdQuestion(i).call()
        fourth = contract.functions.getFourthQuestion(i).call()
        fifth = contract.functions.getFifthQuestion(i).call()
        dd = contract.functions.getDate(i).call()
        time = contract.functions.getTime(i).call()
        grade = contract.functions.getGrade(i).call()
        studentList.append([sid, name, first, second, third, fourth, fifth, dd, time, grade])
        
getUsersList()
getStudentList()

def ViewStudents(request):
    if request.method == 'GET':
        global usersList
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Username</font></th>'
        output+='<th><font size=3 color=black>Password</font></th></tr>'
        for i in range(len(usersList)):
            plist = usersList[i]
            output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
            output+='<td><font size=3 color=black>'+plist[1]+'</font></td></tr>'            
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)   

def ViewGrades(request):
    if request.method == 'GET':
        global studentList
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Student ID</font></th>'
        output+='<th><font size=3 color=black>Student Name</font></th>'
        output+='<th><font size=3 color=black>First Question</font></th>'
        output+='<th><font size=3 color=black>Second Question</font></th>'
        output+='<th><font size=3 color=black>Third Question</font></th>'
        output+='<th><font size=3 color=black>Fourth Question</font></th>'
        output+='<th><font size=3 color=black>Fifth Question</font></th>'
        output+='<th><font size=3 color=black>Completed Date</font></th>'
        output+='<th><font size=3 color=black>Time Taken</font></th>'
        output+='<th><font size=3 color=black>Grade</font></th></tr>'
        for i in range(len(studentList)):
            plist = studentList[i]
            output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
            output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
            output+='<td><font size=3 color=black>'+plist[2]+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[4])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
            output+='<td><font size=3 color=black>'+str(plist[9])+'</font></td></tr>'
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)    

def CheckGrade(request):
    if request.method == 'GET':
        global username, studentList
        output = '<table border=1 align=center>'
        output+='<tr><th><font size=3 color=black>Student ID</font></th>'
        output+='<th><font size=3 color=black>Student Name</font></th>'
        output+='<th><font size=3 color=black>First Question</font></th>'
        output+='<th><font size=3 color=black>Second Question</font></th>'
        output+='<th><font size=3 color=black>Third Question</font></th>'
        output+='<th><font size=3 color=black>Fourth Question</font></th>'
        output+='<th><font size=3 color=black>Fifth Question</font></th>'
        output+='<th><font size=3 color=black>Completed Date</font></th>'
        output+='<th><font size=3 color=black>Time Taken</font></th>'
        output+='<th><font size=3 color=black>Grade</font></th></tr>'
        for i in range(len(studentList)):
            plist = studentList[i]
            if plist[1] == username:
                output+='<tr><td><font size=3 color=black>'+plist[0]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[1]+'</font></td>'
                output+='<td><font size=3 color=black>'+plist[2]+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[3])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[4])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[5])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[6])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[7])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[8])+'</font></td>'
                output+='<td><font size=3 color=black>'+str(plist[9])+'</font></td></tr>'
        output+="</table><br/><br/><br/><br/><br/><br/>"
        context= {'data':output}
        return render(request, 'StudentScreen.html', context)    

def WriteExamAction(request):
    if request.method == 'POST':
        global studentList, username, start
        q1 = request.POST.get('t1', False)
        q2 = request.POST.get('t2', False)
        q3 = request.POST.get('t3', False)
        q4 = request.POST.get('t4', False)
        q5 = request.POST.get('t5', False)
        print(q1+" "+q2+" "+q3+" "+q4+" "+q5)
        end = datetime.now()
        time_taken = end - start
        time_taken = time_taken.seconds
        count = contract.functions.getStudentCount().call()
        status = "none"
        grade = 0.0
        for i in range(len(studentList)):
            sl = studentList[i]
            if sl[1] == username:
                status = "You already wrote exam<br/>Your Previous Grade : "+str(sl[9])
                break
        if status == "none":
            if q1 == "C":
                grade += 1
                q1 = "1"
            else:
                q1 = "0"
            if q2 == "D":
                grade += 1
                q2 = "1"
            else:
                q2 = "0"
            if q3 == "B":
                grade += 1
                q3 = "1"
            else:
                q3 = "0"
            if q4 == "C":
                grade += 1
                q4 = "1"
            else:
                q4 = "0"
            if q5 == "A":
                grade += 1
                q5 = "1"
            else:
                q5 = "0"
            if grade > 0:
                grade = (grade / 5.0) * 100
            sid = len(studentList) + 1
            msg = contract.functions.createGrade(str(sid), username, q1, q2, q3, q4, q5, str(datetime.now()), str(time_taken), str(grade)).transact()
            tx_receipt = web3.eth.waitForTransactionReceipt(msg)
            studentList.append([str(sid), username, q1, q2, q3, q4, q5, str(datetime.now()), str(time_taken), str(grade)])
            status = "Your Grade = "+str(grade)+"<br/>"+str(tx_receipt)
        context= {'data':status}
        return render(request, 'StudentScreen.html', context)                

def WriteExam(request):
    if request.method == 'GET':
        global start, username
        status = ""
        page = "WriteExam.html"
        for i in range(len(studentList)):
            sl = studentList[i]
            if sl[1] == username:
                status = "You already wrote exam<br/>Your Previous Grade : "+str(sl[9])
                page = "StudentScreen.html"
                break
        start = datetime.now()    
        context= {'data':status}    
        return render(request, page, context) 
    
def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})    

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def StudentLogin(request):
    if request.method == 'GET':
       return render(request, 'StudentLogin.html', {})    
    
def Register(request):
    if request.method == 'GET':
       return render(request, 'Register.html', {})

def Signup(request):
    if request.method == 'POST':
        global usersList
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        phone = request.POST.get('contact', False)
        email = request.POST.get('email', False)
        address = request.POST.get('address', False)
        count = contract.functions.getUserCount().call()
        status = "none"
        for i in range(0, count):
            user1 = contract.functions.getUsername(i).call()
            if username == user1:
                status = "exists"
                break
        if status == "none":
            msg = contract.functions.createUser(username, password).transact()
            tx_receipt = web3.eth.waitForTransactionReceipt(msg)
            usersList.append([username, password])
            context= {'data':'Signup Process Completed<br/>'+str(tx_receipt)}
            return render(request, 'Register.html', context)
        else:
            context= {'data':'Given username already exists'}
            return render(request, 'Register.html', context)

def StudentLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        status = "StudentLogin.html"
        output = 'Invalid login details'
        for i in range(len(usersList)):
            ulist = usersList[i]
            print(ulist)
            user1 = ulist[0]
            pass1 = ulist[1]
            if user1 == username and pass1 == password:
                status = "StudentScreen.html"
                output = 'Welcome '+username
                break        
        context= {'data':output}
        return render(request, status, context)

def AdminLoginAction(request):
    if request.method == 'POST':
        global username, contract, usersList
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        status = "AdminLogin.html"
        output = 'Invalid login details'
        if username == "admin" and password == 'admin':
            status = "AdminScreen.html"
            output = 'Welcome '+username                  
        context= {'data':output}
        return render(request, status, context)

