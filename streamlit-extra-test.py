import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.app_logo import add_logo
from streamlit_extras.badges import badge
from streamlit_extras.bottom_container import bottom
from streamlit_extras.button_selector import button_selector
from streamlit_extras.buy_me_a_coffee import button
import logging
from streamlit_extras.capture import stdout, logcapture
import pandas as pd
import altair as alt
from streamlit_extras.card import card
import numpy as np
import time
from streamlit_extras.colored_header import colored_header
from streamlit_extras.customize_running import center_running
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.echo_expander import echo_expander
from streamlit_extras.function_explorer import function_explorer
from streamlit_extras.image_coordinates import streamlit_image_coordinates
import requests
from PIL import Image
from io import BytesIO
from streamlit_extras.image_selector import image_selector
from streamlit_extras.image_selector import show_selection
from streamlit_extras.jupyterlite import jupyterlite
from streamlit_extras.keyboard_text import key, load_key_css
from streamlit_extras.mandatory_date_range import date_range_picker
import textwrap
from streamlit_extras.mention import mention
from streamlit_extras.no_default_selectbox import selectbox
from prometheus_client import Counter
from streamlit_extras.sandbox import sandbox
from streamlit_extras.stoggle import stoggle
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.theme import st_theme
from streamlit_extras.toggle_switch import st_toggle_switch
from streamlit_extras.vertical_slider import vertical_slider
   
# Initialize session state for page selection if it doesn't exist
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'page_1'

# Define pages
def page_1():
    st.title("👽  Add Vertical Space")
    add_n_lines = st.slider("Add n vertical lines below this", 1, 20, 5)
    add_vertical_space(add_n_lines)
    st.write("Here is text after the nth line!")


def page_2():
    st.title("👸  Altex")
    st.text("Not working")
    # Add more elements specific to Page 2 here

def page_3():
    from annotated_text import annotated_text

    annotated_text(
        "This ",
        ("is", "verb", "#8ef"),
        " some ",
        ("annotated", "adj", "#faa"),
        ("text", "noun", "#afa"),
        " for those of ",
        ("you", "pronoun", "#fea"),
        " who ",
        ("like", "verb", "#8ef"),
        " this sort of ",
        ("thing", "noun", "#afa"),
    )

# Define page 4 with the example code
def page_4():
    from streamlit_extras.app_logo import add_logo

    if st.checkbox("Use url", value=True):
        add_logo("https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/500px-Google_2015_logo.svg.png")
    else:
        add_logo("gallery/kitty.jpeg", height=300)
    st.write("👈 Check out the cat in the nav-bar!")

# Define page 5 with the example code
def page_5():
    from streamlit_extras.badges import badge

    badge(type="pypi", name="plost")
    badge(type="pypi", name="streamlit")
    badge(type="buymeacoffee", name="andfanilo")

# Define page 6 with the example code
def page_6():
    from streamlit_extras.bottom_container import bottom

    st.write("This is the main container")

    with bottom():
        st.write("This is the bottom container")
        st.text_input("This is a text input in the bottom container")

# Define page 7 with the example code
def page_7():
    from streamlit_extras.button_selector import button_selector

    month_list = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    selected_index = button_selector(
        month_list,
        index=0,
        spec=4,
        key="button_selector_example_month_selector",
        label="Month Selector",
    )
    st.write(f"Selected month: {month_list[selected_index]}")

# Define page 8 with the example code
def page_8():
    from streamlit_extras.buy_me_a_coffee import button

    button(username="fake-username", floating=False, width=221)

# Define page 9 with the example code
def page_9():
    from streamlit_extras.camera_input import camera_input_live

    st.write("# See a new image every second")
    controls = st.checkbox("Show controls")
    image = camera_input_live(show_controls=controls)
    if image is not None:
        st.image(image)

