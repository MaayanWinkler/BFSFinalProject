from django.shortcuts import render , redirect ,HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import EggMonitor , RearingMonitor, BreedMonitor
from datetime import datetime

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
        # return HttpResponse("Data inserted successfully")

    # If GET request, just render the form
    return render(request, "forms/eggsMonitorForm.html", {})

def fill_rearing_monitor_form(request):
    if request.method == 'POST':
        print (request.POST)
        # Retrieve data from the POST request and handle empty strings
        crate_code = request.POST.get('crateCode')
        eggs_code = request.POST.get('eggsCode')
        starter_date = request.POST.get('starterDate')
        starter_size = request.POST.get('starterSize')
        starter_diet = request.POST.get('starterDiet')
        diet_type = request.POST.get('dietType')
        
        consortium = request.POST.get('consortium') or None
        cycle = request.POST.get('cycle') or None
        box = request.POST.get('box') or None
        goal = request.POST.get('goal') or None
        length_measure_date = request.POST.get('lengthMeasureDate') or None
        average_length = request.POST.get('averageLength') or None
        cooking_date = request.POST.get('cookingDate') or None
        measure_date = request.POST.get('measureDate') or None
        temp = request.POST.get('temp') or None
        total_larvae_weight = request.POST.get('totalLarvaeWeight') or None
        number_of_larvae_sampled = request.POST.get('numberOfLarvaeSampled') or None
        pupation = request.POST.get('pupation') or None
        substrate_before_drying = request.POST.get('substrateBeforeDrying') or None
        substrate_after_drying = request.POST.get('substrateAfterDrying') or None
        harvest_date = request.POST.get('harvestDate') or None
        total_pupae_weight = request.POST.get('totalPupaeWeight') or None
        larvae_weight = request.POST.get('larvaeWeight') or None
        number_of_larvae_pupae_sampled = request.POST.get('numberOfLarvaePupaeSampled') or None
        cage_code = request.POST.get('cageCode') or None

        # Calculating additional fields only if necessary
        if starter_date and length_measure_date:
            date_format = "%Y-%m-%dT%H:%M"  # Adjust format to match your date string format (e.g., "2023-08-23")
            date1 = datetime.strptime(starter_date, date_format)
            date2 = datetime.strptime(length_measure_date, date_format)

            delta = date2 - date1
            starter_age = delta.days
        else:
            starter_age = None

        if total_larvae_weight and number_of_larvae_sampled:
            single_larva_weight = (float(total_larvae_weight) / float(number_of_larvae_sampled))
        else:
            single_larva_weight = None

        if harvest_date and starter_date:
            date_format = "%Y-%m-%dT%H:%M"  # Adjust format to match your date string format (e.g., "2023-08-23")
            date1 = datetime.strptime(harvest_date, date_format)
            date2 = datetime.strptime(starter_date, date_format)

            delta = date2 - date1
            days_from_laying = delta.days
        else:
            days_from_laying = None

        if harvest_date and cooking_date:
            date_format = "%Y-%m-%dT%H:%M"  # Adjust format to match your date string format (e.g., "2023-08-23")
            date1 = datetime.strptime(harvest_date, date_format)
            date2 = datetime.strptime(cooking_date, date_format)

            delta = date2 - date1
            days_from_cooking = delta.days
        else:
            days_from_cooking = None

        if larvae_weight and number_of_larvae_pupae_sampled:
            single_larvae_pupae_weight = 1000 * (float(larvae_weight) / float(number_of_larvae_pupae_sampled))
        else:
            single_larvae_pupae_weight = None
        
        if total_pupae_weight and single_larvae_pupae_weight:
            total_larvae_count = (float(larvae_weight) / (float(number_of_larvae_pupae_sampled) / 1000000 ))
        else:
            total_larvae_count = None

        if total_larvae_count:
            survival_percentage = 100 * (float(total_larvae_count) / 8000)
        else:
            survival_percentage = None
        

        comments = "No comments"  # You can retrieve this from a form field if necessary


        # Retrieve the EggMonitor instance
        try:
            eggs_code_instance = EggMonitor.objects.get(eggs_code = int(eggs_code))
        except EggMonitor.DoesNotExist:
            eggs_code_instance = None  # Handle the case where the instance does not exist
            return HttpResponse("EggMonitor instance not found :(")


        # Save the data to the database
        RearingMonitor.objects.create(
            crate_code=crate_code,
            consortium_entoprotech_breeding=consortium,
            cycle=int(cycle) if cycle else None,
            box=int(box) if box else None,
            goal=goal,
            eggs_code=eggs_code_instance,  # Ensure eggs_code is an EggMonitor instance
            starter_date=starter_date,
            starter_size=int(starter_size) if starter_size else None,
            starter_diet=starter_diet,
            length_measure_date=length_measure_date,
            average_length=float(average_length) if average_length else None,
            starter_age=starter_age,
            cooking_date=cooking_date,
            diet_type=diet_type,
            measure_date=measure_date,
            temperature=float(temp) if temp else None,
            total_larvae_weight=int(total_larvae_weight) if total_larvae_weight else None,
            number_of_larvae_sampled=int(number_of_larvae_sampled) if number_of_larvae_sampled else None,
            single_larva_weight=int(single_larva_weight) if single_larva_weight else None,
            pupation_percentage=float(pupation) if pupation else None,
            substrate_before_drying=float(substrate_before_drying) if substrate_before_drying else None,
            substrate_after_drying=float(substrate_after_drying) if substrate_after_drying else None,
            harvest_date=harvest_date,
            days_from_laying=days_from_laying,
            days_from_cooking=days_from_cooking,
            total_pupae_larvae_weight=float(total_pupae_weight) if total_pupae_weight else None,
            larvae_pupae_weight=float(larvae_weight) if larvae_weight else None,
            number_of_larvae_pupae_sampled=int(number_of_larvae_pupae_sampled) if number_of_larvae_pupae_sampled else None,
            single_larvae_pupae_weight=int(single_larvae_pupae_weight) if single_larvae_pupae_weight else None,
            total_larvae_count=int(total_larvae_count) if total_larvae_count else None,
            survival_percentage=int(survival_percentage) if survival_percentage else None,
            cage_code=cage_code,
            comments=comments
        )

        # Redirect to a success page or return a success message
        # return HttpResponse("Data inserted successfully")

    # If GET request, just render the form
    return render(request, "forms/rearingMonitorForm.html", {})

