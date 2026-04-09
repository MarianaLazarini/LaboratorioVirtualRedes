from django.shortcuts import render

def portal(request):
    """Página principal com os botões de navegação"""
    return render(request, 'simuladores/portal.html')

def espectro(request):
    """Simulador do Micro-ondas vs Wi-Fi"""
    return render(request, 'simuladores/espectro.html')

def canais_wifi(request):
    """Simulador de Sobreposição de Canais"""
    return render(request, 'simuladores/canais_wifi.html')

def mapa_calor(request):
    """Simulador de Atenuação com Paredes"""
    return render(request, 'simuladores/mapa_calor.html')

def diafonia(request):
    """Simulador de NEXT e Cabos Trançados"""
    return render(request, 'simuladores/diafonia.html')

def atenuacao(request):
    """Simulador de Atenuação por Distância"""
    return render(request, 'simuladores/atenuacao.html')