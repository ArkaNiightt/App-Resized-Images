import streamlit as st
from PIL import Image
import io
import zipfile


def resize_image(image, target_size):
    return image.resize(target_size, Image.Resampling.LANCZOS)


def main():
    st.set_page_config(
        page_title="Aplicativo de Redimensionamento de Imagens", layout="centered")
    st.title("📸 Aplicativo de Redimensionamento de Imagens")

    col1, col2 = st.columns(2)

    with col1:
        uploaded_files = st.file_uploader(
            "Carregar Imagens",
            type=["jpg", "jpeg", "png", "bmp", "gif", "tiff"],
            accept_multiple_files=True
        )

    with col2:
        target_width = st.number_input(
            "Largura Desejada", min_value=1, value=1061)
        target_height = st.number_input(
            "Altura Desejada", min_value=1, value=1500)
        target_size = (target_width, target_height)

    if st.button("Redimensionar Imagens"):
        if uploaded_files:
            with io.BytesIO() as buffer:
                with zipfile.ZipFile(buffer, "w") as zipf:
                    for file in uploaded_files:
                        try:
                            img = Image.open(file)
                            resized_img = resize_image(img, target_size)
                            img_byte_arr = io.BytesIO()
                            resized_img.save(img_byte_arr, format=img.format)
                            zipf.writestr(file.name, img_byte_arr.getvalue())
                        except Exception as e:
                            st.error(f"Erro ao processar {file.name}: {e}")
                buffer.seek(0)
                st.download_button(
                    "⬇️ Baixar Imagens Redimensionadas",
                    buffer,
                    "imagens_redimensionadas.zip",
                    mime="application/zip"
                )
        else:
            st.warning("⚠️ Por favor, carregue pelo menos uma imagem.")


if __name__ == "__main__":
    main()
