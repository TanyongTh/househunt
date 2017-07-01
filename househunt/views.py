import requests
from django.shortcuts import render
from .models import Property
from .forms import ScrapingForm, SearchForm
from django.utils import timezone
from .functions import scrapingdata, chk_duplicate_data, insert_prop, search_prop
from django.core.cache import cache
from django.contrib import messages
# from django.shortcuts import render_to_response
from django.shortcuts import render


# Create your views here.
def index(request):
    form = ScrapingForm()
    return render(request, 'househunt/index.html', {'form': form})

def housescraping(request):
    form = ScrapingForm()
    msg="default"

    if request.method == "POST":
        form = ScrapingForm(request.POST)
        if '_btnget' in request.POST:
            if form.is_valid():
                result = scrapingdata(form)
                search_result = result[0][0][0]
                cache.set('s1', result, 5)  # ('Key', 'Value', 'Timeout')
                return render(request, 'househunt/property_list.html',
                              {'form': form, 'list': result, 'search_result': search_result})
            else:
                return render(request, 'househunt/property_scraping.html', {'form': form})

        elif '_btnsave' in request.POST:
            result = cache.get('s1')
            if result:
                for row in result:
                    for i in range(0, len(row)):
                        prop_id = row[i][2]
                        postcode = row[i][5]

                        if chk_duplicate_data(prop_id, postcode) == 0:  #duplicated=1, empty=0
                            msg = insert_prop(row, i)

                form = ScrapingForm()
                # messages.add_message(request, messages.INFO, 'Yeehaw!')
                messages.success(request, 'Record was updated successfully!')
                return render(request, 'househunt/index.html', {'form': form})

    return render(request, 'househunt/index.html', {'form': form})

def property_search(request):
    records=""
    # houses = House.objects.filter(listed_date=timezone.now()).order_by('propertyID')
    form = SearchForm()
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            records = search_prop(str(form.cleaned_data['postcode']), str(form.cleaned_data['address']))
            
            if str(records) !="":
                result = len(records)
            else:
                result=0
            #properties = Property.objects.filter(postcode=form.cleaned_data['postcode'], address=form.cleaned_data['postcode'])
            return render(request, 'househunt/property_searchlist.html', {'form': form, 'property': records, 'result': result,})
        else:
            return render(request, 'househunt/property_search.html', {'form': form, })

    return render(request, 'househunt/property_search.html', {'form': form, })

# p = Property(
#         property_id=row[i][2],
#         address=row[i][3],
#         suburb_name=row[i][4],
#         postcode=row[i][5],
#         listed_date=timezone.now(),
#         price=row[i][7],
#         sold_date=timezone.now(),
#         sold_price=row[i][9],
#         listed_agent=row[i][10],
#         modify_date=timezone.now(),
# )