from watchlist.models import Watchlist,Streamplatform
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from watchlist.api.serializers import WatchlistSerializer,Streamserializer
from rest_framework import status
from rest_framework.views import APIView

class streamplatformAV(APIView):
    def get(self,request):
        platform=Streamplatform.objects.all()
        serializer=Streamserializer(platform,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = Streamserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class streamplatformdetailAV(APIView):
    def get(self,request,pk):
        try:
            platform=Streamplatform.objects.get(pk=pk)
        except Streamplatform.DoesNotExist:
            return Response({'ERROR':'STREAMING PLATFORM DOESNT EXIST'},status=status.HTTP_404_NOT_FOUND)
        serializer=Streamserializer(platform)
        return Response(serializer.data)
    def put(self,request,pk):
        platform=Streamplatform.objects.get(pk=pk)
        serializer=Streamserializer(platform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self,request,pk):
        platform=Streamplatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchlistAV(APIView):
    def get(self,request):
        movies=Watchlist.objects.all()
        serializers=WatchlistSerializer(movies, many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers=WatchlistSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
class WatchdetailsAV(APIView):
    def get(self,request,pk):
        try:
            movies=  Watchlist.objects.get(pk=pk)
        except  Watchlist.DoesNotExist:
            return Response({'ERROR':'Movie not found'},status=status.HTTP_400_BAD_REQUEST)
        serializers=WatchlistSerializer(movies)
        return Response(serializers.data)

    def put(self,request,pk):
        movies= Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status = status.HTTP_200_OK)  
    def delete(self,request,pk):
        movies= Watchlist.objects.get(pk=pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        






# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method =='GET':
#         movies=Movie.objects.all()
#         serializers=MovieSerializer(movies,many=True)
#         return Response(serializers.data)
#     elif request.method =='POST':
#         serializers=MovieSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.error)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,pk):
    
#     if request.method == 'GET':
#         movies=Movie.objects.get(pk=pk)
#         serializers=MovieSerializer(movies)
#         return Response(serializers.data)
    
#     if request.method == 'PUT':
#         movies=Movie.objects.get(pk=pk)
#         serializers= MovieSerializer(movies,data=request.data)  
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.error)  
    
#     if request.method == 'DELETE':
#         movies=Movie.objects.get(pk=pk)
#         movies.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        


   



    

    
    
    






