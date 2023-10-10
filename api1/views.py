from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
import os
from django.conf import settings
import json
from rest_framework import status
from django.views.static import serve
from django.http import HttpResponse
from line_profiler import LineProfiler
from django.core.cache import cache
from .throttle import PaidUserThrottle,UnpaidUserThrottle

profiler = LineProfiler()

data_zip = cache.get("zip_data")
data = cache.get('state_data')

class states_pin(APIView):
    throttle_classes = []
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def chcking_t(self,request):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            self.throttle_classes = [PaidUserThrottle]
        elif user.is_authenticated and not user.is_superuser:
            self.throttle_classes = [UnpaidUserThrottle]

        self.check_throttles(request)
        return True

    def get(self, request):
        check = self.chcking_t(request)
        print(check)
        states_data = []
        for values in data:
            states_data.append(values['state'])
        return Response(list(states_data),status=status.HTTP_200_OK)
    
    def post(self,request):
        check = self.chcking_t(request)
        search_str = request.data['state']
        if search_str == 'Choose...':
            data_a = {'not_state'}
            return Response(list(data_a), status=status.HTTP_200_OK)
        for v in data:
            if v['state'] == search_str:
                data_a = v['districts']
                break
        return Response(list(data_a),status=status.HTTP_200_OK)

@profiler
def Pin_dis(pin):
    data_res=[]
    for i in data_zip:
        if str(i["Pincode"])==pin:
            data_res.append(i["Office Name"])
            data_dist=i["District"]
            data_state=i["StateName"]
    return {"Data_c":data_res,"District":data_dist,'StateName':data_state,'Pincode':pin}

class ZipCode(APIView):
    throttle_classes = []
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def chcking_t(self,request):
        user = request.user
        if user.is_authenticated and user.is_superuser:
            self.throttle_classes = [PaidUserThrottle]
        elif user.is_authenticated and not user.is_superuser:
            self.throttle_classes = [UnpaidUserThrottle]

        self.check_throttles(request)
        return True

    def get(self,request):
        check = self.chcking_t(request)
        return Response({"you cannot get full data."},status=status.HTTP_200_OK)

    def post(self,request):
        check = self.chcking_t(request)
        zip_str = request.data['zip']
        a = Pin_dis(zip_str)
        profiler.print_stats()
        return Response(a,status=status.HTTP_200_OK)

def HomeTest(request):
    return render(request,'api1/index.html')


def ServerJavascript(request,token):
    base_path = os.path.join(settings.BASE_DIR,'api_scripts')
    js_path = os.path.join(base_path, 'states_pin.js')
    with open(js_path, 'r') as f:
        js_code = f.read()
    js_code = js_code.replace('{{ value }}',token)
    response = HttpResponse(js_code, content_type='application/javascript')
    return response
    # return serve(request,path=js_path,document_root=base_path)