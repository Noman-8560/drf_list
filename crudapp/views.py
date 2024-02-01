from django.shortcuts import render
from .models import Student
from django.contrib import messages
from django.db.models import Q

def index(request):
    students = None  # Initialize students as None
    search_query = ""
    
    if request.method == "POST":
        if "create" in request.POST:
            name = request.POST.get("name")
            fname = request.POST.get("fname")
            cnic = request.POST.get("cnic")
            serial = request.POST.get("serial")
            fno = request.POST.get("fno")
            Student.objects.create(
                name=name,
                fname=fname,
                cnic=cnic,
                serial=serial,
                fno=fno,
            )
            messages.success(request, "Voter added Successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            fname = request.POST.get("fname")
            cnic = request.POST.get("cnic")
            serial = request.POST.get("serial")
            fno = request.POST.get("fno")
            student = Student.objects.get(id=id)
            student.name = name
            student.fname = fname
            student.cnic = cnic
            student.serial = serial
            student.fno = fno
            student.save()
            messages.success(request, "Voter updated Successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request, "Voter deleted Successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            if search_query:  # Check if search query is not empty
                students = Student.objects.filter(Q(name__icontains=search_query) | Q(cnic__icontains=search_query))
                # Only pass filtered data to the template if search query is provided

    context = {"students": students, "search_query": search_query}
    return render(request, "index.html", context=context)
