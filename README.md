# ServicePulse

API assíncrona de monitoramento de disponibilidade e latência de serviços HTTP construída com **FastAPI**, **HTTPX** e **Pydantic**, acompanhada de um **Dashboard web interativo** para visualização em tempo real de *uptime*, latência média, filtros por status e re-testes rápidos.

## Funcionalidades

* **Dashboard Interativo (`/`)**: interface escura responsiva com cartões de **Uptime Geral**, **Serviços Online (UP)**, **Indisponíveis (DOWN)** e **Latência Média (ms)**.
* **Testes Rápidos e Re-testar**: botão **Testar Serviços Populares** para popular o painel na hora e botão **Re-testar** em cada linha do histórico.
* **Verificação Assíncrona (`POST /checks`)**: mede o tempo de resposta em milissegundos e classifica o serviço como `up` (respostas `2xx`–`4xx`) ou `down` (erros `5xx`, *timeouts* ou falhas de rede).
* **Histórico com Filtro (`GET /checks`)**: consulta todas as verificações realizadas com filtro opcional por `?status=up` ou `?status=down`.
* **Documentação Automática (`/docs`)**: interface Swagger gerada automaticamente pelo FastAPI.

## Estrutura do Projeto

* `app/main.py`: rotas HTTP (`GET /`, `GET /health`, `POST /checks`, `GET /checks`) e configuração da aplicação FastAPI.
* `app/checker.py`: lógica de verificação HTTP assíncrona com `HTTPX`, medição de latência e gerenciamento do histórico.
* `app/models.py`: esquemas de entrada e saída validados com `Pydantic`.
* `app/templates/index.html`: interface web do Dashboard com Tailwind CSS.

## Como Executar Localmente

1. **Clone o repositório e entre na pasta:**
   ```powershell
   git clone [https://github.com/victorhugolmdev/servicepulse.git](https://github.com/victorhugolmdev/servicepulse.git)
   cd servicepulse