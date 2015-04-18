from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from .models import Article,Comment

# Create your views here.
def articles(request):
	return render_to_response('article_view.html',{'articles':Article.objects.all()})

def article(request, article_id = 1):
	return render_to_response('article_deatil.html',{'article':Article.objects.get(id = article_id)})

def search(request):
	errors = []
	if 'search' in request.GET and request.GET['search']:
		search = request.GET['search']
				
		article = Article.objects.filter(title__icontains = search)
		return render(request,'search_results.html',{'article':article,'query':search})
	else:	
		if  len('search'):
			errors.append('Enter a search term.')	
		elif len('search') > 20:
			errors.append('Please enter at most 20 characters.')		
		return render(request, 'search_form.html',{'errors': errors})
	
