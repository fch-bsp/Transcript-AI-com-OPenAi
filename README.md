# Transcript AI

![Transcript AI](https://img.shields.io/badge/Transcript-AI-4361ee?style=for-the-badge&logo=openai)

Uma aplicação moderna para transcrição e resumo de conteúdo de áudio e vídeo utilizando inteligência artificial.

## 📋 Visão Geral

Transcript AI é uma aplicação web desenvolvida com Streamlit que permite aos usuários fazer upload de arquivos de áudio ou vídeo e obter transcrições precisas e resumos concisos do conteúdo. A aplicação utiliza a API da OpenAI (Whisper para transcrição e GPT-3.5 para resumo) para fornecer resultados de alta qualidade.

## ✨ Funcionalidades

- **Transcrição de Vídeo**: Converte arquivos MP4 em texto
- **Transcrição de Áudio**: Converte arquivos MP3 em texto
- **Geração de Resumo**: Cria automaticamente um resumo dos pontos principais do conteúdo
- **Interface Moderna**: Design limpo e intuitivo com tema claro
- **Download de Resultados**: Permite salvar as transcrições em formato de texto
- **Suporte a Prompts**: Possibilidade de fornecer instruções específicas para melhorar a transcrição

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para criação da interface web
- **OpenAI API**: Serviços de IA para transcrição (Whisper) e resumo (GPT-3.5)
- **MoviePy**: Biblioteca para processamento de vídeo
- **Python**: Linguagem de programação base
- **dotenv**: Gerenciamento de variáveis de ambiente

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/transcript-ai.git
   cd transcript-ai
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   Crie um arquivo `.env` na raiz do projeto com sua chave da API OpenAI:
   ```
   OPENAI_API_KEY=sua_chave_api_aqui
   ```

4. Execute a aplicação:
   ```bash
   streamlit run 02-appnew.py
   ```

## 🚀 Como Usar

1. **Iniciar a Aplicação**: Execute o comando acima para iniciar o servidor Streamlit
2. **Selecionar Modo**: Escolha entre as abas "Vídeo" ou "Áudio"
3. **Fazer Upload**: Carregue seu arquivo MP4 (vídeo) ou MP3 (áudio)
4. **Adicionar Instruções** (opcional): Forneça termos específicos ou instruções para melhorar a transcrição
5. **Processar**: Aguarde enquanto a IA processa o conteúdo
6. **Visualizar Resultados**: Veja o resumo e a transcrição completa nas abas de resultados
7. **Download**: Baixe a transcrição completa se desejar

## 🔍 Detalhes de Implementação

### Fluxo de Processamento

1. **Upload do Arquivo**: O usuário faz upload de um arquivo de áudio ou vídeo
2. **Processamento Inicial**:
   - Para vídeos: Extração do áudio usando MoviePy
   - Para áudios: Processamento direto
3. **Transcrição**: O áudio é enviado para a API Whisper da OpenAI
4. **Resumo**: A transcrição é processada pelo GPT-3.5 para gerar um resumo conciso
5. **Exibição**: Os resultados são mostrados em uma interface organizada

### Estrutura do Código

- **Configuração Inicial**: Carregamento de variáveis de ambiente e configuração da página
- **Processamento de Arquivos**: Funções para lidar com arquivos temporários
- **Integração com API**: Chamadas para os serviços da OpenAI
- **Interface do Usuário**: Layout responsivo com Streamlit
- **Estilização**: CSS personalizado para uma experiência visual moderna

## 📝 Notas de Desenvolvimento

### Fase 1: Configuração Inicial
- Configuração do ambiente e dependências
- Implementação da estrutura básica da aplicação
- Integração com a API da OpenAI

### Fase 2: Desenvolvimento da Interface
- Criação de uma interface de usuário intuitiva
- Implementação de upload de arquivos
- Exibição de resultados em formato organizado

### Fase 3: Aprimoramentos
- Adição da funcionalidade de resumo
- Melhorias na interface do usuário
- Otimização do processamento de arquivos

### Fase 4: Refinamento
- Implementação de tema visual moderno
- Adição de recursos de download
- Melhorias na experiência do usuário

## 🔒 Requisitos de API

Para utilizar esta aplicação, você precisa de uma chave de API válida da OpenAI com acesso aos seguintes modelos:
- **Whisper-1**: Para transcrição de áudio
- **GPT-3.5-turbo**: Para geração de resumos

## 👨‍💻 Autor

Desenvolvido por **Fernando Horas**

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no GitHub!