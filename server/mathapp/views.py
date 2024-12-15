from django.shortcuts import render

def power(request):
    context = {
        'power': "0",
        'I': "0",
        'R': "0",
    }
    if request.method == 'POST':
        print("POST method is used")
        try:
            # Get values from the form
            I = float(request.POST.get('current', '0'))
            R = float(request.POST.get('resistance', '0'))
            
            # Calculate power
            power = (I ** 2) * R
            
            # Update context
            context['power'] = power
            context['I'] = I
            context['R'] = R

            print(f"Current (I) = {I}")
            print(f"Resistance (R) = {R}")
            print(f"Power (P) = {power}")

        except ValueError:
            context['power'] = "Invalid input"
            print("Error: Invalid input detected")
    
    return render(request, 'mathapp/math.html', context)

