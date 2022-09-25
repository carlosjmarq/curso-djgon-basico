from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from polls.models import Question


# Create your views here.
def index(request):
	questions = Question.objects.all()
	return render(request, 'polls/index.html', {
		'lastest_question_list': questions
	})

def detail(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	return render(request, 'polls/detail.html', {
		'question': question
	})
	# try:
	# 	question = Question.objects.get(id=question_id)
	# 	return HttpResponse('Estas viendo la pregunta numero {}\n\n{}'.format(question_id, question.question_text))
	# except:
	# 	return HttpResponse('ha ocurrido un error')

def results(request, question_id):
	return HttpResponse('Estas viendo los resultados de la pregunta numero {}'.format(question_id))

def vote(request, question_id):
	return HttpResponse('Estas votando a la pregunta {}'.format(question_id))