# Define page 10 with the example code
def page_10():
    output = st.empty()
    with stdout(output.code, terminator=""):
        print("This is some captured stdout")
        print("How about that, Isn't it great?")
        if st.button("Click to print more"):
            print("You added another line!")

    # Example for log capture
    logger = logging.getLogger("examplelogger")
    logger.setLevel("DEBUG")
    with logcapture(st.empty().code, from_logger=logger):
        logger.error("Roses are red")
        logger.info("Violets are blue")
        logger.warning("This warning is yellow")
        logger.debug("Your code is broke, too")

# Define page 11 with the card example
def page_11():
    card(
        title="Hello World!",
        text="Some description",
        image="http://placekitten.com/300/250",
        url="https://www.google.com",
    )

# Define page 12 with the chart example
def page_12() -> None:
    data: pd.DataFrame = get_data()  # Ensure get_data() is defined elsewhere in your code
    chart: alt.TopLevelMixin = get_chart(data=data)  # Ensure get_chart() is defined elsewhere in your code

    chart += get_annotations_chart(
        annotations=[
            ("Mar 01, 2008", "Pretty good day for GOOG"),
            ("Dec 01, 2007", "Something's going wrong for GOOG & AAPL"),
            ("Nov 01, 2008", "Market starts again thanks to..."),
            ("Dec 01, 2009", "Small crash for GOOG after..."),
        ],
    )

    st.altair_chart(chart, use_container_width=True)  # type: ignore

# Function to generate random data for the chart
def _get_random_data():
    return pd.DataFrame(
        np.random.randn(10, 2),
        columns=["a", "b"]
    )

# Define page 13 with the chart examples
def page_13():
    chart_data = _get_random_data()
    
    # Example one
    with st.container():  # Using st.container for the chart
        st.write("Here's a cool chart")
        st.area_chart(chart_data)

    # Example two
    with st.container():  # Using st.container for the chart
        st.write(
            "I can use a subset of the data for my chart... "
            "but still give all the necessary context in "
            "`chart_container`!"
        )
        st.area_chart(chart_data[["a", "b"]])

# Define page 14 with the colored header example
def page_14():
    colored_header(
        label="My New Pretty Colored Header",
        description="This is a description",
        color_name="violet-70",
    )

# Define page 15 with the heavy computation example
def page_15():
    @concurrency_limiter(max_concurrency=1)
    def heavy_computation():
        st.write("Heavy computation")
        progress_text = "Operation in progress. Please wait."
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.15)
            my_bar.progress(percent_complete + 1, text=progress_text)
        st.write("END OF Heavy computation")
        return 42

    my_button = st.button("Run heavy computation")

    if my_button:
        heavy_computation()

# Define page 16 with the running widget example
def page_16():
    click = st.button("Observe where the 🏃‍♂️ running widget is now!")
    if click:
        center_running()  # Ensure center_running() is defined elsewhere in your code
        time.sleep(2)

# Define page 17 with the dataframe explorer example
def page_17():
    dataframe = generate_fake_dataframe(
        size=500, cols="dfc", col_names=("date", "income", "person"), seed=1
    )
    filtered_df = dataframe_explorer(dataframe, case=False)
    st.dataframe(filtered_df, use_container_width=True)

# Define page 18 with the echo expander examples
def page_18():
    # Example 1
    with echo_expander():
        import streamlit as st

        st.markdown(
            """
            This component is a combination of `st.echo` and `st.expander`.
            The code inside the `with echo_expander()` block will be executed,
            and the code can be shown/hidden behind an expander.
            """
        )

    # Example 2
    with echo_expander(code_location="below", label="Simple Dataframe example"):
        import pandas as pd
        import streamlit as st

        df = pd.DataFrame(
            [[1, 2, 3, 4, 5], [11, 12, 13, 14, 15]],
            columns=("A", "B", "C", "D", "E"),
        )
        st.dataframe(df)

