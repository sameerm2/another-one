import streamlit as st
from PIL import Image,ImageDraw
from member_v2 import *  #change the member_v2 to your own python file

def son():
    # Page title and description
    st.markdown("<h1 style='text-align: center; color: black;'>Medical Information</h1>", unsafe_allow_html=True)
    #st.markdown("Enter the medical details of a person")

    # Load and display image
    

    # Sidebar for user inputs
    with st.sidebar:
        #st.subheader("Personal Details")
        name = "Sudip Mondal"
        age = 24
        gender = "Male"
        height = "5"
        weight = "60"
        BP="70/100"
        SL=200
        HR=100
        Allergies="None"
        Dieseases="None"



    # Main content to display medical information
    st.write("---")
    if name and age and gender and height and weight:
        #st.markdown("## Medical Information")

        # Create columns
        col1, col2,col3 = st.columns([2, 2 , 2])

        # Display details in columns and rows
        with col1:
            


            image = Image.open("data/boy.jpg")

# Create a circular mask
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the image
            image_with_mask = Image.new("RGBA", image.size)
            image_with_mask.paste(image, (0, 0), mask=mask)

# Add a red border to the image
            border_width = 1
            image_with_border = Image.new("RGBA", (image.size[0] + border_width * 2, image.size[1] + border_width * 2), (255, 0, 0, 255))
            image_with_border.paste(image_with_mask, (border_width, border_width))
            

# Display the modified image
            st.image(image_with_border, caption="Son", use_column_width=True)

        

        with col2:
            st.write("Name:",name)
            st.write("Age:",age)
            st.write("Gender:",gender)
            st.write("Height:",height)
            st.write("Weight:",weight)

        with col3:
            st.write("Blood Pressure:",BP)
            st.write("Sugar level:",SL)
            st.write("Heart rate:",HR)
            st.write("Allergies:",Allergies)
            st.write("Dieseases:",Dieseases)

    member_page()

def daughter():
    st.markdown("<h1 style='text-align: center; color: black;'>Medical Information</h1>", unsafe_allow_html=True)
    #st.markdown("Enter the medical details of a person")

    # Load and display image
    

    # Sidebar for user inputs
    with st.sidebar:
        #st.subheader("Personal Details")
        name = "Riya Dey"
        age = 21
        gender = "female"
        height = "5"
        weight = "60"
        BP="70/100"
        SL=200
        HR=100
        Allergies="None"
        Dieseases="None"



    # Main content to display medical information
    st.write("---")
    if name and age and gender and height and weight:
        #st.markdown("## Medical Information")

        # Create columns
        col1, col2,col3 = st.columns([2, 2 , 2])

        # Display details in columns and rows
        with col1:
            


            image = Image.open("data/boy.jpg")

# Create a circular mask
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the image
            image_with_mask = Image.new("RGBA", image.size)
            image_with_mask.paste(image, (0, 0), mask=mask)

# Add a red border to the image
            border_width = 1
            image_with_border = Image.new("RGBA", (image.size[0] + border_width * 2, image.size[1] + border_width * 2), (255, 0, 0, 255))
            image_with_border.paste(image_with_mask, (border_width, border_width))
            

# Display the modified image
            st.image(image_with_border, caption="Daughter", use_column_width=True)

        

        with col2:
            st.write("Name:",name)
            st.write("Age:",age)
            st.write("Gender:",gender)
            st.write("Height:",height)
            st.write("Weight:",weight)

        with col3:
            st.write("Blood Pressure:",BP)
            st.write("Sugar level:",SL)
            st.write("Heart rate:",HR)
            st.write("Allergies:",Allergies)
            st.write("Dieseases:",Dieseases)

    member_page()

def daughter_in_law():
    st.markdown("<h1 style='text-align: center; color: black;'>Medical Information</h1>", unsafe_allow_html=True)
    #st.markdown("Enter the medical details of a person")

    # Load and display image
    

    # Sidebar for user inputs
    with st.sidebar:
        #st.subheader("Personal Details")
        name = "Riya Dey"
        age = 21
        gender = "female"
        height = "5"
        weight = "60"
        BP="70/100"
        SL=200
        HR=100
        Allergies="None"
        Dieseases="None"



    # Main content to display medical information
    st.write("---")
    if name and age and gender and height and weight:
        #st.markdown("## Medical Information")

        # Create columns
        col1, col2,col3 = st.columns([2, 2 , 2])

        # Display details in columns and rows
        with col1:
            


            image = Image.open("data/boy.jpg")

# Create a circular mask
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the image
            image_with_mask = Image.new("RGBA", image.size)
            image_with_mask.paste(image, (0, 0), mask=mask)

# Add a red border to the image
            border_width = 1
            image_with_border = Image.new("RGBA", (image.size[0] + border_width * 2, image.size[1] + border_width * 2), (255, 0, 0, 255))
            image_with_border.paste(image_with_mask, (border_width, border_width))
            

# Display the modified image
            st.image(image_with_border, caption="Daughter-in-law", use_column_width=True)

        

        with col2:
            st.write("Name:",name)
            st.write("Age:",age)
            st.write("Gender:",gender)
            st.write("Height:",height)
            st.write("Weight:",weight)

        with col3:
            st.write("Blood Pressure:",BP)
            st.write("Sugar level:",SL)
            st.write("Heart rate:",HR)
            st.write("Allergies:",Allergies)
            st.write("Dieseases:",Dieseases)

    member_page()
    
def grandson():
    st.markdown("<h1 style='text-align: center; color: black;'>Medical Information</h1>", unsafe_allow_html=True)
    #st.markdown("Enter the medical details of a person")

    # Load and display image
    

    # Sidebar for user inputs
    with st.sidebar:
        #st.subheader("Personal Details")
        name = "Rahul Sen"
        age = 10
        gender = "Male"
        height = "4ft 10 inch"
        weight = "40"
        BP="70/100"
        SL=200
        HR=100
        Allergies="None"
        Dieseases="None"



    # Main content to display medical information
    st.write("---")
    if name and age and gender and height and weight:
        #st.markdown("## Medical Information")

        # Create columns
        col1, col2,col3 = st.columns([2, 2 , 2])

        # Display details in columns and rows
        with col1:
            


            image = Image.open("data/boy.jpg")

# Create a circular mask
            mask = Image.new("L", image.size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, image.size[0], image.size[1]), fill=255)

# Apply the mask to the image
            image_with_mask = Image.new("RGBA", image.size)
            image_with_mask.paste(image, (0, 0), mask=mask)

# Add a red border to the image
            border_width = 1
            image_with_border = Image.new("RGBA", (image.size[0] + border_width * 2, image.size[1] + border_width * 2), (255, 0, 0, 255))
            image_with_border.paste(image_with_mask, (border_width, border_width))
            

# Display the modified image
            st.image(image_with_border, caption="Grandson", use_column_width=True)

        

        with col2:
            st.write("Name:",name)
            st.write("Age:",age)
            st.write("Gender:",gender)
            st.write("Height:",height)
            st.write("Weight:",weight)

        with col3:
            st.write("Blood Pressure:",BP)
            st.write("Sugar level:",SL)
            st.write("Heart rate:",HR)
            st.write("Allergies:",Allergies)
            st.write("Dieseases:",Dieseases)

    member_page()
