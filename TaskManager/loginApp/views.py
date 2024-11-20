

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from loginApp.models import UserRegisterTable
from loginApp import serializers






class RegisterAPI(APIView):
    
    def post(self, request):
      
     try: 
        print("Request Data:", request.data)
        serializer =serializers.RegisterSerializer(data=request.data)
        if serializer.is_valid():
            print("Validated Data:", serializer.validated_data) 
            serializer.save()
            return Response({"message": "User registered successfully.","data":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     except Exception as e:
          return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Normal serializers -----------
# class RegisterAPI(APIView):
#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)

#         if serializer.is_valid():
#             # Manually save the data to the model
#             user_data = serializer.validated_data
#             UserRegisterTable.objects.create(
#                 name=user_data['name'],
#                 email=user_data['email'],
#                 password=user_data['password']
#             )
#             return Response({
#                 "message": "User registered successfully.",
#                 "data": serializer.data
#             }, status=status.HTTP_201_CREATED)

#         return Response({
#             "message": "Validation failed",
#             "errors": serializer.errors
#         }, status=status.HTTP_400_BAD_REQUEST)