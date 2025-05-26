import streamlit as st
import openai
import os
from dotenv import load_dotenv, find_dotenv
from moviepy.video.io.VideoFileClip import VideoFileClip

_ = load_dotenv(find_dotenv())

# Configuração da página
st.set_page_config(
    page_title=" Transcript AI",
    page_icon="✨",
    layout="wide",
)

# CSS para uma interface mais moderna e leve
st.markdown("""
<style>
    /* Tema geral mais claro e moderno */
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    /* Cabeçalhos mais elegantes */
    h1, h2, h3 {
        color: #4361ee;
        font-weight: 600;
    }
    
    /* Estilização de inputs */
    .stTextInput > div > div > input {
        border-radius: 8px;
        border: 1px solid #e9ecef;
        padding: 10px;
    }
    
    /* Botões mais modernos */
    .stButton > button {
        background-color: #4361ee;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 8px 16px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #3a56d4;
        box-shadow: 0 4px 8px rgba(67, 97, 238, 0.2);
    }
    
    /* Tabs mais modernas */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        border-bottom: 1px solid #e9ecef;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 10px 24px;
        background-color: transparent;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4361ee !important;
        color: white !important;
    }
    
    /* Cards para conteúdo */
    .content-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }
    
    /* Spinner personalizado */
    .stSpinner > div {
        border-top-color: #4361ee !important;
    }
    
    /* Mensagens de alerta mais suaves */
    .stAlert {
        border-radius: 8px;
    }
    
    /* Espaçamento melhorado */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    
    /* Resultado em card */
    .result-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
        margin-top: 10px;
    }
    
    /* Download button */
    .download-btn {
        background-color: #4361ee;
        color: white;
        padding: 8px 16px;
        border-radius: 8px;
        text-decoration: none;
        display: inline-block;
        margin-top: 10px;
    }
</style>
""", unsafe_allow_html=True)

folder_temp = "temp"
# Criar o diretório temp se não existir
if not os.path.exists(folder_temp):
    os.makedirs(folder_temp)
    
file_audio_temp = f"{folder_temp}/audio.mp3"
file_video_temp = f"{folder_temp}/video.mp4"

# Configuração da API OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")

def transcreve_audio(file_audio, prompt=None):
    """Função para transcrever o áudio usando a API da OpenAI"""
    if file_audio:
        transcription = openai.Audio.transcribe(
            "whisper-1",
            file_audio,
            language="pt",
            response_format="text",
            prompt=prompt
        )
        return transcription
    return None

def transcreve_video(file_video, prompt=None):
    """Função para transcrever áudio a partir de um vídeo"""
    if file_video:
        with open(file_video_temp, "wb") as f_video:
            f_video.write(file_video.read())
        video_convert = VideoFileClip(file_video_temp)
        video_convert.audio.write_audiofile(file_audio_temp)
        with open(file_audio_temp, "rb") as file_audio:
            transcription = openai.Audio.transcribe(
                "whisper-1",
                file_audio,
                language="pt",
                response_format="text",
                prompt=prompt
            )
        return transcription
    return None

def gerar_resumo(transcricao):
    """Função para gerar um resumo da transcrição usando a API da OpenAI"""
    if transcricao:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente especializado em criar resumos concisos e informativos. Extraia os pontos principais e ideias centrais do texto."},
                {"role": "user", "content": f"Crie um resumo objetivo dos principais pontos abordados na seguinte transcrição:\n\n{transcricao}"}
            ],
            max_tokens=500
        )
        return response.choices[0].message['content']
    return None

def main():
    """Função principal da aplicação"""
    st.title("✨ Transcript-AI-com-OPenAi")
    st.markdown("Transforme áudio e vídeo em texto com IA")
    
    tabs = ["📹 Vídeo", "🎵 Áudio"]
    tab_video, tab_audio = st.tabs(tabs)
    
    with tab_video:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.subheader("Upload de Vídeo")
            prompt_video = st.text_input("Instruções para transcrição (opcional)", key="video_prompt", 
                                        placeholder="Ex: Termos técnicos específicos, nomes próprios...")
            file_video = st.file_uploader("Selecione um arquivo de vídeo", type=["mp4"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            if file_video:
                with st.spinner("Processando o vídeo..."):
                    transcricao_video = transcreve_video(file_video, prompt_video)
                    
                if transcricao_video:
                    with st.spinner("Gerando resumo..."):
                        resumo = gerar_resumo(transcricao_video)
                else:
                    st.error("Erro ao transcrever o vídeo")
                    resumo = None
        
        with col2:
            if file_video and transcricao_video:
                st.markdown('<div class="content-card">', unsafe_allow_html=True)
                st.subheader("Resultados")
                
                result_tabs = st.tabs(["📝 Resumo", "📄 Transcrição Completa"])
                
                with result_tabs[0]:
                    if resumo:
                        st.markdown(f"**Resumo do Conteúdo:**")
                        st.markdown(f"{resumo}")
                    else:
                        st.warning("Não foi possível gerar um resumo.")
                
                with result_tabs[1]:
                    st.markdown("**Transcrição Completa:**")
                    st.markdown(f"{transcricao_video}")
                    
                # Opção para download da transcrição
                st.download_button(
                    label="⬇️ Download da Transcrição",
                    data=transcricao_video,
                    file_name="transcricao.txt",
                    mime="text/plain"
                )
                st.markdown('</div>', unsafe_allow_html=True)
    
    with tab_audio:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown('<div class="content-card">', unsafe_allow_html=True)
            st.subheader("Upload de Áudio")
            prompt_audio = st.text_input("Instruções para transcrição (opcional)", key="audio_prompt",
                                        placeholder="Ex: Termos técnicos específicos, nomes próprios...")
            file_audio = st.file_uploader("Selecione um arquivo de áudio", type=["mp3"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            if file_audio:
                with st.spinner("Processando o áudio..."):
                    transcricao_audio = transcreve_audio(file_audio, prompt_audio)
                    
                if transcricao_audio:
                    with st.spinner("Gerando resumo..."):
                        resumo = gerar_resumo(transcricao_audio)
                else:
                    st.error("Erro ao transcrever o áudio")
                    resumo = None
        
        with col2:
            if file_audio and transcricao_audio:
                st.markdown('<div class="content-card">', unsafe_allow_html=True)
                st.subheader("Resultados")
                
                result_tabs = st.tabs(["📝 Resumo", "📄 Transcrição Completa"])
                
                with result_tabs[0]:
                    if resumo:
                        st.markdown(f"**Resumo do Conteúdo:**")
                        st.markdown(f"{resumo}")
                    else:
                        st.warning("Não foi possível gerar um resumo.")
                
                with result_tabs[1]:
                    st.markdown("**Transcrição Completa:**")
                    st.markdown(f"{transcricao_audio}")
                    
                # Opção para download da transcrição
                st.download_button(
                    label="⬇️ Download da Transcrição",
                    data=transcricao_audio,
                    file_name="transcricao.txt",
                    mime="text/plain"
                )
                st.markdown('</div>', unsafe_allow_html=True)

    # Rodapé
    st.markdown("---")
    st.markdown("Desenvolvido por Fernando Horas 💙 usando Streamlit e OpenAI")

if __name__ == "__main__":
    main()