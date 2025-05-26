#!/bin/bash
# Script para executar a aplicação OpenAI

# Criar ambiente virtual se não existir
if [ ! -d "venv_openai" ]; then
    python -m venv venv_openai
fi

# Ativar ambiente virtual
source venv_openai/bin/activate

# Instalar dependências
pip install -r requirements_openai.txt

# Executar aplicação
streamlit run appnew.py

# Desativar ambiente virtual
deactivate