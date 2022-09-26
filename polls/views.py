from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic


# Create your views here.
# def index(request):
# 	questions = Question.objects.all()
# 	return render(request, 'polls/index.html', {
# 		'lastest_question_list': questions
# 	})

# def detail(request, question_id):
# 	question = get_object_or_404(Question, id=question_id)
# 	return render(request, 'polls/detail.html', {
# 		'question': question
# 	})

# def results(request, question_id):
# 	question = get_object_or_404(Question, id=question_id)
# 	return render(request, 'polls/results.html', {
# 		"question": question
# 	})


class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'lastest_question_list'

	def get_queryset(self):
		# * return the five latest elements
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, id=question_id)
	try:
		selected_choice = question.choice_set.get(id=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
			"error_message": 'No has elegido una respuesta',
			"question": question
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=[question.id]))