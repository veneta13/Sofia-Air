import streamlit as st

# page info
st.set_page_config(
    layout='wide',
    page_title='Sofia Air',
    page_icon=':cloud:',
)


def switch_lang(lang):
    if 'lang' in st.session_state:
        if lang == 'bg':
            st.session_state.lang = 'bg'
        else:
            st.session_state.lang = 'en'


@st.cache
def bind_socket(session_state):
    session_state.lang = 'bg'


bind_socket(st.session_state)
if 'lang' not in st.session_state:
    st.session_state.lang = 'bg'

################### SIDEBAR #########################
with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.button(
            label='EN',
            key='en',
            on_click=switch_lang,
            args=['en']
        )
    with col2:
        st.button(
            label='BG',
            key='bg',
            on_click=switch_lang,
            args=['bg']
        )
