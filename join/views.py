import folium
from join import models
from join.forms import CampoForm
from django.middleware import csrf
from django.shortcuts import render, redirect



def index(request):
    # formulario para adicionar nova coordenada no mapa
    if request.method == 'POST':
        form = CampoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CampoForm()


    # posicao inicial do mapa
    m = folium.Map([-22.934849111475224, -43.35453760891537], zoom_start=2)
    # verifica se banco esta vazio
    if models.Campo.objects.count() == 0:
        mensagem = 'Não existe nenhum local cadastrado'
    else:
        mensagem = None
    # marca no mapa todos os pontos registrados e disponibiliza um popup com formulario para deletar e atualizar instancia
        coordenadas = models.Campo.objects.all()
        for coordenada in coordenadas:
            folium.Marker([coordenada.latitude, coordenada.longitude], tooltip=coordenada.nome, popup=f'''
                                <form method="POST">
                                    <input type="hidden" name="csrfmiddlewaretoken" value="{csrf.get_token(request)}">
                                    <div class="mb-3">
                                        <label for="nome_local" class="form-label">Nome do local</label>
                                        <input type="text" class="form-control" id="nome" name="nome" value={coordenada.nome} required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="latitude" class="form-label">Latitude</label>
                                        <input type="text" class="form-control" id="latitude" name="latitude" value={coordenada.latitude} required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="longitude" class="form-label">Longitude</label>
                                        <input type="text" class="form-control" id="longitude" name="longitude" value={coordenada.longitude} required>
                                    </div>
                                    <div class="mb-3">
                                        <label for="data_expiracao" class="form-label">Data de expiração</label>
                                        <input type="date" class="form-control" id="data_expiracao" name="data_expiracao" value={coordenada.data_expiracao} required>
                                    </div>
                                    <div style="display: flex; margin-top: 10px;" class="container">
                                    <button type="submit" class="p-2 btn btn-success" formaction="/join/atualiza/{coordenada.pk}">Atualizar</button>
                                    <button type="submit" class="btn btn-danger" formaction="/join/deleta/{coordenada.pk}">Excluir</button>
                                    </div>
                                </form>
                        ''').add_to(m)
        
    # representacao html do mapa
    m = m._repr_html_()

    context = {
        'm': m,
        'mensagem': mensagem,
        'form': form,
    }
    return render(request, 'join/index.html', context=context)


def atualiza_coordedana(request, pk):
    # instancia que queremos atualizar
    coordenada = models.Campo.objects.get(pk=pk)
    if request.method == 'POST':
        # passa coordenada como instancia que queremos atualizar no formulario
        form = CampoForm(request.POST, instance=coordenada)
        if form.is_valid():
            # salva instancia atualizada no banco
            form.save()
            return redirect('index')
    else:
        form = CampoForm()
    return render(request, 'join/index.html', context=None)


def deleta_coordedana(request, pk):
    # instancia que queremos deletar
    coordenada = models.Campo.objects.get(pk=pk)
    if request.method == 'POST':
        # deleta instancia
        coordenada.delete()
        return redirect('index')
    return render(request, 'join/index.html', context=None)