from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from .models import Company, Investor
from .setget import CompanyPicks, calculate_revenue

company_pick = CompanyPicks()


def vc_invest(request):
    investor = Investor.objects.all()
    vc_investor = None
    if investor:
        for person in investor:
            if person.name == request.user.username:
                vc_investor = get_object_or_404(Investor, name=person.name)
                return render(request, '../VCTemplate/index.html', {'investor': vc_investor})
    return render(request, '../VCTemplate/index.html', {'investor': vc_investor})


def create_investor(request):
    if request.user:
        logout(request)
    if request.method == "POST":
        name = request.POST['name']
        country = request.POST['Country']
        firm = request.POST['Firm']
        user_list = User.objects.all()
        # user already exists
        for user in user_list:
            if user.username == name:
                login(request, user)
                return redirect('Investor:find_startup')
        Investor.objects.create(name=name, location=country, firm=firm)
        person = User.objects.create(username=name)
        login(request, person)
        return redirect('Investor:find_startup')
    else:
        return render(request, '../VCTemplate/create_investor.html')


def find_startup(request):
    investor = Investor.objects.all()
    vc_investor = None
    if investor:
        for person in investor:
            if person.name == request.user.username:
                vc_investor = get_object_or_404(Investor, name=person.name)
    if request.method == "POST":
        sector = request.POST['sector']
        location = request.POST['location']
        stage = request.POST['stage']
        valuation = request.POST['valuation']
        year = request.POST['year']
        revenue = request.POST['revenue']
        companies = Company.objects.all()
        picks = []
        for company in companies:
            if sector == "None" or sector == company.sector:
                if location == "None" or location == company.location:
                    if stage == "None" or company.stage == stage:
                        launch = 2021 - int(year)
                        if int(valuation) == 1000:
                            if company.valuation < int(valuation):
                                calculate_revenue(company, revenue, picks, launch)
                        elif int(valuation) == 3000:
                            if 1000 < company.valuation < int(valuation):
                                calculate_revenue(company, revenue, picks, launch)
                        elif int(valuation) == 12000:
                            if 3000 < company.valuation < int(valuation):
                                calculate_revenue(company, revenue, picks, launch)
        company_pick.setSelection(picks)
        return redirect('Investor:startup_list')
    else:
        return render(request, '../VCTemplate/find_startup.html', {'investor': vc_investor})


def startup_list(request):
    picks = company_pick.getSelection()
    if picks:
        return render(request, '../VCTemplate/startup_list.html', {'companies': picks})
    else:
        return render(request, '../VCTemplate/startup_list.html', {'companies': picks})


def about_startup(request, slug):
    company = get_object_or_404(Company, slug=slug)
    return render(request, '../VCTemplate/about_startup.html', {'company': company})