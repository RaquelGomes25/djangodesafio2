# djangodesafio2
1 - Criei um ambiente virtual biblioteca e ativei o ambiente virtual

2 - Instalei o django 

    pip install django

3 - Criei um projeto biblioteca_virtual e criei um aplicativo clientes para salvar dados de clientes

4 - Instalar as dependências do django rest framework, que são:

	pip install djangorestframework
  
    pip install markdown
  
	pip install django-filter
  
5 - Registrei o django rest e o aplicativo “clientes” no settings.py

6 – Crie no models.py  um tabela no banco chamada Cliente com os seguintes atributos: nome, idade, rg , cpf , email e telefone

7 - Para o atributo Telefone Instalei 

    pip install django-phonenumber-field[phonenumberslite]

8- Registrei 'phonenumber_field', na lista de aplicativos instalados no settings.py

9 - Para o atributo CPF Instalei 

    pip install django-cpf 

10- Registrei ‘cpf_field’ , na lista de aplicativos instalados no settings.py

11 – Fiz o comando  python .\manage.py makemigrations para criar a tabela no banco de dados

12 - Fiz o comando  python .\manage.py migrate 

13 - Crie um super usuário com o comando: python .\manage.py createsuperuser

14 - Registrei a tabela no admin.py : admin.site.register(Cliente)

15 - Dentro do aplicativo criei um novo arquivo chamado serializers.py para fazer a serialização e apresentar os dados em json

16 - Importei e criei o queryset para ter a lista com todos os clientes a partir da base de dados no views.py

17 - Na urls.py do projeto foi criada a rota

18 - Rodei o comando python .\manage.py runserver e apresentou a tela:

![image](https://user-images.githubusercontent.com/92063008/178159814-99bde4b8-472d-43d9-beac-fdb83d659ab3.png)

![image](https://user-images.githubusercontent.com/92063008/178159851-a999958e-3ec7-4e85-bc55-ec4f181e0c43.png)

![image](https://user-images.githubusercontent.com/92063008/178159860-d11b96f4-b781-4e31-b632-5438b8d1d6fc.png)

19 – Para criar o cache fiz o import  cache_page e o import method_decorator no views.py.

20 – Criei  a função list que já vem pronta do Viewsets 

    @method_decorator(cache_page(60))

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

21 – Para iniciar os testes exclui o arquivo existente no aplicativo e criei uma nova pasta chamada tests. 

22 - Dentro dessa pasta eu criei inicial __init__.py e o test_models.py

23- Dentro do test_models.py fiz o import do unitttest , fiz a classe TestCliente, fiz a função e passei o atributo a ser testado.

24 – Testei se o atributo nome Raquel  era igual a Raquel e obtive Sucesso

![image](https://user-images.githubusercontent.com/92063008/178159903-340bf9b9-09d1-4455-9d29-abb591ff80a0.png)

25 – Testei se o atributo nome Raquel  era igual a Mariana e obtive Erro

![image](https://user-images.githubusercontent.com/92063008/178159918-a610c7ce-a7c0-476a-bfb8-28f3e5003632.png)

26 - Fiz Teste Exploratório

	Rodei o comando python .\manage.py runserver Cliquei no http do Clientes

![image](https://user-images.githubusercontent.com/92063008/178159936-e13ec277-78c6-4748-8b2c-4907f29ea6ae.png)

	Funcionou e fui direcionada para essa tela

![image](https://user-images.githubusercontent.com/92063008/178159950-bb023e58-ac06-4d65-85e3-903ed2a7e590.png)

	Preenchi os dados e cliquei no botão de POST

![image](https://user-images.githubusercontent.com/92063008/178159959-37c9a198-ffb3-41c8-ac99-0e81641c16c1.png)

	Funcionou e os dados apareceram na parte superior

![image](https://user-images.githubusercontent.com/92063008/178159972-ae00417f-cee8-4f9f-8818-d033b5686bfa.png)

	Já atualizado com dois clientes

![image](https://user-images.githubusercontent.com/92063008/178159987-0510c6b0-9670-46c1-8667-f6d8c072239d.png)

    Já no banco de dados

![image](https://user-images.githubusercontent.com/92063008/178160001-30677f77-ae2e-4684-b505-1555ec9a9d87.png)




 


