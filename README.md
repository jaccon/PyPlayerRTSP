# PyPlayerRTSP

PyPlayerRTSP é um player de vídeo RTSP desenvolvido em Python usando a biblioteca OpenCV. Ele oferece recursos simples para visualização de transmissões RTSP de câmeras IP.

## Funcionalidades

- **Visualização de Câmeras RTSP:** Abre e reproduz streams de vídeo RTSP de câmeras IP.

- **Captura de Tela:** Capture instantaneamente uma imagem da transmissão em tela.

- **Modo Tela Cheia:** Alternar entre modos de tela cheia e normal com a tecla 'F'.

- **Instruções na Tela:** Fornece instruções úteis na tela para ajudar os usuários a interagir com o player.

- **Mensagens de Captura:** Exibe uma mensagem "Captured" com fade por 5 segundos após cada captura de tela.

## Como Usar

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/py-playerrtsp.git
    ```

2. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

3. Execute o player RTSP:

    ```bash
    python rtspPlayerCapture.py
    ```

4. Interaja com o player usando as teclas conforme indicado nas instruções.

## Configuração

- O arquivo `config.json` contém a configuração das câmeras, incluindo a URL RTSP, texto da legenda e texto de instruções.

## Contribuição

Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novos recursos. Abra uma issue para discutir suas ideias.

## Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).
