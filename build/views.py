from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . forms import CreateUserForm


from .models import Question, Choice, Current_user

# Get questions and display them


	# check_voted = Current_user.objects.get_or_create(user = user'voted')
	#         video_data.objects.get_or_create(user_id = user, video_url= video_url)

	# USER = Current_user.objects.get_or_create('voted')
@login_required(login_url='/polls/login')
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:7]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)



#  Register

def register(request):
	if request.user.is_authenticated:
		return redirect("/polls")
	else:
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Sign Up Successful!')
			return redirect('/polls/login')
	context={'form': form}
	return render(request, "polls/register.html", context) 


# Login

def login_page (request):
    if request.user.is_authenticated:
        return redirect('/polls')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/polls')
            else:
                messages.info(request, 'Matric Number OR Password incorrect')

    context={}
    return render(request, "polls/login.html", context)
    

# Log out
def logout_user(request):
    logout(request)
    return redirect('/polls/login')





# Show specific question and choices

@login_required(login_url='/polls/login')
def detail(request, question_id):
	

	"""
	CHECKING TO SEE WHICH POSITION USER HAS VOTED FOR ALREADY SO THEY CAN NOT VOTE TWICE
	This was hectic!!!
	"""

	#GETTING OR CREATING A POLLS FOR USER BY DEFAULT
	Current_user.objects.get_or_create(user = request.user, id=request.user.id)

	if question_id == 1:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_2

	elif question_id == 2:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_2

	elif question_id == 3:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_3

	elif question_id == 4:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_4

	elif question_id == 5:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_5

	elif question_id == 6:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_6

	elif question_id == 7:
		check_voting_status = Current_user.objects.get(user = request.user, id=request.user.id).voted_position_7
	
	else: messages.info(request, "INFO: NO SUCH POSITION")
	


	if check_voting_status == True:
		messages.info(request, "INFO: You Have Already Casted A Vote For That Position!")
		return redirect('/polls')

	try:
		question = Question.objects.get(pk = question_id)
		print("IDDDDD", question_id)
	except Question.DoesNotExist:
		raise Http404("Question does not exist")
	else:
		print(str(request.method))

	return render(request, 'polls/detail.html', {'question': question, 'id': question_id})


# CONFIRM DECISION
def confirmation(request, question_id): 


	if request.method == "POST":
		print("Done!!!")
		if question_id == 1:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_1 = True
			change_voting_status.save()

		elif question_id == 2:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_2 = True
			change_voting_status.save()

		elif question_id == 3:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_3 = True
			change_voting_status.save()

		elif question_id == 4:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_4 = True
			change_voting_status.save()

		elif question_id == 5:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_5 = True
			change_voting_status.save()

		elif question_id == 6:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_6 = True
			change_voting_status.save()
		
		elif question_id == 7:
			change_voting_status = Current_user.objects.get(user = request.user, id=request.user.id)
			change_voting_status.voted_position_7 = True
			change_voting_status.save()
		
		else: messages.info(request, "INFO: NO SUCH POSITION")

		question = get_object_or_404(Question, pk = question_id)
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
		selected_choice.votes += 1
		selected_choice.save()
	
	
		messages.info(request, "Your Vote Has Been Recorded!")

		return redirect('/polls')

	return render(request, 'polls/confirmation.html')

# Get question and display results

@login_required(login_url='/polls/login')
def results(request, question_id):
	question = get_object_or_404(Question, pk = question_id)
	return render(request, 'polls/results.html', {'question': question})

# Vote for a question choice

@login_required(login_url='/polls/login')
def vote(request, question_id):
	# print(request.POST['choice'])
	question = get_object_or_404(Question, pk = question_id)
	try:
		selected_choice = question.choice_set.get(pk = request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))

def about(request):
	return render(request, 'polls/about.html')