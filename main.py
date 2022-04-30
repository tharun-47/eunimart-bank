from flask import Blueprint, Flask, render_template,request, session, redirect, url_for, render_template, flash,jsonify

from flask import Flask, render_template, redirect, request, session
from flask_session import Session
from flask_cors import CORS as cors
from flask_session import Session
import random

import psycopg2
import psycopg2.extras

app=Flask(__name__, template_folder='templates')
app.secret_key = 'eunimart'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
cors(app)


def insertUser(countryCode,mobileNumber,firstName,lastName,fatherName,dob,permanentAddress,currentAddress,accNum,pin):
    hostname = 'localhost'
    database = 'bank_details'
    username = 'postgres'
    pwd = '12345'
    port_id = 5432
    conn = None
    result = 0

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                insert_script = "INSERT INTO account_holder(country_code,mobile_num,first_name,last_name,father_name,dob,permanent_address,current_address,account_num,pin)VALUES ('%s', '%s', '%s', '%s','%s', Date '%s','%s', '%s', '%s', '%s')"
                insert_values = [(countryCode, mobileNumber, firstName, lastName, fatherName, dob,permanentAddress,currentAddress,accNum,pin)]

                for record in insert_values:

                    if (cur.execute(insert_script% record) == None):
                        result = 1
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return result


def getaccountnumber():
    hostname = 'localhost'
    database = 'bank_details'
    username = 'postgres'
    pwd = '12345'
    port_id = 5432
    conn = None
    result = -1

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(
                    "SELECT account_num FROM account_holder ORDER BY account_num DESC LIMIT 1;")
                data = cur.fetchall()
                if (len(data) > 0):
                    result = str(int(data[0][0])+1)
                else:
                    result = 1



    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return result



def checkExistingUser(mobileNum):
    hostname = 'localhost'
    database = 'bank_details'
    username = 'postgres'
    pwd = '12345'
    port_id = 5432
    conn = None
    result = -1

    try:
        with psycopg2.connect(
                host=hostname,
                dbname=database,
                user=username,
                password=pwd,
                port=port_id) as conn:

            with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
                cur.execute(
                    "SELECT mobile_num FROM account_holder WHERE mobile_num='" + mobileNum + "';")
                data = cur.fetchall()



                if (len(data) > 0):
                    result = 0
                else:
                    result = 1
    except Exception as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return result


@app.route('/signup',methods=['GET','POST'])
def signup():
    data={}
    data['countryCode']=str(request.args['countryCode'])
    data['mobileNum'] = str(request.args['mobileNum'])
    data['firstName']=str(request.args['firstName'])
    data['lastName']=str(request.args['lastName'])

    flag = checkExistingUser(data['mobileNum'])
    print(flag)


    if flag==1:
        return '1'
    elif flag == 0:
        return '0'
    else:
        return '2'

@app.route('/createAccount',methods=['GET','POST'])
def createAccount():
    data={}
    data['countryCode']=str(request.args['countryCode'])
    data['mobileNum'] = str(request.args['mobileNum'])
    data['firstName']=str(request.args['firstName'])
    data['lastName']=str(request.args['lastName'])
    data['fatherName'] = str(request.args['fatherName'])
    data['dob'] = str(request.args['dob'])
    data['permanentAddress'] = str(request.args['permanentAddress'])
    data['currentAddress'] = str(request.args['currentAddress'])

    userMobileNumber = data['mobileNum'][-10:]

    userAccountNumber = getaccountnumber()
    pin = random.randint(0, 999999)

    flag=insertUser(data['countryCode'],data['mobileNum'],data['firstName'],data['lastName'],data['fatherName'],data['dob'],data['permanentAddress'],data['currentAddress'],userAccountNumber,pin)
    if flag==1:
        return 'Account created with account number: %s and pin : %s'%(userAccountNumber,pin)
    else:
        return 'Something went wrong'
    return str(flag)




@app.route('/')
def index():
    return "Index"




if __name__ == '__main__':
   app.run(debug=True,port=5500)
