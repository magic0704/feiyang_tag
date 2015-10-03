from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
	string = "this is a tag test"
	taglist = ['dota','lol','war3','EVA','CVD','zhibo']
	#taglist = map(str,range(100))
	return render(request,'index.html',{'taglist':taglist})
def submittag(request):
	request.encoding='utf-8'
	#return HttpResponse(request.GET['q'])
	#message = request.GET['q'] 
	#message = request.GET['favcolor1'].encode('utf-8') +  request.GET['favcolor2'] +  request.GET['favcolor3']
	message = []
	if 'tag1' in request.GET:
		message1 = request.GET['tag1'] 
		message.append(message1)
	if 'tag2' in request.GET:
		message2 = request.GET['tag2'] 
		message.append(message2)
	if 'tag3' in request.GET:
		message3 = request.GET['tag3'] 
		message.append(message3)
#	else:
#		return render(request,'result.html','you should choose at least one')
	message4 = "this is a string"
	#return render(request,'result.html',{'list1':message})
	#return render(request,'result.html',{'list1':message})
	#return HttpResponse(message1)
	return render(request,'result.html',{'list1':message})
