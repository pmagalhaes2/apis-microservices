from flask import Flask, request, make_response, redirect, render_template
app = flask(__name__)

usuarios = [
    {"login": "Maria", "senha": "1234"},
    {"login": "Roberto", "senha": "4321"},
    {"login": "Carlos", "senha": "abcd"},
    {"login": "Paula", "senha": "wxyz"}
]

def verificar_login(login, senha):
    for u in usuarios:
        if u["login"] == login and u["senha"] == senha:
            return u
        return None
    
def autenticar_login():
    login = request.cookies.get("login", "")
    senha = request.cookies.get("senha", "")
    return verificar_login(login, senha)
    