# Define page 19 with the GitHub and GitLab examples
def page_19():
    st.subheader("GitHub Gist Example")
    github_gist(
        "https://gist.github.com/randyzwitch/be8c5e9fb5b8e7b046afebcac12e5087/",
        width=700,
        height=400,
    )

    st.subheader("GitLab Snippet Example")
    gitlab_snippet(
        "https://gitlab.com/snippets/1995463",
        width=700,
        height=200,
    )

# Define page 20 with the Streamlit Faker example
def page_20():
    fake = get_streamlit_faker(seed=42)
    fake.markdown()
    fake.info(icon="💡", body="You can also pass explicit parameters!")
    fake.selectbox()
    fake.slider()
    fake.metric()
    fake.altair_chart()

# Define page 21 with the function explorer example
def page_21():
    def foo(age: int, name: str, image_url: str = "http://placekitten.com/120/120"):
        st.write(f"Hey! My name is {name} and I'm {age} years old")
        st.write("Here's a picture")
        st.image(image_url)

    function_explorer(foo)

# Define page 22 with the grid example
def page_22():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    my_grid = grid(2, [2, 4, 1], 1, 4, vertical_align="bottom")

    # Row 1:
    my_grid.dataframe(random_df, use_container_width=True)
    my_grid.line_chart(random_df, use_container_width=True)
    # Row 2:
    my_grid.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    my_grid.text_input("Your name")
    my_grid.button("Send", use_container_width=True)
    # Row 3:
    my_grid.text_area("Your message", height=40)
    # Row 4:
    my_grid.button("Example 1", use_container_width=True)
    my_grid.button("Example 2", use_container_width=True)
    my_grid.button("Example 3", use_container_width=True)
    my_grid.button("Example 4", use_container_width=True)
    # Row 5 (uses the spec from row 1):
    with my_grid.expander("Show Filters", expanded=True):
        st.slider("Filter by Age", 0, 100, 50)
        st.slider("Filter by Height", 0.0, 2.0, 1.0)
        st.slider("Filter by Weight", 0.0, 100.0, 50.0)
    my_grid.dataframe(random_df, use_container_width=True)

# Define page 23 with the image coordinates example
def page_23():
    st.markdown("# Click on the image")
    last_coordinates = streamlit_image_coordinates("https://placekitten.com/200/300")

    st.write(last_coordinates)

# Define page 24 with the dataframe example
def page_24():
    # Create a sample DataFrame with a 'Flag' column containing URLs
    data = {
        "Name": ["Item 1", "Item 2", "Item 3"],
        "Flag": [
            "https://placekitten.com/120/120",
            "https://placekitten.com/121/121",
            "https://placekitten.com/122/122",
        ],
    }
    df = pd.DataFrame(data)

    st.caption("Input dataframe (notice 'Flag' column is full of URLs)")
    st.write(df)
    df_html = table_with_images(df=df, url_columns=("Flag",))
    st.caption("Output")
    st.markdown(df_html, unsafe_allow_html=True)

# Define page 25 with the image selection example
def page_25():
    response = requests.get(
        "https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500"
    )

    image = Image.open(BytesIO(response.content))

    selection_type = st.radio(
        "Selection type", ["lasso", "box"], index=0, horizontal=True
    )

    selection = image_selector(image=image, selection_type=selection_type)
    if selection:
        st.json(selection, expanded=False)
        show_selection(image, selection)

# Define page 26 with the JupyterLite example
def page_26():
    jupyterlite(1500, 1600)

# Define page 27 with the key example
def page_27():
    st.subheader("Key Example")
    
    # Example with default key
    load_key_css()
    key("⌘+K")
    
    # Example with inline key
    st.write(
        f"Also works inline! Example: {key('⌘+K', write=False)}",
        unsafe_allow_html=True,
    )

# Define page 28 with the keyboard example
def page_28():
    # Main function
    keyboard_to_url(key="S", url="https://www.github.com/streamlit/streamlit")

    load_key_css()
    st.write(
        f"""Now hit {key("S", False)} on your keyboard...!""",
        unsafe_allow_html=True,
    )

# Define page 29 with the rain example
def page_29():
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )

