# Import the request HTTP library for python
import requests

# Import HTTPBasicAuth to handle the required authentication for the web services
from requests.auth import HTTPBasicAuth

# Import json library to process encoding and decoding of JSON
import json

# Import sys library to perform sys.exit
import sys

# use the read() method of SafeConfigParser to read the configuration file.
import config

# All test data has been stored to to TestData class
import FMEDA_test_data

# Import run_var class to get all ID's that will be use
import run_var

# Read all data from excel file
import xlrd

# Import and configure logging
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log', level=logging.DEBUG)


def add_fmeda(fmeda_name):

    # The REST API path
    path_uri = '/api/Fmedas?FmedaName={}'.format(fmeda_name)

    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_fmeda():
    # The REST API path
    path_uri = '/api/Fmedas?page=0&pageSize=0&sorts=[object Object]' \
               '&filters=[object Object]&groups=[object Object]&aggregates=[object Object]'

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def delete_fmeda(fmeda_id):

    # The REST API path
    path_uri = '/api/Fmedas/{}'.format(fmeda_id)

    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.delete(config.host + path_uri,
                               auth=HTTPBasicAuth(config.username, config.password),
                               verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def update_fmeda(fmeda_name_to_update, fmeda_id_update):
    # The REST API path
    path_uri = '/api/Fmedas/{}?FmedaName={}'.format(fmeda_id_update, fmeda_name_to_update)
    # Send the PUT request
    # Return the result of the PUT request
    try:
        return requests.put(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def add_new_tlsrs(tlsrs_name, tlsrs_def, ffm, target_asil):
    # The REST API path
    path_uri = "/api/Tlsrs/{}?Name={}&Definition={}&IsFunctionalFailureMode={}&TargetAsil={}".format(run_var.FMEDA_ID,
                                                                                                     tlsrs_name,
                                                                                                     tlsrs_def, ffm,
                                                                                                     target_asil)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_tlsrs(fmeda_id):
    # The REST API path
    path_uri = "/api/Tlsrs/{}?page=0&pageSize=0&sorts=[object Object]&filters=[object Object]" \
               "&groups=[object Object]&aggregates=[object Object]".format(fmeda_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def create_configuration():
    # The REST API path
    path_uri = "/api/fmeda/{}/HeBfrs".format(run_var.FMEDA_ID)
    data = FMEDA_test_data.calculation_settings_test_data
    # Send the POST request
    # Return the result of the POST request
    try:

        headers = {
            'accept': '*/*',
            'Content-Type': 'application/json',
        }
        return requests.post(config.host + path_uri,
                             data=json.dumps(data), headers=headers, verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_configuration(fmeda_id):
    # The REST API path
    path_uri = "/api/fmeda/{}/HeBfrs".format(fmeda_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def cycling_phase_mission_profile(number_of_cycles, temperature_difference, consider_self_heating):
    # The REST API path
    path_uri = "/api/IecCyclingProfile/{}?NumberOfCycles={}&TemperatureDifference={}&ConsiderSelfHeating={}".format(
        run_var.CALC_PARAMS_AND_BFR_ID, number_of_cycles, temperature_difference, consider_self_heating)

    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_cycling_phase_mission_profile(calc_params_bfr_id):
    # The REST API path
    path_uri = "/api/IecCyclingProfile/{}?page=0&pageSize=0&sorts=[object Object]&" \
               "filters=[object Object]&groups=[object Object]".format(calc_params_bfr_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def temperature_phases_mission_profile(amb_temp_case_in_celsius, operating_time_in_hours):
    # The REST API path
    path_uri = "/api/IecTemperatureProfile/{}?AmbTempCaseInCelsius={}&OperatingTimeInHours={}".format(
        run_var.CALC_PARAMS_AND_BFR_ID, amb_temp_case_in_celsius, operating_time_in_hours)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_temperature_phases(calc_params_bfr_id):
    # The REST API path
    path_uri = "/api/IecTemperatureProfile/{}?page=0&pageSize=0&sorts=[object Object]&" \
               "filters=[object Object]&groups=[object Object]&aggregates=[object Object]".format(calc_params_bfr_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def add_circuit_types(name, unit, alpha_se_density, neutron_se_density, total_size, total_transistor, total_area,
                      IsPackage):
    # The REST API path
    path_uri = "/api/CircuitTypes/{}?" \
               "Name={}" \
               "&Unit={}" \
               "&AlphaSeDensity={}" \
               "&NeutronSeDensity={}" \
               "&TotalSize={}" \
               "&TotalTransistorCount={}" \
               "&TotalArea={}" \
               "&IsPackage={}".format(run_var.FMEDA_ID, name, unit, alpha_se_density,
                                      neutron_se_density, total_size, total_transistor, total_area, IsPackage)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_circuit_types(fmeda_id):
    # The REST API path
    path_uri = "/api/CircuitTypes/{}?page=0&pageSize=0&sorts=[object Object]&filters=[object Object]&groups=[object" \
               " Object]&aggregates=[object Object]".format(fmeda_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def add_safety_mechanism(tag, name, fmc_rf, fmc_mpf_reporting, comment, safety_function_description,
                         failure_ext, failure_in, all_blocks, all_sw_units_implementing_sm,
                         sm_repetition_time, sm_maximum_reaction_time, sm_functional_in_operating_mode,
                         ic_failure_reaction_at_interface_to_system, rationale_for_diagnostic_coverage, sm_available):
    # The REST API path
    path_uri = "/api/SafetyMechanisms/{}" \
               "?Tag={}" \
               "&Name={}" \
               "&FmcRf={}" \
               "&FmcMpfReporting={}" \
               "&Comment={}" \
               "&SafetyFunctionDescription={}" \
               "&FailureDiagnosisForExternalFaults={}" \
               "&FailureDiagnosisForInternalHwBlocks={}" \
               "&AllHwBlocksImplementingSm={}" \
               "&AllSwUnitsImplementingSm={}" \
               "&SmRepetitionTime={}" \
               "&SmMaximumReactionTime={}" \
               "&SmFunctionalInOperatingMode={}" \
               "&IcFailureReactionAtInterfaceToSystem={}" \
               "&RationaleForDiagnosticCoverage={}" \
               "&SmAvailable={}".format(run_var.FMEDA_ID, tag, name, fmc_rf, fmc_mpf_reporting, comment, safety_function_description,
                                        failure_ext, failure_in, all_blocks, all_sw_units_implementing_sm,
                                        sm_repetition_time, sm_maximum_reaction_time, sm_functional_in_operating_mode,
                                        ic_failure_reaction_at_interface_to_system, rationale_for_diagnostic_coverage,
                                        sm_available)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def get_all_safety_mechanisms(fmeda_id):
    # The REST API path
    path_uri = "/api/SafetyMechanisms/{}?page=0&pageSize=0&sorts=[object Object]" \
               "&filters=[object Object]&groups=[object Object]&aggregates=[object".format(fmeda_id)

    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri,
                            auth=HTTPBasicAuth(config.username, config.password),
                            verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def check_results():
    # The REST API path
    path_uri = "/api/fmeda/{}/Calculations".format(run_var.FMEDA_ID)
    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri, auth=HTTPBasicAuth(config.username, config.password), verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


def generate_customer_fmeda_excel_file(fmeda_id, calculation_settings_id, tlsrs_id):
    # The REST API path
    path_uri = "/api/fmeda/{}/Excel?calculationSettingsId={}{}&" \
               "createSnapshot=true&showColumnB=true&showIecMetrics=true".\
                format(fmeda_id, calculation_settings_id, tlsrs_id)
    # Send the GET request
    # Return the result of the GET request
    try:
        return requests.get(config.host + path_uri, auth=HTTPBasicAuth(config.username, config.password), verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


# BUG - NOT YET FIXED
# Not yet working
def add_architectural_elements(name, element_class, voltage_domain_name, clock_domain_name, comment):
    # The REST API path
    path_uri = "/api/ArchitecturalElements{}?Name={}&ElementClass={}&VoltageDomainName={}" \
               "&ClockDomainName={}&Comment={}".format(run_var.FMEDA_ID, name, element_class,
                                                       voltage_domain_name, clock_domain_name, comment)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


# BUG - NOT YET FIXED
# Not yet working
def add_associations(analysis_group_id, architectural_elements_id):
    # The REST API path
    path_uri = "/api/FailureModes/{}?ArchitecturalElementId={}".format(analysis_group_id, architectural_elements_id)
    # Send the POST request
    # Return the result of the POST request
    try:
        return requests.post(config.host + path_uri,
                             auth=HTTPBasicAuth(config.username, config.password),
                             verify=False)
    except requests.exceptions.RequestException as e:
        print('Error: {}'.format(e))
        sys.exit(1)


# Not yet working
# Compare excel file data from web page
def check_results_summary(file_path):
    # "Excel\Annisand2020-03-12%2011%3A15%3A47_master_20200312_0316.xlsm"
    # File path of the exported excel
    wb = xlrd.open_workbook(file_path)
    wb.sheet_names()
    sheet_fmeda_results = wb.sheet_by_index(2)
    # For row 0 and column 0
    # sheet.cell_value(4, 4)
    for i in range(4, sheet_fmeda_results.nrows):
        print(sheet_fmeda_results.cell_value(i, 4))