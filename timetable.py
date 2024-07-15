import pandas as pd
import streamlit as st

timetable = {'InternationalEconomic': {'Tuesday': 3, 'Thursday': 3 , 'Friday': 3, 'Wednesday': 't1'},
'MoneyBankAndMarket' : {'Tuesday': 2 , 'Thursday': 2, 'Friday': 2, 'Monday': 't1'},
'IssuesInEcoDev' : {'Monday': 5, 'Wednesday': 5,'Thursday': 1, 'Tuesday': 't9'},
'ElectroDevices' : {'Tuesday': 4 , 'Thursday': 4 , 'Friday': 4 , 'Monday':'t9'},
'ElectroMagTheory' : {'Monday': 3, 'Wednesday': 3, 'Thursday': 9, 'Friday': 't9'},
'ElectricalMachines' : {'Tuesday': 5, 'Thursday': 5, 'Friday': 5, 'Wednesday': 't9'},
'DigitalDesign': {'Monday': 2, 'Wednesday': 2, 'Tuesday': 1 , 'Friday':'t1' },
}

labs = {'ElectricalMachines_lab': {'Wednesday': [7,8]},
        'DigitalDesign_lab': {'Tuesday': [7,8]}}

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
slots = [f'Slot {i}' for i in range(1, 10)]
df = pd.DataFrame('', index = slots, columns = weekdays)

for class_name, schedule in timetable.items():
    for day, slot in schedule.items():
        if isinstance(slot, int):
            df.at[f'Slot {slot}', day] = class_name
        elif isinstance(slot, str) and slot.startswith('t'):
            slot_num = int(slot[1:])
            df.at[f'Slot {slot_num}', day] = f'{class_name}_tutorial'

for class_name, schedule in labs.items():
    for day,slot in schedule.items():
        if isinstance(slot, list):
            for i in slot:
                df.at[f'Slot {i}', day] = f'{class_name}'
st.dataframe(df)

