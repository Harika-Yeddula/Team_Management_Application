from django.shortcuts import render, redirect
from .models import Member
import teammanagementapplication

# Create your views here.

#View for listing the members
def member_list(request):
    members = Member.objects.all()
    return render(request, 'member_list.html', {'members': members})

#View for editing the members
def member_edit(request,id):
    member = Member.objects.get(pk=id)
    if request.method == 'POST':
        member.first_name=request.POST['first_name']
        member.last_name=request.POST['last_name']
        member.phone_number=request.POST['phone_number']
        member.email=request.POST['email']
        member.role = request.POST['role']
        member.save()
        return redirect('member_list')
    return render(request, 'member_edit.html', {'member': member})

#View for adding the members
def member_add(request):
    if request.method == 'POST':
        Member.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone_number=request.POST['phone_number'],
            email=request.POST['email'],
            role=request.POST['role'],
        )
        return redirect('member_list')
    return render(request,'member_add.html')

#View for deleting the members
def member_delete(request, id):
    Member.objects.get(pk=id).delete()
    return redirect('member_list')
