import streamlit as st
from face_detection import detect_face_shape
from skin_tone import get_skin_tone
from recommendations import recommend_colors

st.set_page_config(page_title="AI Fashion Stylist", page_icon="👗", layout="wide")

st.title("👗 AI Fashion Stylist")
st.markdown("#### Upload an image to get personalized fashion recommendations!")

st.sidebar.header("📌 Features")
st.sidebar.markdown("- **Detect Face Shape** 🧑‍🎨\n- **Identify Skin Tone** 🎨\n- **Suggest Outfit Colors** 👕")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("temp.jpg", caption="📸 Uploaded Image", use_column_width=True)

    with col2:
        face_shape = detect_face_shape("temp.jpg")
        skin_tone = get_skin_tone("temp.jpg")
        colors = recommend_colors(skin_tone)

        st.markdown(f"**🔹 Face Shape:** `{face_shape}`")
        st.markdown(f"**🔹 Skin Tone:** `{skin_tone}`")

        st.markdown("### 🎨 Recommended Outfit Colors:")
        for color in colors:
            st.markdown(f"🟢 **{color}**")
