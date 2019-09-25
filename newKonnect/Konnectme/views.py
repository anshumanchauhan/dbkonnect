from django.shortcuts import render
import pymysql.cursors
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
class KonnectView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(KonnectView, self).dispatch(*args, **kwargs)
    def post(self, request):
        
        data=request.body
        print(data)
        data = json.loads(data)
        print(data)
        connection = pymysql.connect(database=data['database'],
                                         host=data['host'],
                                         port=data['port'],
                                         
                                         user=data['user'],
                                         password=data['password'],
                                         cursorclass=pymysql.cursors.DictCursor
                                         )
        try:                                 
            f=open(data['table'],"w+")
            

            cursor = connection.cursor()
            cursor.execute("USE employees")
            cursor.execute("SELECT emp_no,birth_date,first_name,last_name,gender,hire_date FROM employees LIMIT 10")
            result =cursor.fetchall() 
            data1 =[]
            for row in result:
                data1.append({'emp_no':row[0],'birth_date':row[1],'first_name':row[2],'last_name':row[3],'gender':row[4],'hire_date':row[5]})
                f.append(data1)         
                print(data1)
        
        finally:
            connection.close()
            print("MySQL connection is close d")