def fill_breeding_monitor_form(request):
    if request.method == 'POST':
        # Retrieve data from the POST request and handle empty strings
        crate_code = request.POST.get('crate-code')
        cage_code = request.POST.get('cage-code')
        cage_date = request.POST.get('cage-date')
        goal = request.POST.get('goal') or None
        cage_geometry = request.POST.get('cage-geometry') or None
        target_density = request.POST.get('target-density')
        amount_of_eggis = request.POST.get('amount-of-eggis') or None
        hydrogel_surface_area = request.POST.get('hydrogel-surface-area') or None
        attractant_container_volume_recipe = request.POST.get('attractant-container-volume-recipe') or None
        first_emergence_date = request.POST.get('first-emergence-date') or None
        comments = request.POST.get('comments') or None

        ##
        try:
            rearing_obj = RearingMonitor.objects.get(cage_code=cage_code)
        except MyModel.DoesNotExist:
            rearing_obj = None

        if cage_geometry and target_density and rearing_obj.single_larvae_pupae_weight:
            pupae = (float(cage_geometry) * float(target_density)) * float(rearing_obj.single_larvae_pupae_weight) / 1000
        else:
            pupae = None
        ##

        if first_emergence_date and cage_date:
            date_format = "%Y-%m-%dT%H:%M"  # Adjust format to match your date string format (e.g., "2023-08-23")
            date1 = datetime.strptime(first_emergence_date, date_format)
            date2 = datetime.strptime(cage_date, date_format)

            delta = date2 - date1
            days_from_cage_date = delta.days
        else:
            days_from_cage_date = None

        # Retrieve the EggMonitor instance
        try:
            crate_code_instance = RearingMonitor.objects.get(crate_code = int(crate_code))
            cage_code_instance = RearingMonitor.objects.get(cage_code = int(cage_code))

        except RearingMonitor.DoesNotExist:
            crate_code_instance = None  # Handle the case where the instance does not exist

            return HttpResponse("RearingMonitor instance not found :(")

        print (days_from_cage_date)
        BreedMonitor.objects.create(
            crate_code = crate_code_instance,
            harvest_date = crate_code_instance.harvest_date if crate_code_instance.harvest_date else None,
            single_larvae = float(crate_code_instance.single_larvae_pupae_weight) if crate_code_instance.single_larvae_pupae_weight else None,
            starter_date = crate_code_instance.starter_date if crate_code_instance.starter_date else None,
            cage_code = cage_code_instance,
            cage_date = cage_date,
            goal = goal if goal else None,
            cage_geometry = float(cage_geometry) if cage_geometry else None,  # Ensure eggs_code is an EggMonitor instance
            target_density = int(target_density),
            pupae = float(pupae) if pupae else None,
            amount_of_eggs = int(amount_of_eggis) if amount_of_eggis else None,
            hydrogel_surface = hydrogel_surface_area if hydrogel_surface_area else None,
            attractant = attractant_container_volume_recipe if attractant_container_volume_recipe else None,
            first_emergence_date = first_emergence_date if first_emergence_date else None,
            peak_daily = None,
            total_eggs_harvest = None,
            avg_oviposition = None,
            oviposition = None,
            mg_eggs_female = None,
            num_eggs_female = None,
            avg_fertility = None,
            num_clutches = None,
            num_females = None,
            from_hatch_to_emer_days = None,
            days_from_cage_date = days_from_cage_date if days_from_cage_date else None,
            days_from_egg_placement = None,
            days_for_first_egg_from_emer = None,
            comments=comments
        )

        # Redirect to a success page or return a success message
        # return HttpResponse("Data inserted successfully")

    # If GET request, just render the form
    return render(request, "forms/breedingMonitorForm.html", {})

