import streamlit as st

st.set_page_config(page_title="Streamlit App", page_icon=":fire:",layout="wide")




st.subheader("Streamlit App")
st.title("Streamlit App")
st.write("Hello World")
st.write("[Learn More](https://www.streamlit.io/)")


# Examples on Streamlit

# 1. Text
# Title
st.title("Streamlit App")
# Header/Subheader
st.header("Streamlit App")
# Subheader
st.subheader("Streamlit App")
# Text
st.write("Hello World")
# Markdown
st.write("[Learn More](https://www.streamlit.io/)")
# Markdown
st.markdown("### Streamlit App")
# 
st.markdown("## Nikhil $")
# Add Equation in Streamlit
st.markdown("$\int_0^\infty x^2 dx$")
st.markdown("**Streamlit App**")
st.markdown("*Streamlit App*")
st.markdown("_Streamlit App_")
st.markdown("__Streamlit App__")
st.markdown("___Streamlit App___")
st.markdown("~~Streamlit App~~")
st.markdown("`Streamlit App`")
st.markdown("```Streamlit App```")
st.markdown("> Streamlit App")
st.markdown(">> Streamlit App")
st.markdown(">>> Streamlit App")
st.markdown(">>>> Streamlit App")
st.markdown(">>>>> Streamlit App")
st.markdown(">>>>>> Streamlit App")
st.markdown(">>>>>>> Streamlit App")
st.markdown(">>>>>>>> Streamlit App")

with st.container():
    st.write("---")
    st.write("This is inside the container")
    st.write("This is also inside the container")

import matplotlib.pyplot as plt
import numpy as np



# Change the size of Plot in Streamlit
cat = ["bored", "happy", "bored", "bored", "happy", "bored"]
dog = ["happy", "happy", "happy", "happy", "bored", "bored"]
activity = ["combing", "drinking", "feeding", "napping", "playing", "washing"]

width = st.slider("plot width", 1, 25, 3)
height = st.slider("plot height", 1, 25, 1)

fig, ax = plt.subplots(figsize=(width, height))
ax.plot(activity, dog, label="dog")
ax.plot(activity, cat, label="cat")
plt.gcf().set_dpi(500)
ax.legend()

st.pyplot(fig)


def SideBar():


    st.markdown(
        """
    <style>
    span[data-baseweb="tag"] {
    background-color: blue !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )


    # Create a container for the sidebar
    menu = st.sidebar.container()
    st.sidebar.title('Contents')


    # Add a menu item to the container
    with menu:
        st.sidebar.header('Main Menu')
        selection = st.sidebar.radio('Select an option', ['Option 1', 'Option 2'])
        
        # Create a submenu for Option 1
        if selection == 'Option 1':
            submenu = st.expander('Submenu')
            with submenu:
                st.write('This is a submenu for Option 1')
        
        # Create a submenu for Option 2
        elif selection == 'Option 2':
            submenu = st.expander('Submenu')
            with submenu:
                st.write('This is a submenu for Option 2')


SideBar()




import plotly.figure_factory as ff

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)





hide_streamlit_style = """
            <style>
            MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 