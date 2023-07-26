from django.shortcuts import render
from django.http import HttpResponse
from myweb.models import Item
# Create your views here.
def index(request):
    data = Item.objects.all()
    print(data)
    return render(request, 'index.html', {'data':data})

def display(request):
    return render(request, 'index.html')

def template(request):
    msg = "Hello Template"
    person = {"name": "A", "age": 20}
    data = ["Stack", "Queue", "Deque", "LinkedList", "Tree"]
    # html에 데이터를 전송하고자 하면 세 번째 매개변수에 dict를 만들어서
    # 이름과 데이터를 기재함.
    return render(request, "template.html", {"message":msg,
                                             "person":person,
                                             "data":data})

def detail(request, itemid):
    item = Item.objects.get(itemid = itemid)
    return render(request, "detail.html", {"item":item})
