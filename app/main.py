# imports
import streamlit as st
import util_funcs

con = None

# page info
st.set_page_config(
    layout='centered',
    page_title='Sofia Air',
    page_icon=':cloud:'
)


def form_callback():
    print(st.session_state)
    st.session_state['df'] = util_funcs.show_by_location(
        st.session_state['df'],
        st.session_state['station_selector']
    )


def main():
    st.session_state.lang = 'en'

    content = util_funcs.load_content()

    # load initial data
    st.session_state['df'] = util_funcs.read_data()

    # get selector data
    stations = st.session_state['df']['station_name'].unique()

    if 'FormSubmitter:map_properties-Get information' not in st.session_state:
        st.session_state.click = False
        util_funcs.map(st.session_state['df'], stations, None)
    else:
        if st.session_state['FormSubmitter:map_properties-Get information'] == False:
            util_funcs.map(st.session_state['df'], stations, None)
        else:
            util_funcs.map(st.session_state['df'], stations, None)

    with st.form(key='map_properties'):

        st.multiselect(
            content['ams_selector'][st.session_state.lang],
            options=stations,
            default=stations[0],
            key='station_selector'
        )

        submit_button = st.form_submit_button(
            label='Get information',
            on_click=form_callback()
        )


if __name__ == "__main__":
    main()