def get_egg_monitor_table(request):
    all_eggs_monitors = EggMonitor.objects.get_queryset()
    return render(request, "tables/eggMonitorTable.html",{})

def get_egg_monitor_table(request):
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
    return render(request, 'tables/eggMonitorTable.html', {'data_from_server': data})

def get_rearing_monitor_table(request):
    all_rearing_monitors = RearingMonitor.objects.get_queryset()
    return render(request, "tables/rearingMonitorTable.html",{})

def get_rearing_monitor_table(request):
    # Fetch all records from the EggMonitor model
    all_rearing_monitors = RearingMonitor.objects.all()
    data = []

    for item in all_rearing_monitors:
        # Create a dictionary for each row, mapping your model fields to table columns
        row_dict = {
            'col1': item.crate_code,
            'col2': item.consortium_entoprotech_breeding,
            'col3': item.cycle,
            'col4': item.box,
            'col5': item.goal,
            'col6': item.eggs_code,
            'col7': item.starter_date,
            'col8': item.starter_size,
            'col9': item.starter_diet,
            'col10': item.length_measure_date,
            'col11': item.average_length,
            'col12': item.starter_age,
            'col13': item.cooking_date,
            'col14': item.diet_type,
            'col15': item.measure_date,
            'col16': item.temperature,
            'col17': item.total_larvae_weight,
            'col18': item.number_of_larvae_sampled,
            'col19': item.single_larva_weight,
            'col20': item.pupation_percentage,
            'col21': item.substrate_before_drying,
            'col22': item.substrate_after_drying,
            'col23': item.harvest_date,
            'col24': item.days_from_laying,
            'col25': item.days_from_cooking,
            'col26': item.total_pupae_larvae_weight,
            'col27': item.larvae_pupae_weight,
            'col28': item.number_of_larvae_pupae_sampled,
            'col29': item.single_larvae_pupae_weight,
            'col30': item.total_larvae_count,
            'col31': item.survival_percentage,
            'col32': item.cage_code,
            'col33': item.comments,
        }
        # Append the row dictionary to the data list
        data.append(row_dict)

    # Render the data in the template
    return render(request, 'tables/rearingMonitorTable.html', {'data_from_server': data})

def get_breeding_monitor_table(request):
    console.log("#######################")
    all_breeding_monitors = BreedMonitor.objects.get_queryset()
    return render(request, "tables/breedingMonitorTable.html",{})

def get_breeding_monitor_table(request):
    all_breeding_monitors = BreedMonitor.objects.all()
    data = []

    for item in all_breeding_monitors:
        # Create a dictionary for each row, mapping your model fields to table columns
        row_dict = {
            'col1': item.crate_code,  # crate_code
            'col2': item.harvest_date,  # harvest_date
            'col3': item.single_larvae,  # single_larvae
            'col4': item.starter_date,  # starter_date
            'col5': item.cage_code,  # cage_code
            'col6': item.cage_date,  # cage_date
            'col7': item.goal,  # goal
            'col8': item.cage_geometry,  # cage_geometry
            'col9': item.target_density,  # target_density
            'col10': item.pupae,  # pupae
            'col11': item.amount_of_eggs,  # amount_of_eggs
            'col12': item.hydrogel_surface,  # hydrogel_surface
            'col13': item.attractant,  # attractant
            'col14': item.first_emergence_date,  # first_emergence_date
            'col15': item.peak_daily,  # peak_daily
            'col16': item.total_eggs_harvest,  # total_eggs_harvest
            'col17': item.avg_oviposition,  # avg_oviposition
            'col18': item.oviposition,  # oviposition
            'col19': item.mg_eggs_female,  # mg_eggs_female
            'col20': item.num_eggs_female,  # num_eggs_female
            'col21': item.avg_fertility,  # avg_fertility
            'col22': item.num_clutches,  # num_clutches
            'col23': item.num_females,  # num_females
            'col24': item.from_hatch_to_emer_days,  # from_hatch_to_emer_days
            'col25': item.days_from_cage_date,  # days_from_cage_date
            'col26': item.days_from_egg_placement,  # days_from_egg_placement
            'col27': item.days_for_first_egg_from_emer,  # days_for_first_egg_from_emer
            'col28': item.comments,  # comments
        }
        # Append the row dictionary to the data list
        data.append(row_dict)

    # Render the data in the template
    return render(request, 'tables/breedingMonitorTable.html', {'data_from_server': data})