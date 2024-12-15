# Ex.05 Design a Website for Server Side Processing
# Date:19/10/24
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
<!DOCTYPE html>
<html>
<head>
<meta charset='utf-8'>
<meta http-equiv='X-UA-Compatible' content='IE=edge'>
<title>Power Calculation</title>
<meta name='viewport' content='width=device-width, initial-scale=1'>
<style type="text/css">
body {
    background-color: lavender;
}
.edge {
    width: 100%;
    padding-top: 250px;
    text-align: center;
}
.box {
    display: inline-block;
    border: thick dashed rgb(210, 237, 118);
    width: 500px;
    min-height: 300px;
    font-size: 20px;
    background-color: rgb(232, 17, 207);
}
.formelt {
    color: black;
    text-align: center;
    margin-top: 7px;
    margin-bottom: 6px;
}
h1 {
    color: black;
    padding-top: 20px;
}
</style>
</head>
<body>
<div class="edge">
    <div class="box">
        <h1>Power Calculation (P = I<sup>2</sup>R)</h1>
        <h3>Kanishka(24003362)</h3>
        <form method="POST">
            {% csrf_token %}
            <div class="formelt">
                Current (I): <input type="text" name="current" value="{{I}}"> A<br/>
            </div>
            <div class="formelt">
                Resistance (R): <input type="text" name="resistance" value="{{R}}"> Ω<br/>
            </div>
            <div class="formelt">
                <input type="submit" value="Calculate"><br/>
            </div>
            <div class="formelt">
                Power (P): <input type="text" name="power" value="{{power}}"> W<br/>
            </div>
        </form>
    </div>
</div>
</body>
</html>

views.py

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

urls.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('powercalculation/', views.power, name="powercalculation"),
    path('', views.power, name="powerroot"),
]

```
# SERVER SIDE PROCESSING:
![alt text](<Screenshot 2024-12-15 174433.png>)
# HOMEPAGE:
![alt text](<Screenshot 2024-12-15 174008.png>)
# RESULT:
The program for performing server side processing is completed successfully.
