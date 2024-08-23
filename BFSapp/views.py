from django.shortcuts import render , redirect ,HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import EggMonitor
# from .models import Measurement

# Create your views here.
 
def user_login(request):
    context = {}
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/index')
        else:
            context = {
            "error": 'Email or Password are wrong.',
            }
            print("ERROR")
    return render(request, "login.html", context)

def index(request):
    return render(request, "index.html", {"name": request.POST.get("username")})

def check_user(request):
    print("*******************************************************")
    if request.method == "POST":
        if check_parameters(request.POST.get("email"), request.POST.get("password")):
            return render(request, "index.html", {"name": request.POST.get("username")})
        else:
            return render(request, "login.html",{})

def fill_eggs_monitor_form(request):
    if request.method == 'POST':
        # Retrieve data from the POST request and handle empty strings
        date_measure = request.POST.get('dateTime')
        cage_code = request.POST.get('cageCode')
        eggs_code = request.POST.get('eggsCode')
        
        egg_weight_1 = request.POST.get('weightEgg1') or None
        egg_weight_2 = request.POST.get('weightEgg2') or None
        egg_weight_3 = request.POST.get('weightEgg3') or None
        
        num_eggs_1 = request.POST.get('numberEggs1') or None
        num_eggs_2 = request.POST.get('numberEggs2') or None
        num_eggs_3 = request.POST.get('numberEggs3') or None
        
        total_eggs_weight = request.POST.get('total_eggs_weight') or None
        
        fertile_eggs_1 = request.POST.get('numberFertileEggs1') or None
        fertile_eggs_2 = request.POST.get('numberFertileEggs2') or None
        fertile_eggs_3 = request.POST.get('numberFertileEggs3') or None
        
        infertile_eggs_1 = request.POST.get('numberInfertileEggs1') or None
        infertile_eggs_2 = request.POST.get('numberInfertileEggs2') or None
        infertile_eggs_3 = request.POST.get('numberInfertileEggs3') or None
        
        target_density = request.POST.get('targetDensity') or None
        incubation_temp = request.POST.get('incubationTemp') or None
        incubation_tube = request.POST.get('incubationTube') or None
        
        # Calculating additional fields only if necessary
        if egg_weight_1 and egg_weight_2 and egg_weight_3:
            avg_single_weight = (float(egg_weight_1) + float(egg_weight_2) + float(egg_weight_3)) / 3
        else:
            avg_single_weight = None

        rsd_single_weight = 0.0  # Assuming 0.0 for now; adjust if needed

        if num_eggs_1 and num_eggs_2 and num_eggs_3 and fertile_eggs_1 and fertile_eggs_2 and fertile_eggs_3:
            fertelity_percentage = (
                (int(fertile_eggs_1) + int(fertile_eggs_2) + int(fertile_eggs_3))
                / (int(num_eggs_1) + int(num_eggs_2) + int(num_eggs_3))
            ) * 100
        else:
            fertelity_percentage = None

        rsd_fertelity_percentage = 0.0  # Assuming 0.0 for now; adjust if needed

        amount_of_added_eggs = 0.0  # Set this based on your logic
        comments = "No comments"  # You can retrieve this from a form field if necessary

        # Save the data to the database
        EggMonitor.objects.create(
            date_measure=date_measure,
            passed_hours=0.0,  # Set this based on your logic
            cage_code=cage_code,
            eggs_code=eggs_code,
            egg_weight_1=float(egg_weight_1) if egg_weight_1 else None,
            egg_weight_2=float(egg_weight_2) if egg_weight_2 else None,
            egg_weight_3=float(egg_weight_3) if egg_weight_3 else None,
            num_eggs_1=int(num_eggs_1) if num_eggs_1 else None,
            num_eggs_2=int(num_eggs_2) if num_eggs_2 else None,
            num_eggs_3=int(num_eggs_3) if num_eggs_3 else None,
            avg_single_weight=avg_single_weight,
            rsd_single_weight=rsd_single_weight,
            total_eggs_weight=int(total_eggs_weight) if total_eggs_weight else None,
            added_eggs=amount_of_added_eggs,
            fertile_eggs_1=int(fertile_eggs_1) if fertile_eggs_1 else None,
            fertile_eggs_2=int(fertile_eggs_2) if fertile_eggs_2 else None,
            fertile_eggs_3=int(fertile_eggs_3) if fertile_eggs_3 else None,
            infertile_eggs_1=int(infertile_eggs_1) if infertile_eggs_1 else None,
            infertile_eggs_2=int(infertile_eggs_2) if infertile_eggs_2 else None,
            infertile_eggs_3=int(infertile_eggs_3) if infertile_eggs_3 else None,
            fertelity_percentage=fertelity_percentage,
            rsd_fertelity_percentage=rsd_fertelity_percentage,
            target_density=int(target_density) if target_density else None,
            amount_of_added_eggs=amount_of_added_eggs,
            incubation_temp=incubation_temp,
            incubation_tube=incubation_tube,
            comments=comments
        )

        # Redirect to a success page or return a success message
        return HttpResponse("Data inserted successfully")

    # If GET request, just render the form
    return render(request, "eggsMonitorForm.html", {})

