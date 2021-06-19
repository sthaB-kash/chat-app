from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .registerform import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import socket
import threading
import time


def runserver():
    HEADER = 64
    PORT = 1229

    # SERVER = "192.168.123.2"
    DISCONNECT_MESSAGE = "!DISCONNECT"
    SERVER = "172.17.36.97"  # socket.gethostbyname(socket.gethostname())
    print(SERVER)
    ADDR = (SERVER, PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind(ADDR)

    def handle_client(conn, addr):
        print(f"[New connection] {addr} connected.")
        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode('utf-8')
            if msg_length:
                # print("length",msg_length)
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode('utf-8')
                # print("**********",msg)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
                conn.send("Msg received".encode("utf-8"))
        print("outside loop(server)")
        conn.close()

    def start():
        server.listen()
        print(f"[LISTENING] server is Listening on {ADDR}")
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE Connections] {threading.activeCount() - 1}")

    # print(server.listen())

    print("[STARTING] server is starting...")

    start()


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['user_id'] = user.id
            request.session['user_email'] = user.email
            # print(user)
            return redirect('home')
        else:
            messages.info(request, "Username or  Password is invalid")

    context = {}
    return render(request, "login.html", context)


def logout_user(request):
    user = User.objects.get(username=request.user)
    user.is_active = False
    logout(request)
    try:
        del request.session['user_id']
        del request.session['user_email']
    except KeyError:
        pass
    return redirect('login_page')



@login_required(login_url='login_page')
def home(request):
    logged_in = False
    if request.user.is_authenticated:
        print(request.user)
        # logged_in = True
        user = User.objects.get(username=request.user)
        user.is_active = True
        logged_in = True
        print('my id is ', request.session.get('user_id'))

        # open server
        # runserver()

    users = User.objects.all()
    # print(users)
    return render(request, "home.html",  {'users': users, 'logged_in': logged_in})


def registration_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            print(user)
            messages.success(request, 'User account successfully created for \'' + user + '\'')
            return redirect('login_page')
    context = {
        'form': form
    }
    return render(request, "register.html", context)