# Define page 30 with the date range picker example
def page_30():
    st.write(
        """
        This is an example of a date range picker that *always* returns a start and
        end date, even if the user has only selected one of the dates. Until the
        user selects both dates, the app will not run.
        """
    )
    result = date_range_picker("Select a date range")
    st.write("Result:", result)

# Define page 31 with the collapsible content example
def page_31():
    mdlit(
        textwrap.dedent(
            """
    ??? Bonus
        @(🎁)(A very insightful tutorial)(https://www.youtube.com/watch?v=dQw4w9WgXcQ)
    """
        )
    )

# Define page 32 with the mention examples
def page_32():
    st.subheader("Mention Examples")

    # Example 1
    mention(
        label="An awesome Streamlit App",
        icon="streamlit",  # Some icons are available... like Streamlit!
        url="https://extras.streamlitapp.com",
    )

    # Example 2
    mention(
        label="streamlit-extras",
        icon="🪢",  # You can also just use an emoji
        url="https://github.com/arnaudmiribel/streamlit-extras",
    )

    # Example 3
    mention(
        label="example-app-cv-model",
        icon="github",  # GitHub is also featured!
        url="https://github.com/streamlit/example-app-cv-model",
    )

    # Example 4
    mention(
        label="That page somewhere in Notion",
        icon="notion",  # Notion is also featured!
        url="https://notion.so",
    )

    # Example 5
    inline_mention = mention(
        label="streamlit",
        icon="twitter",  # Twitter is also featured!
        url="https://www.twitter.com/streamlit",
        write=False,
    )

    st.write(
        f"Here's how to use the mention inline:  {inline_mention}. Cool right?",
        unsafe_allow_html=True,
    )

# Define page 33 with the metric example
def page_33():
    col1, col2, col3 = st.columns(3)

    col1.metric(label="Gain", value=5000, delta=1000)
    col2.metric(label="Loss", value=5000, delta=-1000)
    col3.metric(label="No Change", value=5000, delta=0)

    style_metric_cards()

# Define page 34 with the selectbox example
def page_34():
    st.write(
        """
        This is an example of a selectbox that returns None unless the user has
        explicitly selected one of the options.

        The selectbox below has no default value, so it will return None until the
        user selects an option.
        """
    )
    result = selectbox("Select an option", ["A", "B", "C"])
    st.write("Result:", result)

    result = selectbox(
        "Select an option with different label",
        ["A", "B", "C"],
        no_selection_label="<None>",
    )
    st.write("Result:", result)

# Define page 35 with the Prometheus metrics example
def page_35():
    @st.cache_resource
    def get_metric():
        registry = streamlit_registry()  # Ensure streamlit_registry() is defined elsewhere in your code
        return Counter(
            name="my_counter",
            documentation="A cool counter",
            labelnames=("app_name",),
            registry=registry,  # important!!
        )

    SLIDER_COUNT = get_metric()

    app_name = st.text_input("App name", "prometheus_app")
    latest = st.slider("Latest value", 0, 20, 3)
    if st.button("Submit"):
        SLIDER_COUNT.labels(app_name).inc(latest)

    st.write(
        """
        View a fuller example that uses the (safer) import metrics method at:
        https://github.com/arnaudmiribel/streamlit-extras/tree/main/src/streamlit_extras/prometheus/example
        """
    )

    st.write(
        """
        ### Example output at `{host:port}/_stcore/metrics`
        ```
        # TYPE my_counter counter
        # HELP my_counter A cool counter
        my_counter_total{app_name="prometheus_app"} 14.0
        my_counter_created{app_name="prometheus_app"} 1.7042185907557938e+09
        ```
        """
    )

# Define page 36 with the grid example
def page_36():
    random_df = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    row1 = row(2, vertical_align="center")
    row1.dataframe(random_df, use_container_width=True)
    row1.line_chart(random_df, use_container_width=True)

    row2 = row([2, 4, 1], vertical_align="bottom")

    row2.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
    row2.text_input("Your name")
    row2.button("Send", use_container_width=True)

