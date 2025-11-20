from django.shortcuts import render

def index(request):
    dynamic=" Recent posts"
    post=[
        {'id':1,'post':'post 1','content':'This is post 1 content'},
        {'id':2,'post':'post 2','content':'This is post 2 content'},
        {'id':3,'post':'post 3','content':'This is post 3 content'},
        {'id':4,'post':'post 4','content':'This is post 4 content'}
    ]
    return render(request, 'index.html', {'dynamic': dynamic , 'post':post })   # Include app folder name
def detail(request,id):
    dynamic=" Recent posts"
    return render(request,'detail.html', {'dynamic': dynamic})