from django.shortcuts import render

def home(request):
    return render(request, 'index.html')
def calculator(request):
    number1=eval(request.GET.get('number1','0'))
    number2=eval(request.GET.get('number2','0'))
    sum=number1+number2
    sub=number1-number2
    mul=number1*number2
    div=number1/number2
    data={'addition':sum, 'subtraction':sub, 
          'multiplication':mul, 'division':div,}
    return render(request, 'calculator.html',data)
    

    