# Define page 37 with the embedded app example
def page_37():
    def embedded_app():
        import numpy as np
        import pandas as pd
        import plotly.express as px
        import streamlit as st

        @st.cache_data
        def get_data():
            dates = pd.date_range(start="01-01-2020", end="01-01-2023")
            data = np.random.randn(len(dates), 1).cumsum(axis=0)
            return pd.DataFrame(data, index=dates, columns=["Value"])

        data = get_data()

        value = st.slider(
            "Select a range of values",
            int(data.min()),
            int(data.max()),
            (int(data.min()), int(data.max())),
        )
        filtered_data = data[(data["Value"] >= value[0]) & (data["Value"] <= value[1])]
        st.plotly_chart(px.line(filtered_data, y="Value"))

    sandbox(embedded_app)

# Define page 38 with the keyup example
def page_38():
    st.write("## Notice how the output doesn't update until you hit enter")
    out = st.text_input("Normal text input")
    st.write(out)
    st.write("## Notice how the output updates with every key you press")
    out2 = st_keyup("Keyup input")
    st.write(out2)

# Define page 39 with the star rating example
def page_39():
    st.text("10/10 would watching")
    star_rating(5)

# Define page 40 with the button example
def page_40():
    if button("Button 1", key="button1"):
        if button("Button 2", key="button2"):
            if button("Button 3", key="button3"):
                st.write("All 3 buttons are pressed")

# Define page 41 with the chat example
def page_41():
    with chat(key="my_chat"):
        if prompt := st.chat_input():
            add_message("user", prompt, avatar="🧑‍💻")

            def stream_echo():
                for word in prompt.split():
                    yield word + " "
                    time.sleep(0.15)

            add_message("assistant", "Echo: ", stream_echo, avatar="🦜")

# Define page 42 with the to-do example
def page_42():
    to_do(
        [(st.write, "☕ Take my coffee")],
        "coffee",
    )
    to_do(
        [(st.write, "🥞 Have a nice breakfast")],
        "pancakes",
    )
    to_do(
        [(st.write, ":train: Go to work!")],
        "work",
    )

# Define page 43 with the stoggle example
def page_43():
    stoggle(
        "Click me!",
        """🥷 Surprise! Here's some additional content""",
    )

# Define page 44 with the streaming example
def page_44():
    def stream_example():
        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(0.1)

        # Also supports any other object supported by `st.write`
        yield pd.DataFrame(
            np.random.randn(5, 10),
            columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
        )

        for word in _LOREM_IPSUM.split():
            yield word + " "
            time.sleep(0.05)

    if st.button("Stream data"):
        write(stream_example)

# Define page 45 with the stylable container example
def page_45():
    with stylable_container(
        key="green_button",
        css_styles="""
            button {
                background-color: green;
                color: white;
                border-radius: 20px;
            }
            """,
    ):
        st.button("Green button")

    st.button("Normal button")

    with stylable_container(
        key="container_with_border",
        css_styles="""
            {
                border: 1px solid rgba(49, 51, 63, 0.2);
                border-radius: 0.5rem;
                padding: calc(1em - 1px)
            }
            """,
    ):
        st.markdown("This is a container with a border.")

# Define page 46 with the switch page example
def page_46():
    want_to_contribute = st.button("I want to contribute!")
    if want_to_contribute:
        switch_page("Contribute")

# Define page 47 with the tagger example
def page_47():
    tagger_component("Here is a feature request", ["p2", "🚩triaged", "backlog"])
    tagger_component(
        "Here are colored tags",
        ["turtle", "rabbit", "lion"],
        color_name=["blue", "orange", "lightblue"],
    )
    tagger_component(
        "Annotate the feature",
        ["hallucination"],
        color_name=["blue"],
    )

