from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PerfilTreinadorView(APIView):
    # 🛡️ Esse atributo garante que o DRF vai barrar quem não mandar um JWT válido
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # O Django automaticamente injeta o usuário logado no request.user graças ao JWT
        usuario = request.user

        # Aqui, na Clean Arch, você pegaria esse usuario e passaria para um Use Case.
        # Por enquanto, vamos retornar direto para testar:
        dados_treinador = {
            "username": usuario.username,
            "email": usuario.email,
            "saldo_pokedollars": 1000.00,  # Exemplo estático (depois virá do banco)
        }

        return Response(dados_treinador)
