from django.shortcuts import render
import razorpay
# Create your views here.


def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        client = razorpay.Client(auth = ("rzp_test_bKtMj90QOs6Af2", "vNLvdBnrIGSHG2C4BiWoDGvd"))
    return render(request,'app/index.html')


def success(request):
    return render(request, 'app/success.html')