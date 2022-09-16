import json
import datetime
import time

# Create and Update Fmeda name
fmeda_name = 'Demo in fmeda test{}'.format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
updated_fmeda_name = 'New test Demo Test FMEDA{}'.format(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

# Calculation Settings $ HE BFR Test Data
with open("test_data\\calculation_settings_test_data.json") as f:
    calculation_settings_test_data = json.load(f)

# Add Cycling Phases Mission Profile
with open("test_data\\cycling_phases_mission_profile.json") as f:
    add_cycling_phases_mission_profile = json.load(f)

# Add Temperature Phases Mission Profile
with open("test_data\\temperature_phases_mission_profile.json") as f:
    add_temperature_phases = json.load(f)

# Add Circuit type
with open("test_data\\circuit_types_and_se_failure_rates.json") as f:
    add_circuit_type_and_se_failure_rates = json.load(f)
# Add TLSRS
with open("test_data\\tlsrs.json") as f:
    add_tlsrs = json.load(f)

# Create New Record Safety Mechanism
with open("test_data\\safety_mechanism.json") as f:
    safety_mechanisms_test_data = json.load(f)






