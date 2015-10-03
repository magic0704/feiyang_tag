from django.shortcuts import render

# Create your views here.
def home(request):
	#indexlist = ['a','b','c']
	#return render(request,'home.html',{'indexlist':indexlist})
	string = 'this is a dota test'
	string2 = 'this is a lol test'
	return render(request,'home.html',{'content1':string,'content2':string2})
