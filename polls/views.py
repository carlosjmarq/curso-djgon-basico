from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question


# Create your views here.
def index(request):
	return HttpResponse("<h1>estas en la pagina principal de premios platzi app</h1>")


def detail(request, question_id):
	try:
		question = Question.objects.get(id=question_id)
		return HttpResponse('Estas viendo la pregunta numero {}\n\n{}'.format(question_id, question.question_text))
	except:
		return HttpResponse('ha ocurrido un error')

def results(request, question_id):
	return HttpResponse('Estas viendo los resultados de la pregunta numero {}'.format(question_id))


def vote(request, question_id):
	return HttpResponse('Estas votando a la pregunta {}'.format(question_id))