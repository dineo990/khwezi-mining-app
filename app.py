import streamlit as st

st.title("KHWEZI MINING")
st.write("Health, Safety and Equipment Monitoring Application")

st.header("Login")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):

    if username == "admin" and password == "admin123":
        st.success("Login successful")
        st.write("Welcome Administrator")
        
    elif username == "safety" and password == "safety123":
        st.success("Login successful")
        st.write("Welcome Safety Officer")
        
    elif username == "mining" and password == "mining123":
        st.success("Login successful")
        st.write("Welcome Mining Engineer")
        
    elif username == "maintenance" and password == "maintenance123":
        st.success("Login successful")
        st.write("Welcome Maintenance Engineer")
        
    elif username == "manager" and password == "manager123":
        st.success("Login successful")
        st.write("Welcome Manager")
        
    else:
        st.error("Incorrect username or password")