# Define page 48 with the theme example
def page_48():
    adjust = st.toggle("Make the CSS adjustment")

    st.write("Input:")
    st.code(
        f"""
        st.write("Lorem ipsum")
        st_theme(adjust={adjust})
        st.write("Lorem ipsum")
        """
    )

    st.write("Output:")
    st.write("Lorem ipsum")
    st_theme(adjust=adjust)
    st.write("Lorem ipsum")

# Define page 49 with the toggle switch example
def page_49():
    st.write("## Toggle Switch")
    st_toggle_switch(
        label="Enable Setting?",
        key="switch_1",
        default_value=False,
        label_after=False,
        inactive_color="#D3D3D3",  # optional
        active_color="#11567f",  # optional
        track_color="#29B5E8",  # optional
    )

# Define page 50 with the vertical slider example
def page_50():
    st.write("## Vertical Slider")
    vertical_slider(
        key="slider",
        default_value=25,
        step=1,
        min_value=0,
        max_value=100,
        track_color="gray",  # optional
        thumb_color="blue",  # optional
        slider_color="red",  # optional
    )

# Define page 51 with the word importance example
def page_51():
    text = (
        "Streamlit Extras is a library to help you discover, learn, share and"
        " use Streamlit bits of code!"
    )
    html = format_word_importances(
        words=text.split(),
        importances=(0.1, 0.2, 0, -1, 0.1, 0, 0, 0.2, 0.3, 0.8, 0.9, 0.6, 0.3, 0.1, 0, 0, 0),  # fmt: skip
    )
    st.write(html, unsafe_allow_html=True)

