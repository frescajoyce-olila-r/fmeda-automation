# Import json library to process encoding and decoding of JSON
import json
# Import TestData class to get all testdata
import FMEDA_test_data
# Import run_var class to get all ID's that will be use
import run_var
# Import sys library to perform sys.exit
import sys
# Fmeda common functions
import FMEDA_functions
# Fmeda rest api
import FMEDA_api
# Import time library use to delay time
import time
# Import and configure logging
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log', level=logging.DEBUG)


def add_fmeda():
    # Add fmeda using rest api call
    add_fmeda_response = FMEDA_api.add_fmeda(FMEDA_test_data.fmeda_name)
    # Store fmeda_id to run_var class
    run_var.FMEDA_ID = FMEDA_functions.get_fmeda_id(add_fmeda_response)
    # Check the response of rest apo call and validate
    FMEDA_functions.add_check_response_and_validate(add_fmeda_response, FMEDA_api.get_all_fmeda(),
                                                    'FMEDA_ID: ', 'Id', run_var.FMEDA_ID, FMEDA_test_data.fmeda_name,
                                                    'FMEDA')


def delete_fmeda():
    # Add fmeda using rest api call
    delete_fmeda_response = FMEDA_api.delete_fmeda(run_var.FMEDA_ID)
    # Check the response of rest apo call and validate
    FMEDA_functions.delete_check_response_and_validate(delete_fmeda_response, FMEDA_api.get_all_fmeda(),
                                                       'FMEDA_ID: ', 'Id', run_var.FMEDA_ID, FMEDA_test_data.fmeda_name,
                                                       'FMEDA')


def update_fmeda_name():
    # Update fmeda name using rest api call
    update_fmeda_response = FMEDA_api.update_fmeda(FMEDA_test_data.updated_fmeda_name, run_var.FMEDA_ID)
    # Update check response and validate
    FMEDA_functions.update_check_response_and_validate(update_fmeda_response, FMEDA_api.get_all_fmeda(), 'FMEDA_ID: ',
                                                       run_var.FMEDA_ID, FMEDA_test_data.fmeda_name, 'FmedaName',
                                                       FMEDA_test_data.updated_fmeda_name, 'UPDATE FMEDA NAME')


def add_tlsrs():
    # Loop all test data for tlsrs
    for testdata in FMEDA_test_data.add_tlsrs:
        # Add tlsrs using rest api call
        add_new_tlsrs_response = FMEDA_api.add_new_tlsrs(testdata['tlsrs_name'], testdata['tlsrs_definition'],
                                                    testdata['ffm'], testdata['target_asil'])
        # Store tlsrs id to run_var class
        run_var.TLSRS_ID.append(FMEDA_functions.get_tlsrs_id(add_new_tlsrs_response))
        # Check response and validate
        FMEDA_functions.add_check_response_and_validate(add_new_tlsrs_response,
                                                        FMEDA_api.get_all_tlsrs(run_var.FMEDA_ID), 'TLSRS_ID: ', 'Id',
                                                        FMEDA_functions.get_tlsrs_id(add_new_tlsrs_response),
                                                        testdata['tlsrs_name'], 'TLSRS')


def create_configuration():
    # Create new configuration using rest api call
    create_new_configuration_response = FMEDA_api.create_configuration()
    # Store calculation settings id to run_var class
    run_var.CALC_PARAMS_AND_BFR_ID = FMEDA_functions.get_calc_params_and_bfr_id(create_new_configuration_response)
    # Check response and validate
    FMEDA_functions.add_check_response_and_validate(create_new_configuration_response,
                                                    FMEDA_api.get_all_configuration(run_var.FMEDA_ID),
                                                    "CALC_PARAMS_AND_BFR_ID:", 'Id', run_var.CALC_PARAMS_AND_BFR_ID,
                                                    FMEDA_test_data.calculation_settings_test_data['Name'], 'CONFIGURATION')


