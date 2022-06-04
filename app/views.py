from django.shortcuts import render
from app.models import Coffe
import razorpay
# Create your views here.


def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = int(request.POST.get('amount')) * 100
        client = razorpay.Client(auth = ("rzp_test_bKtMj90QOs6Af2", "vNLvdBnrIGSHG2C4BiWoDGvd"))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
        print(payment)
        coffe = Coffe(name=name, amound=amount, paiment_id=payment['id'])
        return render(request,'app/index.html', {'payment':payment})
    return render(request,'app/index.html')


def success(request):
    return render(request, 'app/success.html')