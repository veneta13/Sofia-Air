import streamlit as st

import util_funcs

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

content = util_funcs.load_content()
levels = util_funcs.load_levels()

#################### TITLE ##########################
st.title(content['reference_title'][st.session_state.lang])

################## SUBHEADING #######################
st.subheader(content['reference_subheading'][st.session_state.lang])

################### METRICS #########################
col11, col12, col13, col14 = st.columns(4)

col11.metric(
    content['particulate_matter_label'][st.session_state.lang],
    str(levels["Particulate matter"]) + " µg/m³",
)
col12.metric(
    content['03_label'][st.session_state.lang],
    str(levels["O3"]) + " µg/m³"
)
col13.metric(
    content['SO2_label'][st.session_state.lang],
    str(levels["SO2"]) + " µg/m³"
)
col14.metric(
    content['NO2_label'][st.session_state.lang],
    str(levels["NO2"]) + " µg/m³"
)

col21, col22, col23 = st.columns(3)

col21.metric(
    content['CO_label'][st.session_state.lang],
    str(levels["CO"]) + " µg/m³"
)
col22.metric(
    content['C6H6_label'][st.session_state.lang],
    str(levels["C6H6"]) + " µg/m³"
)
col23.metric(
    content['NO_label'][st.session_state.lang],
    str(levels["NO"]) + " µg/m³"
)

##################### NOTES #########################
st.markdown('##')
st.subheader(content['reference_notes_subheading'][st.session_state.lang])
st.markdown(content['reference_notes_overall'][st.session_state.lang])

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
