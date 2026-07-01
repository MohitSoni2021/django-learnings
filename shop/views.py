from django.http import HttpResponse

# Create your views here.
def shopHome(req):
    return HttpResponse("This is the home of the shop")

def searchShop(req, shop_id):
    return HttpResponse(f"The shop {shop_id} is at the location ...")

def shopByOpeningYear(req, year):
    return HttpResponse(f"Sine {year}, we are providing the best quality of goods...")

# This function is handling multiple arguments... using kwargs - return the dict of info...
def shopInformations(req, **kwargs):
    print("Information from shopInformation Function:")
    print(kwargs)
    return HttpResponse(f"The shop id : {kwargs['shop_id']} and shop name : {kwargs['shop_name']} is now at your screen...")
