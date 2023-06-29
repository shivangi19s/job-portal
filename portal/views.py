from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import JobPosting, Resume
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


@login_required(redirect_field_name="home")
def applicant(request):
    return render(request, "applicant.html")


@login_required(redirect_field_name="home")
def recruiter(request):
    return render(request, "recruiter.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = first_name
        myuser.last_name = last_name

        myuser.save()
        return redirect('home')


def rec_signin(request):
    if request.method == 'POST':
        loguser = request.POST['loguser']
        logpass = request.POST['logpass']

        myuser = authenticate(username=loguser, password=logpass)

        if myuser is not None:
            login(request, myuser)
            return redirect('recruiter')
        else:
            return redirect('home')


def app_signin(request):
    if request.method == 'POST':
        loguser = request.POST['loguser']
        logpass = request.POST['logpass']

        myuser = authenticate(username=loguser, password=logpass)

        if myuser is not None:
            login(request, myuser)
            return redirect('applicant')
        else:
            return redirect('home')


def signout(request):
    logout(request)
    return redirect('home')


@login_required(redirect_field_name="home")
def postjob(request):
    if request.method == 'POST':
        post = JobPosting()
        post.user_id = request.user
        post.company = request.POST['company']
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.skills = request.POST['skills']
        post.location = request.POST['location']
        post.save()

        return redirect('myjob')

    else:
        return redirect('recruiter')


@login_required(redirect_field_name="home")
def myjob(request):
    user = request.user
    user_jobs = JobPosting.objects.filter(user_id=user.id).order_by('-id')

    paginator = Paginator(user_jobs, 2)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    last_page = paginator.num_pages - 1

    return render(request, 'myjob.html', {'jobs': jobs, 'last_page': last_page})


@login_required(redirect_field_name="home")
def viewjob(request):
    job = JobPosting.objects.all()

    paginator = Paginator(job, 2)
    page_number = request.GET.get('page')
    jobs = paginator.get_page(page_number)

    last_page = paginator.num_pages - 1
    return render(request, 'viewjob.html', {'jobs': jobs, 'last_page': last_page})


def delete_job(request):
    job_id = request.GET.get('job_id')

    try:
        job = JobPosting.objects.get(id=job_id)
        job.delete()
        return redirect('myjob')
    except JobPosting.DoesNotExist:
        return redirect('myjob')


def edit_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)

    if request.method == 'POST':
        job.company = request.POST['company']
        job.title = request.POST['title']
        job.description = request.POST['description']
        job.skills = request.POST['skills']
        job.location = request.POST['location']
        job.save()
        return redirect('myjob')

    return render(request, 'myjob.html', {'job': job})


@login_required(redirect_field_name="home")
def view_application(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)
    applications = Resume.objects.filter(job_id=job)

    context = {
        'job': job,
        'applications': applications
    }

    return render(request, 'application.html', context)


def apply_job(request):
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        applicant_id = request.user
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        resume = request.FILES.get('resume')
        why = request.POST.get('why')

        job = get_object_or_404(JobPosting, id=job_id)

        resume_obj = Resume(applicant_id=applicant_id, job_id=job, full_name=full_name, email=email, resume=resume, why=why)
        resume_obj.save()

        return redirect('viewjob')

    return render(request, 'applicant.html')


