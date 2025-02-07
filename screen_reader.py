import streamlit as st
import PyPDF2
import pytesseract
from PIL import Image
import numpy as np
import plotly.graph_objects as go
from gtts import gTTS
import tempfile
import soundfile as sf
import time


class AdvancedScreenReader:
    def __init__(self):
        st.set_page_config(page_title="Screen Reader", layout="wide")

    def extract_text_from_pdf(self, file):
        try:
            reader = PyPDF2.PdfReader(file)
            return " ".join([page.extract_text() for page in reader.pages])
        except Exception as e:
            st.error(f"PDF Error: {e}")
            return ""

    def extract_text_from_image(self, file):
        try:
            image = Image.open(file)
            return pytesseract.image_to_string(image)
        except Exception as e:
            st.error(f"Image Error: {e}")
            return ""

    def generate_text_summary(self, text, max_words=50):
        words = text.split()
        return ' '.join(words[:max_words]) + '...' if len(words) > max_words else text

    def read_aloud(self, text):
        try:
            tts = gTTS(text=text, lang='en')
            with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp_mp3:
                tts.save(temp_mp3.name)
                return temp_mp3.name
        except Exception as e:
            st.error(f"Audio Generation Error: {e}")
            return None

    def generate_voice_graph(self):
        # Generate random data for voice modulation graph (simulate amplitude)
        x_vals = np.linspace(0, 1, 100)
        y_vals = (np.random.random(100) - 0.5) * 0.6  # Simulate amplitude data
        return x_vals, y_vals

    def dynamic_voice_graph(self):
        # Create a placeholder for the graph
        graph_placeholder = st.empty()

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[], y=[], mode='lines', name="Amplitude"))

        fig.update_layout(
            title="Real-Time Voice Modulation",
            xaxis_title="Time (s)",
            yaxis_title="Amplitude",
            showlegend=True
        )

        # Real-time graph update
        for _ in range(100):  # Loop for 100 updates
            x_vals, y_vals = self.generate_voice_graph()
            fig.data[0].x = x_vals
            fig.data[0].y = y_vals
            graph_placeholder.plotly_chart(fig, use_container_width=True)
            time.sleep(1)  # Wait 1 second for the next update

    def run(self):
        st.title("Intelligent Screen Reader 🧠")

        uploaded_file = st.file_uploader(
            "Upload Document", 
            type=["pdf","jpeg", "png", "txt"]
        )

        if uploaded_file is not None:
            file_ext = uploaded_file.name.split('.')[-1].lower()
            extracted_text = ""

            with st.spinner('Processing document...'):
                if file_ext == "pdf":
                    extracted_text = self.extract_text_from_pdf(uploaded_file)
                elif file_ext in ["jpg", "jpeg", "png"]:
                    extracted_text = self.extract_text_from_image(uploaded_file)
                elif file_ext == "txt":
                    extracted_text = uploaded_file.getvalue().decode("utf-8")

            if extracted_text:
                summary = self.generate_text_summary(extracted_text)
                
                st.subheader("Extracted Text")
                st.text_area("Document Content", value=extracted_text, height=200)

                st.subheader("Text Summary")
                st.write(summary)

                if st.button("Read Summary"):
                    with st.spinner('Generating audio...'):
                        audio_file = self.read_aloud(summary)
                        if audio_file:
                            st.audio(audio_file, format='audio/mp3')

                # Display dynamic voice modulation graph
                st.subheader("Voice Modulation Graph (Dynamic)")
                self.dynamic_voice_graph()


def main():
    reader = AdvancedScreenReader()
    reader.run()


if __name__ == "__main__":
    main()
