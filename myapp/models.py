from django.db import models

class Profile(models.Model):
    nome_completo = models.CharField(max_length=100, verbose_name="Nome Completo")
    data_nascimento = models.DateField(verbose_name="Data de Nascimento", blank=True)
    bio = models.TextField(verbose_name="Bio", blank=True)
    linkedin_url = models.URLField(max_length=200, verbose_name="URL do LinkedIn", blank=True)
    email = models.EmailField(verbose_name="Email")
    numero_telefonico = models.IntegerField(verbose_name="Número Telefônico")

    def __str__(self):
        return self.nome_completo

"""
Explicações dos Tipos de Campo Utilizados:

1. CharField: 
   - Utilizado para armazenar strings de tamanho fixo.
   - O parâmetro max_length define o número máximo de caracteres que o campo pode ter.
   - Exemplo: nome_completo é um CharField com um máximo de 100 caracteres.

2. DateField: 
   - Usado para armazenar datas (ano, mês, dia).
   - A opção blank=True permite que o campo seja opcional, ou seja, não é obrigatório preencher este campo.
   - Exemplo: data_nascimento é um DateField que permite datas de nascimento.

3. TextField: 
   - Ideal para armazenar grandes blocos de texto.
   - Não possui limite de caracteres.
   - Exemplo: bio é um TextField usado para armazenar uma biografia, permitindo mais conteúdo textual.

4. URLField: 
   - Usado para armazenar URLs, garantindo que os dados inseridos sejam validados como URLs.
   - max_length define o comprimento máximo permitido para a URL.
   - Exemplo: linkedin_url é um URLField para armazenar a URL do perfil do LinkedIn.

5. EmailField: 
   - Um campo específico para armazenar endereços de e-mail.
   - Valida automaticamente o formato do e-mail para garantir que os dados inseridos estejam corretos.
   - Exemplo: email é um EmailField usado para armazenar endereços de e-mail.

6. IntegerField: 
   - Utilizado para armazenar números inteiros.
   - Exemplo: numero_telefonico é um IntegerField para armazenar números telefônicos como inteiros.
"""