# Create sidebar navigation with buttons styled as text
def sidebar_navigation():
    st.sidebar.title("Navigation")
    
    # Create clickable buttons for each page
    pages = {
        'page_1': '👽  Add Vertical Space',
        'page_2': '👸  Altex',
        'page_3': '🖊️  Annotated text',
        'page_4': '🐱  App logo',  # Existing page
        'page_5': '🏷️  Badges',  # Existing page
        'page_6': '⬇️  Bottom Container',  # Existing page
        'page_7': '🔢  Button Selector',  # Existing page
        'page_8': '☕  Buy Me a Coffee Button',  # Existing page
        'page_9': '📸  Camera input live',  # Existing page
        'page_10': '🥅  Capture',  # Existing page
        'page_11': '💳️  Card',  # Existing page
        'page_12': '⬇  Chart annotations',  # Existing page
        'page_13': '🖼️  Chart container',  # Existing page
        'page_14': '🖌️  Color ya Headers',  # Existing page
        'page_15': '🚦  Concurrency limiter for your Streamlit app',  # Existing page
        'page_16': '🏃‍♂️  Customize running',  # Existing page
        'page_17': '📊  DataFrame Explorer',  # Existing page
        'page_18': '📜  Echo Expander',  # Existing page
        'page_19': '📁  GitHub & GitLab Snippets',  # Existing page
        'page_20': '🎭  Streamlit Faker',  # Existing page
        'page_21': '🔍  Function Explorer',  # Existing page
        'page_22': '📊  Grid Example',  # Existing page
        'page_23': '🖼️  Image Coordinates',  # Existing page
        'page_24': '📊  DataFrame with Images',  # Existing page
        'page_25': '🖼️  Image Selector',  # Existing page
        'page_26': '📓  JupyterLite Example',  # Existing page
        'page_27': '⌨️  Key Example',  # Existing page
        'page_28': '⌨️  Keyboard Example',  # Existing page
        'page_29': '🌧️  Rain Animation',  # Existing page
        'page_30': '📅  Date Range Picker',  # Existing page
        'page_31': '📚  Collapsible Content',  # Existing page
        'page_32': '🔗  Mention Examples',  # Existing page
        'page_33': '📊  Metric Example',  # Existing page
        'page_34': '🔄  Selectbox Example',  # Existing page
        'page_35': '📈  Prometheus Metrics Example',  # Existing page
        'page_36': '📊  Grid Example',  # Existing page
        'page_37': '🔄  Embedded App Example',  # Existing page
        'page_38': '⌨️  Keyup Example',  # Existing page
        'page_39': '⭐  Star Rating Example',  # Existing page
        'page_40': '🔘  Button Example',  # Existing page
        'page_41': '💬  Chat Example',  # Existing page
        'page_42': '📝  To-Do Example',  # Existing page
        'page_43': '🔄  Stoggle Example',  # Existing page
        'page_44': '📡  Streaming Example',  # Existing page
        'page_45': '🎨  Stylable Container Example',  # Existing page
        'page_46': '🔄  Switch Page Example',  # Existing page
        'page_47': '🏷️  Tagger Example',  # New page added
        'page_48': '🎨  Theme Example',  # New page added
        'page_49': '🔄  Toggle Switch Example',  # New page added
        'page_50': '📊  Vertical Slider Example',  # New page added
        'page_51': '📜  Word Importance Example'  # New page added
    }
    
    # Custom CSS to make buttons look like text with reduced spacing
    st.markdown("""
        <style>
        .stButton button {
            width: 100%;
            text-align: left;
            padding: 4px 8px;  /* Reduced vertical padding */
            background: none;
            border: none;
            color: #000000;
            margin: -15px 0;    /* Negative margin to reduce gap */
        }
        .stButton button:hover {
            background-color: #f0f2f6;
        }
        .stButton button:active {
            background-color: #e6e9ef;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Create buttons for navigation
    for page_id, page_name in pages.items():
        if st.sidebar.button(
            page_name,
            key=page_id,
            help=f"Navigate to {page_name}"
        ):
            st.session_state.current_page = page_id

# Main app logic
def main():
    # Add sidebar navigation
    sidebar_navigation()
    
    # Render the correct page based on session state
    match st.session_state.current_page:
        case 'page_2':
            page_2()
        case 'page_3':
            page_3()
        case 'page_4':
            page_4()
        case 'page_5':
            page_5()
        case 'page_6':
            page_6()
        case 'page_7':
            page_7()
        case 'page_8':
            page_8()
        case 'page_9':
            page_9()
        case 'page_10':
            page_10()
        case 'page_11':
            page_11()
        case 'page_12':
            page_12()
        case 'page_13':
            page_13()
        case 'page_14':
            page_14()
        case 'page_15':
            page_15()
        case 'page_16':
            page_16()
        case 'page_17':
            page_17()
        case 'page_18':
            page_18()
        case 'page_19':
            page_19()
        case 'page_20':
            page_20()
        case 'page_21':
            page_21()
        case 'page_22':
            page_22()
        case 'page_23':
            page_23()
        case 'page_24':
            page_24()
        case 'page_25':
            page_25()
        case 'page_26':
            page_26()
        case 'page_27':
            page_27()
        case 'page_28':
            page_28()
        case 'page_29':
            page_29()
        case 'page_30':
            page_30()
        case 'page_31':
            page_31()
        case 'page_32':
            page_32()
        case 'page_33':
            page_33()
        case 'page_34':
            page_34()
        case 'page_35':
            page_35()
        case 'page_36':
            page_36()
        case 'page_37':
            page_37()
        case 'page_38':
            page_38()
        case 'page_39':
            page_39()
        case 'page_40':
            page_40()
        case 'page_41':
            page_41()
        case 'page_42':  # New case for page 42
            page_42()
        case 'page_43':  # New case for page 43
            page_43()
        case 'page_44':  # New case for page 44
            page_44()
        case 'page_45':  # New case for page 45
            page_45()
        case 'page_46':  # New case for page 46
            page_46()
        case 'page_47':  # New case for page 47
            page_47()
        case 'page_48':  # New case for page 48
            page_48()
        case 'page_49':  # New case for page 49
            page_49()
        case 'page_50':  # New case for page 50
            page_50()
        case 'page_51':  # New case for page 51
            page_51()
        case _:
            page_1()

if __name__ == "__main__":
    main()