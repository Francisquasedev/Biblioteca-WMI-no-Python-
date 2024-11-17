# Monitoramento do Sistema com WMI

Este projeto é uma aplicação simples em Python que utiliza a biblioteca `WMI` para coletar informações do sistema, listar processos, monitorar eventos e controlar serviços no Windows.
___
## Funcionalidades

1. **Coletando Informações do Processador**  
   - Exibe o nome do processador, o número de núcleos e a frequência máxima.

2. **Listando Processos em Execução**  
   - Lista todos os processos atualmente em execução, incluindo o ID do processo (PID) e o nome.

3. **Monitorando o Uso de Memória**  
   - Exibe a memória total e a memória física disponível no sistema.

4. **Controlando Serviços do Sistema**  
   - Verifica o estado do serviço de impressão (`Spooler`) e inicia o serviço, caso ele não esteja em execução.

5. **Monitorando Eventos em Tempo Real**  
   - Monitora a criação de novos processos no sistema e exibe o nome e o ID do processo criado.

6. **Executando Consultas Personalizadas com WQL**  
   - Permite executar consultas WQL (Windows Query Language) para buscar processos específicos. Exemplo: busca por `fontdrvhost.exe`.
___
## Requisitos

- Python 3.6 ou superior.
- Sistema operacional Windows.
- Biblioteca `wmi`.
___
### Instalação da Biblioteca `wmi`

Para instalar a biblioteca necessária, execute:
```bash
pip install WMI
```
## Como Executar
1. Clone o repositório ou copie o código
2. Crie um ambiente virtual (opcional, mas recomendado):
```bash
python -m venv venv
```
Ative o ambiente virtual:
- No Windows:
```bash
venv\Scripts\activate
```
3. Instale as dependências:
```bash
pip install WMI
```
4. Execute o script:
```bash
python nome_do_arquivo.py
```
___
## Menu de Opções
Ao executar o programa, você verá o seguinte menu interativo:
Escolha uma das opções:
[1] Coletando Informações do Processador
[2] Listando Processos em Execução
[3] Monitorando o Uso de Memória
[4] Controlando Serviços do Sistema
[5] Monitorando Eventos em Tempo Real
[6] Executando Consultas Personalizadas com WQL
[0] Encerrar
Basta selecionar uma das opções para explorar as funcionalidades.
### Observação
a opção **5 - Monitorando Eventos en Tempo Real** entra em um loop infinito para monitorar eventos continuamente. Para sair, interrompa a execução manualmente (Ctrl + C).
___
## Contribuição
Sinta-se à vontade para contribuir com melhorias, novos recursos ou correções de bugs.
***
## Licença
Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
***
## Contato
Criado por: Francis Monteles
Email: <quasedev@protonmail.com>
LinkedIn: [Francis Monteles](https://www.linkedin.com/in/francis-monteles/)