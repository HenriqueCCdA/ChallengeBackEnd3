from django.shortcuts import redirect, render
from cbe3.core.models import Register, User

from cbe3.core.transaction import (file_csv,
                                   file_is_empty,
                                   first_date,
                                   save_transactions_db,
                                   transaction_valid)


def import_csv(request):
    dict_ = {}
    dict_['register'] = Register.objects.all()
    if request.method == 'POST' and request.FILES.get('csv-file'):
        file_in_memory = request.FILES['csv-file']

        raw_transactions = file_csv(file_in_memory)
        raw_transactions = transaction_valid(raw_transactions)
        dict_['csv_file'] = file_in_memory.name
        if file_is_empty(raw_transactions):
            dict_['status'] = 'empty'
            return render(request, 'import_csv.html', dict_)

        if not save_transactions_db(raw_transactions):
            dict_['status'] = 'duplicate'
            dict_['day'] = first_date(raw_transactions)
            return render(request, 'import_csv.html', dict_)

        dict_['status'] = 'ok'
        return render(request, 'import_csv.html', dict_)

    return render(request, 'import_csv.html', dict_)


def register(request):

    if request.method == 'POST':
        username = request.POST['username']  # TODO: Valida com forms.
        email = request.POST['email']

        old_user = User.objects.filter(email=email).first()

        if old_user:
            context = {'status': 'duplicate', 'email': email}
            return render(request, 'register_user.html', context)

        User.objects.create_user(username=username, email=email)

    return render(request, 'register_user.html')


def users_list(request):

    users = User.objects.filter(is_staff=False)

    return render(request, 'users_list.html', {'users': users})


def delete_user(request, id):
    User.objects.get(id=id).delete()

    users = User.objects.filter(is_staff=False)

    return render(request, 'users_list.html', {'users': users})


def update_user(request, id):

    if request.method == 'POST':
        username = request.POST['username']  # TODO: Valida com forms.

        user = User.objects.get(id=id)

        user.username = username
        user.save()

        return redirect('users_list')

    user = User.objects.get(id=id)

    return render(request, 'edit_user.html', {'user_edit': user})
