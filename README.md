# Reconhecimento de Voz com AWS Transcribe

## 📜 Descrição

Este projeto automatiza a transcrição de arquivos de áudio para texto utilizando os serviços da AWS, especialmente o Amazon Transcribe.  
Ele possibilita o upload de áudios em um bucket Amazon S3, dispara automaticamente a transcrição via AWS Lambda, e salva o texto transcrito em outro bucket S3 para fácil acesso.

---

## 🚀 Funcionalidades

- Upload automático de arquivos de áudio (MP3, WAV, MP4, entre outros) para o bucket S3.
- Início automático do job de transcrição usando Amazon Transcribe.
- Monitoramento do status da transcrição via EventBridge.
- Salvamento da transcrição em formato `.txt` em bucket S3 separado.
- Arquitetura serverless usando AWS Lambda e SAM (Serverless Application Model).
- Fácil escalabilidade e deploy via infraestrutura como código.

---

## 🛠 Tecnologias utilizadas

- AWS Transcribe  
- AWS S3  
- AWS Lambda  
- AWS EventBridge  
- AWS SAM  
- Python 3.x  
- Boto3 (SDK AWS para Python)

---

## 📂 Estrutura do projeto

transcribe-pipeline/
│
├── template.yaml # Infraestrutura (SAM/CloudFormation)
├── lambda_start_job/
│ └── app.py # Lambda que inicia o job de transcrição
├── lambda_process_result/
│ └── app.py # Lambda que processa o resultado e salva no S3
└── requirements.txt # Dependências Python

yaml
Copiar
Editar

---

## ⚙️ Como usar

### Pré-requisitos

- Conta AWS com permissões para S3, Transcribe, Lambda e EventBridge  
- AWS CLI configurado com credenciais válidas  
- AWS SAM CLI instalado  

### Passos

1. Clone este repositório:  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
Build do projeto com SAM:

bash
Copiar
Editar
sam build
Deploy com SAM:

bash
Copiar
Editar
sam deploy --guided
Siga as instruções para informar nomes dos buckets e permissões.

Faça upload de um arquivo de áudio no bucket S3 configurado para entrada.

Aguarde a transcrição ser processada automaticamente.

Encontre o arquivo .txt com a transcrição no bucket S3 de saída, dentro da pasta processed/.

📈 Aplicações
Transcrição de podcasts, entrevistas e reuniões

Geração automática de legendas

Acessibilidade para pessoas com deficiência auditiva

Automação de fluxos que envolvem áudio para texto

📌 Contato
Se tiver dúvidas ou quiser contribuir, fique à vontade para abrir issues ou enviar pull requests!
Contato: Gabriel Gomes — LinkedIn

📝 Licença
MIT License — veja o arquivo LICENSE para mais detalhes.


---

MIT License

Copyright (c) 2025 Gabriel Gomes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
