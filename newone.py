import streamlit as st
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%A , %I:%M %p")
st.header(current_time)
monday = {'8 to 9': 'ECON F312 NAB 6109', '9 to 10': 'EEE F215 L1 LTC 5102', '10 to 11': 'EEE F212 L1 LTC 5101', '11 to 12': 'break', '12 to 1': 'ECON F313 L1 NAB 6155', '1 to 2': 'break', '2 to 4': 'EEE F215 P3 FD2 2241', '4 to 5': 'EEE F214 T2 NAB 6161'}
tuesday = {'8 to 9': 'EEE F215 L1 LTC 5102', '9 to 10': 'ECON F312 L1 NAB 6164', '10 to 11': 'ECON F311 L1 NAB 6164', '11 to 12': 'EEE F214 L1 LTC 5102', '12 to 1': 'EEE F211 L1 LTC 5105', '1 to 2': 'break', '2 to 4': 'EEE F211 P1D FD2 2119', '4 to 5': 'ECON F313 T1 NAB 6109'}
wednesday = {'8 to 9': 'ECON F311 T1 NAB 6109', '9 to 10': 'EEE F215 L1 LTC 5102', '10 to 11': 'EEE F212 L1 LTC 5101', '11 to 12': 'break', '12 to 1': 'ECON F313 L1 NAB 6155', '1 to 2': 'break', '2 to 3': 'break', '3 to 4': 'break', '4 to 5': 'EEE F211 T2 NAB 6160'}
thursday = {'8 to 9': 'ECON F313 L1 NAB 6155', '9 to 10': 'ECON F312 L1 NAB 6164', '10 to 11': 'ECON F311 L1 NAB 6164', '11 to 12': 'EEE F214 L1 LTC 5102', '12 to 1': 'EEE F211 L1 LTC 5105', '1 to 2': 'break', '2 to 3':'break', '3 to 4': 'break', '4 to 5': 'EEE F212 L1 LTC 5101'}
friday = {'8 to 9': 'EEE F215 T11 NAB 6105', '9 to 10': 'ECON F312 L1 NAB 6164', '10 to 11': 'ECON F311 L1 NAB 6164', '11 to 12': 'EEE F214 L1 LTC 5102', '12 to 1': 'EEE F211 L1 LTC 5105', '1 to 2':'break', '2 to 3': 'break', '3 to 4': 'break', '4 to 5': 'EEE F212 T1 NAB 6102'}
weekdays = [monday, tuesday, wednesday, thursday, friday]
days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
for da, clas in zip(days, weekdays):
    st.header(da)
    st.write(clas)

    
    