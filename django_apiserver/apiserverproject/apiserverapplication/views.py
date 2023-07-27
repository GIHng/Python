from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import BookSerializer
from .models import Book


# Create your views here.
# GET 요청만 처리함.
@api_view(['GET'])
def helloAPI(request):
    return Response("HELLO REST API")


@api_view(['POST', 'GET'])
def booksAPI(request):

    if request.method == 'GET':
        books = Book.objects.all()
        serialzer = BookSerializer(books, many=True)

        return Response(serialzer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        # 클라이언트가 전송한 데이터를 Model이 사용할 수 있는 데이터로 변환
        serializer = BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()  # 데이터 저장
            # 성공했을 때 전송한 데이터를 다시 전송
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패했을 때 처리.
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework.generics import get_object_or_404

@api_view(['GET'])
def bookAPI(request,bid):
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)

def ajax(request):
    return render(request,"ajax.html")