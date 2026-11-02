import streamlit as st
from numpy.core import records

from Blood_donor_view import BloodDonorManager

donor_instance = BloodDonorManager()

tab1, tab2 = st.tabs(["ADD", "VIEW"])

with tab1:
    st.header("Add New Donors")

    Donor_Name = st.text_input("Enter Donor Name ")
    Contact = st.text_input("Enter Donor Contact Number ")
    Blood_Group = st.selectbox("Select Blood Group", ["A+","B+","AB+","O+","A-","B-","AB-","O-"])
    Place = st.text_input("Enter Donor City")
    Last_Donation = st.text_input("Enter Last Donation ")
    if st.button("Add New Donor"):
        donor_instance.post(name=Donor_Name, blood_group=Blood_Group, city=Place, phone=Contact, last_donation=Last_Donation)
        st.success("New Donor Added Successfully")
with tab2:
    st.header("View Donor Details")
    records=donor_instance.get()
    # st.table(records)
    if records:
        st.table(records)
    else:
        st.warning("No Donor Details Found...!")