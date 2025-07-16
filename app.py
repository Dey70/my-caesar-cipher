import streamlit as st


st.set_page_config(page_title="Caesar Cipher", page_icon="🔐")

st.markdown("""
<style>
    .ascii-art {
        font-family: monospace;
        white-space: pre;
        line-height: 1;
        margin: 0.5rem 0;
    }
    .header {
        text-align: center;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)


st.markdown('<div class="header"><h1>🔐 Caesar Cipher Encryption Tool</h1></div>', unsafe_allow_html=True)


st.markdown('<div class="ascii-art">' + r"""
  ____                    ____       _               
 / ___|__ _ ___  ___ _ __/ ___|  ___(_) ___ _ __ ___ 
| |   / _` / __|/ _ \ '__\___ \ / __| |/ _ \ '__/ __|
| |__| (_| \__ \  __/ |   ___) | (__| |  __/ |  \__ \
 \____\__,_|___/\___|_|  |____/ \___|_|\___|_|  |___/
""" + '</div>', unsafe_allow_html=True)

st.markdown('<div class="ascii-art">' + r"""
   _____     _                _       _     
  / ____|   (_)              | |     | |    
 | |     ___ _ _ __ ___ _ __ | | __ _| |__  
 | |    / _ \ | '__/ _ \ '_ \| |/ _` | '_ \ 
 | |___|  __/ | | |  __/ |_) | | (_| | | | |
  \_____\___|_|_|  \___| .__/|_|\__,_|_| |_|
                       | |                  
                       |_|                  
""" + '</div>', unsafe_allow_html=True)


alphabet = list("abcdefghijklmnopqrstuvwxyz")

def caesar_cipher(text, shift, mode):
    if mode == "Decode":
        shift *= -1

    result = ""
    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result

mode = st.radio("Choose an operation:", ["Encode", "Decode"])
text = st.text_input("Enter your message:").lower()
shift = st.slider("Shift amount", 1, 25, 3)

if st.button("Run Caesar Cipher"):
    result = caesar_cipher(text, shift, mode)
    st.success(f"The {mode.lower()}d text is: {result}")