def add_cycling_phase_mission_profile():
    # get temperature difference and number of cycle value from TestData
    temperature = FMEDA_test_data.add_cycling_phases_mission_profile['TemperatureDifference']
    initial_cycle = FMEDA_test_data.add_cycling_phases_mission_profile['NumberOfCycles']
    for i in range(temperature, 42):
        # If self healing number is even then true if not false
        self_healing = True
        if i % 2 != 0:
            self_healing = False
        # increment value every next cycle of loop
        temperature = i
        # Add 10 every next cycle of loop
        initial_cycle += 10
        # Add cycling phase mission profile using rest api call
        cycling_phase_mission_profile_response = FMEDA_api.cycling_phase_mission_profile\
            (initial_cycle, temperature, self_healing)
        run_var.CYCLING_PHASES_ID = FMEDA_functions.get_cycling_phases_id(cycling_phase_mission_profile_response)
        # Check response and validate
        FMEDA_functions.add_check_response_and_validate(cycling_phase_mission_profile_response,
                                                        FMEDA_api.get_all_cycling_phase_mission_profile
                                                        (run_var.CALC_PARAMS_AND_BFR_ID), 'CYCLING_PHASES_MISSION_ID:',
                                                        'Id', run_var.CYCLING_PHASES_ID, '', '')
        print('CYCLING PHASES MISSION_PROFILE [{}] [{}] [{}]'.format(initial_cycle, temperature, self_healing))
        logging.info('CYCLING PHASES MISSION_PROFILE [{}] [{}] [{}]'.format(initial_cycle, temperature, self_healing))


def add_temperature_phase_mission_profile():
    # get amb_temp_case_celcius  and operating_time_in_hours value from TestData
    amb_temp_case_in_celsius = FMEDA_test_data.add_temperature_phases['AmbTempCaseInCelsius']
    operating_time_in_hours = FMEDA_test_data.add_temperature_phases['OperatingTimeInHours']
    # Loop amb_temp_case_in_celsius from TestData
    for i in range(amb_temp_case_in_celsius, 43):
        # increment value every next cycle of loop
        amb_temp_case_in_celsius = i
        # Add 10 every next cycle of loop
        operating_time_in_hours += 10
        # Add Temperature Phases Mission Profile using rest api call
        temperature_phase_mission_profile_response = \
            FMEDA_api.temperature_phases_mission_profile(amb_temp_case_in_celsius, operating_time_in_hours)
        run_var.TEMPERATURE_PHASES_ID = \
            FMEDA_functions.get_temperature_phases_id(temperature_phase_mission_profile_response)
        # Check response and validate
        FMEDA_functions.add_check_response_and_validate(temperature_phase_mission_profile_response,
                                                        FMEDA_api.get_all_temperature_phases(
                                                            run_var.CALC_PARAMS_AND_BFR_ID),
                                                        'TEMPERATURE_PHASES_MISSION_ID:', 'Id',
                                                        run_var.TEMPERATURE_PHASES_ID, '', '')
        print('TEMPERATURE PHASES MISSION_PROFILE [{}] [{}]'.format(amb_temp_case_in_celsius, operating_time_in_hours))
        logging.info('TEMPERATURE PHASES MISSION_PROFILE [{}] [{}]'.format(amb_temp_case_in_celsius, operating_time_in_hours))


def add_circuit_types():
    # Loop all test data for circuit types
    for testdata in FMEDA_test_data.add_circuit_type_and_se_failure_rates:
        # Add circuit type using rest api call
        add_circuit_type_response = FMEDA_api.add_circuit_types(testdata['Name'], testdata['Unit'],
                                                                testdata['AlphaSeDensity'], testdata['NeutronSeDensity'],
                                                                testdata['TotalSize'], testdata['TotalTransistorCount'],
                                                                testdata['TotalArea'], testdata['IsPackage'])
        # Store analysis_template_id to run_var class
        run_var.ANALYSIS_TEMPLATE_ID = FMEDA_functions.get_analysis_template_id(add_circuit_type_response)
        # Check response and validate
        FMEDA_functions.add_check_response_and_validate(add_circuit_type_response,
                                                        FMEDA_api.get_all_circuit_types(run_var.FMEDA_ID),
                                                        'ANALYSIS_TEMPLATE_ID: ', 'Id', run_var.ANALYSIS_TEMPLATE_ID,
                                                        testdata['Name'], 'CIRCUIT TYPE')


