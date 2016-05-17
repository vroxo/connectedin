from django.shortcuts import render
from models import Perfil

def index(request):
	return render(request, 'index.html')

def exibir(request,perfil_id):
	perfil = Perfil()

	if (perfil_id == '1'):
		perfil = Perfil(nome='Flavio Almeida', email='flavio@flavio.com.br', telefone='777777', nome_empresa='Caelum')

	return render(request, 'perfil.html', {'perfil': perfil})