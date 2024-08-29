#from django.shortcuts import render

#def home(request):
#    return render(request, 'resume/home.html')


from django.shortcuts import render

def resume_view(request):
    context = {
        'name': 'Fariba',
        'experience': [
            'Senior Engineer at ABC Corp (2020 - Present)',
            'Research Assistant at University of Sydney (2018 - 2020)'
        ],
        'education': [
            'PhD in Power Electronics, University of Technology Sydney (2024)',
            'Master of Engineering (Electrical), University of Sydney (2019)'
        ]
    }
    return render(request, 'index.html', context)

