from django.shortcuts import render

def SimpleMarksheet(request):
    context = {
        't': None,
        'p': None,
        'divi': None
    }
    if request.method == "POST":
        try:
            s1 = float(request.POST.get("num1"))
            s2 = float(request.POST.get("num2"))
            s3 = float(request.POST.get("num3"))
            s4 = float(request.POST.get("num4"))
            s5 = float(request.POST.get("num5"))
            t=s1+s2+s3+s4+s5
            p= (t * 100)/500
            if p>60:
                divi="First Class"
            elif p>50:
                divi="Second Class"
            elif p>35:
                divi="pass"
            else:
                divi="fail"
            context = {
                't': t,
                'p': p,
                'divi': divi
            }
        except Exception as e:
            print(f"Error: {e}")
            context['divi'] = "Invalid Input"
    
    return render(request, 'SimpleMarksheet.html', context)