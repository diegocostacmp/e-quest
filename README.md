

# eQuest Games

Sistema de respostas para estudantes, o qual visa atingir o potencial da gamificação para motivar e engajar os alunos durante o processo de aprendizado.

## Início - Principais características

* Plataforma multi tenancy, com perfil aluno e professor;
* Implementação de sistema em plataforma Web totalmente responsiva;
* Persistência de dados no banco mysql, utilizando modelo relacional;
* Jornada do Usuário e Casos de Uso.

### Pre-requisitos

Requisitos minimos para utilização do sistema:

```
Python 3.7.2+
```
```
Django 2.0.2+
```

### Instalação

A seguir um passo a passo para a instalação do sistema e suas dependências

* clone o projeto:
```
git clone https://github.com/diegocostacmp/e-quest.git
```
* Certifique-se de que o Python e o Ambiente Virtual (venv) estejam instalados.
Crie o ambiente virtual e instale os pacotes.
 ```
 cd e-quest
 virtualenv venv
 source venv/bin/activate
 pip install -r requirements.txt
```
* Execute as migrações do banco de dados:

```
python manage.py makemigrations
python manage.py migrate
```

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

