
# IDE Tkinter

Uma mini IDE desenvolvida em Python utilizando a biblioteca Tkinter, que permite abrir, editar, salvar e executar arquivos Python (.py) diretamente em uma interface gráfica amigável.

## 🚀 Funcionalidades

- Abrir arquivos Python (.py)
- Editar o conteúdo do arquivo
- Salvar alterações
- Executar o código diretamente na interface
- Exibir saída e erros no terminal integrado
- Interface intuitiva com botões gráficos personalizados

## 📁 Estrutura do Projeto

```
ide_tkinter/
├── __app__.py                # Arquivo principal que executa a aplicação
├── classes/
│   └── Application.py        # Classe principal da aplicação
├── consts/
│   └── const.py              # Arquivo de constantes (paths, configs)
├── functions/
│   ├── config_window.py      # Configurações da janela principal
│   ├── create_buttons.py     # Criação dos botões
│   ├── create_frames.py      # Criação dos frames
│   ├── open_images.py        # Carregamento das imagens
│   └── commands/             # Comandos da IDE
│       ├── close_app.py      # Fechar aplicação
│       ├── execute_code.py   # Executar código Python
│       ├── open_archive.py   # Abrir arquivo .py
│       ├── save_archive.py   # Salvar arquivo
│       └── set_path.py       # Definir path do arquivo
├── images/                   # Imagens e ícones da interface
│   ├── icon_app.ico
│   ├── open_archive.png
│   ├── save_archive.png
│   ├── run_code.png
│   └── exit_program.png
```

## 🛠 Tecnologias Utilizadas

- Python 3
- Tkinter (GUI)
- Pillow (manipulação de imagens)
- Subprocess (execução de códigos)

## 💽 Instalação e Execução

1. Clone o repositório ou baixe o projeto.

```bash
git clone https://github.com/joaovictor0209/ide_tkinter.git
```

2. Acesse a pasta do projeto.

```bash
cd ide_tkinter
```

3. Instale as dependências (se ainda não tiver):

```bash
pip install pillow
```

4. Execute o arquivo principal:

```bash
python __app__.py
```

## 👥 Autor

- **João Victor Alexandre Almeida**

## 💡 Observações

- O terminal integrado mostra tanto a saída padrão (`stdout`) quanto os erros (`stderr`) dos códigos Python executados.
- A interface foi projetada para ser simples, prática e intuitiva.
- Todos os caminhos de imagens estão centralizados no arquivo `consts/const.py`.
