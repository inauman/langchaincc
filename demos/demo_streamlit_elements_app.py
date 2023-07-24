# import streamlit module
import streamlit as st

# import PIL
from PIL import Image

# Title
st.title("StreamLit Demo App")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.text("This is a text")

# Markdown
st.markdown("# Markdown Header")
st.markdown("## Markdown Subheader")
st.markdown("### Markdown Text")


# Error/Colorful Text
st.success("Successful")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")
st.exception(ZeroDivisionError("Trying to divide by Zero"))
#st.help(range)


# Writing Text/Super Fxn
st.write("Text with write")

# Writing Python inbuilt function range
st.write(range(10))

# Display image
img = Image.open("demos/logo.png")
st.image(img, width=50, caption="Simple Image")

# checkbox
if st.checkbox("Show/Hide"):
    st.text("Showing or Hiding Widget")

# Radio Buttons
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive, Activate")

# SelectBox
occupation = st.selectbox("Your Occupation", ["Programmer", "DataScientist", "Doctor", "Businessman"])
st.write("You selected this option: ", occupation)

# MultiSelect
location = st.multiselect("Where do you work?", ("London", "New York", "Accra", "Kiev", "Nepal"))
st.write("You selected", len(location), "locations")

# Buttons
st.button("Click me Button")

if st.button("About"):
    st.text("Streamlit is Cool")

# Slider
age = st.slider("What is your age?", 1, 100, 25)
st.write("Your age is: ", age)

# Text Input
name = st.text_input("Enter your name", "")

if st.button("Submit1"):
    result = name.title()
    st.success(result)





