from django.test import TestCase
from join.models import Campo

# Create your tests here.
class CampoTestCase(TestCase):
    '''
        - Class responsável pelos teste feitos na classe Campo
    '''
    def setUp(self) -> None:
        # cria instancia de campo no nosso banco de dados teste
        self.campo = Campo.objects.create(
            nome='Nome do local',
            latitude=-22.934849111475224,
            longitude=-43.35453760891537,
            data_expiracao='2022-12-01'
        )
    
    def test_fields_model(self):
        '''
            - Verifica se modelo esta recebendo os dados no formato escolhido
        '''
        self.assertEqual(self.campo.nome, 'Nome do local')
        self.assertEqual(self.campo.latitude, -22.934849111475224)
        self.assertEqual(self.campo.longitude, -43.35453760891537)
        self.assertEqual(self.campo.data_expiracao, '2022-12-01')