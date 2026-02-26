# Maneger Packages: Fedora

Olá, este projeto foi criado com o propósito de facilitar questões como automatizar ações corriqueiras utilizando o terminal. Todo o projeto foi criado voltado para a familía RPM (apesar de que com pouco esforço, a mesma possa atender distros da familía DEB).

![gif](https://github.com/Diogonogueirasantos/Maneger_Packages/blob/main/recursos/ezgif.com-video-to-gif-converter.gif)

## Tecnologia Usada

- Pyqt6



## Como usar
Para utilizar esta aplicação é necessário clonar este repositório estar dentro do mesmo e seguir as instruções abaixo.

Primeiro é necessário criar um ambiente virtual, pois é altamente recomendável a criação do mesmo, assim evitando conflito de dependências.

	python3 -m venv nome_para_seu_ambiente

com o seu ambiente criado basta ativar o seu ambiente e baixar os requisitos necessários que estão no arquivo **requirements.txt**

	source nome_do_seu_ambiente/bin/activate

agora é preciso instalar os requisitos necessários -- que no nosso caso é o módulo **Pyqt6**.

	pip3 install -r requirements.txt

Com isso agora só precisamos instânciar o script *update.py*

	python3 update.py


depois que terminar de utilizar esta aplicação recomendo desativar o seu ambiente virtual, pois assim se evita a instalação outros módulos python neste ambiente.

	deactivate 

	
