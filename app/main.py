# imports
import datetime

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
    pass


def main():
    st.session_state.lang = 'en'
    st.session_state['df'] = util_funcs.read_data()
    min_max_date = util_funcs.min_max_date(st.session_state['df'])

    format = 'DD.MM.YYYY'
    st.session_state['min_max_date_df'] = []
    st.session_state['min_max_date_df'].append(
        datetime.datetime.fromisoformat(min_max_date[0]).date()
    )
    st.session_state['min_max_date_df'].append(
        datetime.datetime.fromisoformat(min_max_date[1]).date()
    )

    content = util_funcs.load_content()

    stations = st.session_state['df']['station_name'].unique()
    metrics = st.session_state['df']['param_name'].unique()

    if 'station_selector' not in st.session_state:
        util_funcs.map(st.session_state['df'], stations, None)
    else:
        if 'date_slider' in st.session_state:
            st.session_state.update({
                'df': util_funcs.show_by_time(
                    util_funcs.show_by_location(
                        st.session_state['df'],
                        st.session_state['station_selector']
                    ),
                    st.session_state['date_slider'][0],
                    st.session_state['date_slider'][1]
                ),
            })
        util_funcs.map(st.session_state['df'], stations, None)

    with st.form(key='map_properties'):
        st.multiselect(
            content['ams_selector'][st.session_state.lang],
            options=stations,
            default=stations,
            key='station_selector'
        )

        st.selectbox(
            'Select metric',
            options=metrics,
            key='metric_selector'
        )

        st.slider(
            'Select date',
            min_value=st.session_state['min_max_date_df'][0],
            max_value=st.session_state['min_max_date_df'][1],
            value=(
                st.session_state['min_max_date_df'][0],
                st.session_state['min_max_date_df'][1],
            ),
            format=format,
            key='date_slider'
        )

        submit_button = st.form_submit_button(
            label='Get information',
            on_click=form_callback
        )


if __name__ == "__main__":
    main()