def get_table1(request):
    all_eggs_monitors = EggMonitor.objects.get_queryset()
    return render(request, "table1.html",{})

def get_table1(request):
    # Fetch all records from the EggMonitor model
    all_eggs_monitors = EggMonitor.objects.all()
    data = []

    for item in all_eggs_monitors:
        # Create a dictionary for each row, mapping your model fields to table columns
        row_dict = {
            'col1': item.date_measure,
            'col2': item.cage_code,
            'col3': item.eggs_code,
            'col4': item.egg_weight_1,
            'col5': item.egg_weight_2,
            'col6': item.egg_weight_3,
            'col7': item.num_eggs_1,
            'col8': item.num_eggs_2,
            'col9': item.num_eggs_3,
            'col10': item.avg_single_weight,
            'col11': item.rsd_single_weight,
            'col12': item.total_eggs_weight,
            'col13': item.added_eggs,
            'col14': item.fertile_eggs_1,
            'col15': item.fertile_eggs_2,
            'col16': item.fertile_eggs_3,
            'col17': item.infertile_eggs_1,
            'col18': item.infertile_eggs_2,
            'col19': item.infertile_eggs_3,
            'col20': item.fertelity_percentage,
            'col21': item.rsd_fertelity_percentage,
            'col22': item.target_density,
            'col23': item.amount_of_added_eggs,
            'col24': item.incubation_temp,
            'col25': item.incubation_tube,
            'col26': item.comments,
        }
        # Append the row dictionary to the data list
        data.append(row_dict)

    # Render the data in the template
    return render(request, 'table1.html', {'data_from_server': data})

def filter_view(request):
    # Handle user input for filtering
    filter_option = request.GET.get('filter_option', '')  # Get the selected filter option from the query string
    
    queryset = []

    # Apply filtering based on the selected option
    if filter_option == 'cycle':
        queryset = Measurement.objects.filter(cycle=request.GET.get('filter_text'))
    elif filter_option == 'diet':
        queryset = Measurement.objects.filter(diet=request.GET.get('filter_text'))
    elif filter_option == 'temperature':
        queryset = Measurement.objects.filter(temperature=request.GET.get('filter_text'))
    elif filter_option == 'date':
        queryset = Measurement.objects.filter(date=request.GET.get('filter_text'))
    elif filter_option == 'larvae_weight':
        queryset = Measurement.objects.filter(larvae_weight=request.GET.get('filter_text'))
    else:
        queryset = Measurement.objects.all()

    data = []

    if queryset.__len__() > 0:
        for item in queryset:
            row_dict = {
                'col1': item.cycle,
                'col2': item.diet,
                'col3': item.date,
                'col4': item.temperature,
                'col5': item.larvae_weight,
                'col6': item.before_dry,
                'col7': item.after_dry,
            }
            data.append(row_dict)

    return render(request, 'filter.html', {'data_from_server': data})