def add_safety_mechanism():
    # Loop all test data for safety mechanisms
    for testdata in FMEDA_test_data.safety_mechanisms_test_data:
        # Add Safety Mechanisms using rest api call
        if testdata['tag'] == 'EDC':
            testdata['SmAvailable'] = 'True'
            testdata['FmcRf'] = 0.75
            testdata['FmcMpfReporting'] = 0.8
        add_safety_mechanisms_response = FMEDA_api.add_safety_mechanism(testdata['tag'], testdata['name'], testdata['FmcRf'],
                                                                   testdata['FmcMpfReporting'], testdata['comment'],
                                                                   testdata['SafetyFunctionDescription'],
                                                                   testdata['Failure_Ext'], testdata['Failure_In'],
                                                                   testdata['all_blocks'],
                                                                   testdata['AllSwUnitsImplementingSm'],
                                                                   testdata['SmRepetitionTime'],
                                                                   testdata['SmMaximumReactionTime'],
                                                                   testdata['SmFunctionalInOperatingMode'],
                                                                   testdata['IcFailureReactionAtInterfaceToSystem'],
                                                                   testdata['RationaleForDiagnosticCoverage'],
                                                                   testdata['SmAvailable'])
        # Store safety mechanism id for validation
        run_var.SAFETY_MECHANISM = FMEDA_functions.get_safety_mechanism_id(add_safety_mechanisms_response)
        # Check response and validate
        FMEDA_functions.add_check_response_and_validate(add_safety_mechanisms_response,
                                                        FMEDA_api.get_all_safety_mechanisms(run_var.FMEDA_ID),
                                                        'SAFETY MECHANISM ID:', 'Id', run_var.SAFETY_MECHANISM,
                                                        testdata['name'], 'SAFETY MECHANISM')


def check_results():
    time.sleep(2)
    # Get results through GET rest api call
    get_results_response = FMEDA_api.check_results()
    # Check response call
    if get_results_response.status_code == 200:
        # get json response text
        response_json = json.loads(get_results_response.text)
        # result value
        result = 'FMEDA Result: Passed [having no NaN values]'
        result_fail = 'FMEDA Result : Failed [having NaN values]'

        # Loop all the data from json response text
        for result_arr in range(0, len(response_json)):
            for data in response_json[result_arr]['Value']['Value']:
                for i in response_json[result_arr]['Value']['Value'][data]:
                    # Check values if it does not have 'NaN' values result is pass Else result is fail
                    if response_json[result_arr]['Value']['Value'][data]['LambdaTotal'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaNp'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaSpf'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaRf'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaDpfDet'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaDpfLat'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaSafe'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaSafetyRelated'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['Spfm'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['Lfm'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaRaw'] == 'NaN':
                        result = result_fail
                    elif response_json[result_arr]['Value']['Value'][data]['LambdaUndet'] == 'NaN':
                        result = result_fail

        print(result)
        logging.info(result)
    else:
        print("Error: {}{}".format(get_results_response.status_code, get_results_response.text))
        logging.warning("Error: {}{}".format(get_results_response.status_code, get_results_response.text))
        sys.exit(1)


def export_fmeda_excel():
    # delay 1 sec to avoid [502] bad gateway
    time.sleep(1)
    tlsrs_id = ''
    for i in run_var.TLSRS_ID:
        # get tlsrs id and store together to use for get excel rest api call
        tlsrs_id += '&tlsrIds={}'.format(i)

    # get results using GET rest api call
    generate_excel_file_response = FMEDA_api.generate_customer_fmeda_excel_file(run_var.FMEDA_ID,
                                                                                run_var.CALC_PARAMS_AND_BFR_ID,
                                                                                tlsrs_id)
    # generate fmeda excel file
    FMEDA_functions.generate_excel_export(generate_excel_file_response)