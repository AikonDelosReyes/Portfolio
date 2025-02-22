from django.shortcuts import render

def dashboard(request):
    data = [
        {"title": "Users", "count": 150},
        {"title": "Orders", "count": 320},
        {"title": "Revenue", "count": "12450"},
    ]
    return render(request, 'dashboard_app/dashboard.html', {'data': data})
