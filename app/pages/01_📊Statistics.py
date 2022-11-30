import datetime

import altair as alt
import streamlit as st
import util_funcs

# page info
st.set_page_config(
    layout='wide',
    page_title='Sofia Air',
    page_icon=':cloud:',
)

st.session_state.lang = 'bg'

st.session_state['df'] = util_funcs.read_data()
st.session_state['df_mark_circle'] = st.session_state['df']
st.session_state['df_mark_area'] = st.session_state['df']

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

if 'date_slider_mark_circle' in st.session_state:
    st.session_state.update({
        'df_mark_circle':
            util_funcs.show_by_metrics(
                util_funcs.show_by_time(
                    util_funcs.show_by_location(
                        st.session_state['df'],
                        st.session_state['station_selector_mark_circle']
                    ),
                    st.session_state['date_slider_mark_circle'][0],
                    st.session_state['date_slider_mark_circle'][1]
                ),
                st.session_state['metric_selector_mark_circle']
            )
    })

if 'date_slider_mark_area' in st.session_state:
    st.session_state.update({
        'df_mark_area':
            util_funcs.show_by_metrics(
                util_funcs.show_by_time(
                    util_funcs.show_by_location(
                        st.session_state['df'],
                        st.session_state['station_selector_mark_area']
                    ),
                    st.session_state['date_slider_mark_area'][0],
                    st.session_state['date_slider_mark_area'][1]
                ),
                st.session_state['metric_selector_mark_area']
            )
    })

################ MARK CIRCLE CHART ##################
st.altair_chart(
    alt.Chart(st.session_state['df_mark_circle']).mark_circle().encode(
        x=alt.X('timest:O', title='Date'),  # TODO translate title
        y=alt.Y('param_name:O', title='Metric'),  # TODO translate title
        size='level:Q'
    ).interactive(),
    use_container_width=True
)

with st.form(key='mark_circle'):
    st.slider(
        content['date_selector'][st.session_state.lang],
        min_value=st.session_state['min_max_date_df'][0],
        max_value=st.session_state['min_max_date_df'][1],
        value=(
            st.session_state['min_max_date_df'][0],
            st.session_state['min_max_date_df'][1],
        ),
        format=format,
        key='date_slider_mark_circle'
    )

    st.selectbox(
        content['ams_selector'][st.session_state.lang],
        options=stations,
        key='station_selector_mark_circle'
    )

    st.multiselect(
        content['metric_selector'][st.session_state.lang],
        options=metrics,
        default=metrics,
        key='metric_selector_mark_circle'
    )

    submit_button = st.form_submit_button(
        content['submit_button'][st.session_state.lang],
        on_click=(lambda: None)
    )

################# MARK AREA CHART ###################
st.altair_chart(
    alt.Chart(st.session_state['df_mark_area']).mark_area().encode(
        alt.X(
            'timest:T',
            axis=alt.Axis(format='%Y-%m-%d', domain=False, tickSize=0),
            title='Date'  # TODO translate title
        ),
        alt.Y(
            'level:Q',
            stack='center',
            axis=None
        ),
        alt.Color(
            'param_name:N',
            title='Metric',  # TODO translate title
            scale=alt.Scale(scheme='category20b')
        )
    ).interactive(),
    use_container_width=True
)

with st.form(key='mark_area'):
    st.slider(
        content['date_selector'][st.session_state.lang],
        min_value=st.session_state['min_max_date_df'][0],
        max_value=st.session_state['min_max_date_df'][1],
        value=(
            st.session_state['min_max_date_df'][0],
            st.session_state['min_max_date_df'][1],
        ),
        format=format,
        key='date_slider_mark_area'
    )

    st.selectbox(
        content['ams_selector'][st.session_state.lang],
        options=stations,
        key='station_selector_mark_area'
    )

    st.multiselect(
        content['metric_selector'][st.session_state.lang],
        options=metrics,
        default=metrics,
        key='metric_selector_mark_area'
    )

    submit_button = st.form_submit_button(
        content['submit_button'][st.session_state.lang],
        on_click=(lambda: None)
    )

################### SIDEBAR #########################
with st.sidebar:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.button(
            label='EN',
            key='en'
        )
    with col2:
        st.button(
            label='BG',
            key='bg'
        )

################### LANGUAGE #########################
if st.session_state.en:
    st.session_state.lang = 'en'
else:
    st.session_state.lang = 'bg'
