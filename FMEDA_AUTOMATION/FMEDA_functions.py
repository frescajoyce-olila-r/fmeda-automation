# Import json library to process encoding and decoding of JSON
import json
# Import sys library to process encoding and decoding of JSON
import sys
# Use to save excel file to a directory
import os
# Import and configure logging
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log', level=logging.DEBUG)


def get_fmeda_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # Check if key 'Data' exist from the response
    if 'Data' in response:
        # return fmeda ID
        return response['Data'][0]['Id']


def get_tlsrs_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # return tlsrs_id
    return response['Data'][0]['Id']


def get_analysis_template_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # Check if key 'Data' exist from the response
    if 'Data' in response:
        # return analysis template id
        return response['Data'][0]['Id']
    else:
        # return analysis template id
        return response['Data']['Id']


def get_calc_params_and_bfr_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # return calculation settings id
    return response['Id']


def get_cycling_phases_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # return cycling_phases_id
    return response['Data'][0]['Id']


def get_temperature_phases_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # return temperature_phases_id
    return response['Data'][0]['Id']


def get_safety_mechanism_id(response_json):
    # Get json response text of rest api call
    response = json.loads(response_json.text)
    # Check if key 'Data' exist from the response
    if 'Data' in response:
        # return safety mechanism id
        return response['Data'][0]['Id']


def add_check_response_and_validate(add_response, get_all_response, id_name, id_response_text,
                                    id_test_data, name_test_data, function_name):
    # Check the post rest api response call
    if add_response.status_code == 200:

        # Get all data to check if data is added
        get_all_data_response = get_all_response
        print('{} {}'.format(id_name, id_test_data))
        logging.info('{} {}'.format(id_name, id_test_data))

        # Check if FMEDA is created/added
        if get_all_data_response.status_code == 200:
            response = json.loads(get_all_data_response.text)
            validation_result = 'Validation: Fail'
            # Check if key 'Data' exist
            if 'Data' in response:
                for i in response['Data']:

                    # Check if the created/added value exist using its ID
                    if i[id_response_text] == id_test_data:
                        print("{} {} has been added".format(name_test_data, function_name))
                        logging.info("{} {} has been added".format(name_test_data, function_name))
                        validation_result = 'Validation: Pass'
                print(validation_result)
                logging.info(validation_result)

            # If key 'Data' does not exist
            else:
                for i in response:

                    # Check if the created/added value exist using its ID
                    if i[id_response_text] == id_test_data:
                        print("{} {} has been added".format(name_test_data, function_name))
                        logging.info("{} {} has been added".format(name_test_data, function_name))
                        validation_result = 'Validation: Pass'
                print(validation_result)
                logging.info(validation_result)
        else:
            print('{} does not return data'.format(function_name))
            logging.warning('{} does not return data'.format(function_name))
    else:
        print('Error: {}{}'.format(add_response.status_code, add_response.text))
        logging.warning('Error: {}{}'.format(add_response.status_code, add_response.text))
        sys.exit(1)


def delete_check_response_and_validate(delete_response, get_all_response, id_name, id_response_text,
                                       id_test_data, name_test_data, function_name):
    # Check the post rest api response call
    if delete_response.status_code == 200:

        # Get all data to check if data is deleted
        get_all_data_response = get_all_response
        print('{} {}'.format(id_name, id_test_data))
        logging.info('{} {}'.format(id_name, id_test_data))

        # Check if FMEDA is deleted
        if get_all_data_response.status_code == 200:
            response = json.loads(get_all_data_response.text)
            validation_result = 'Validation: Fail'
            delete_msg_response = "{} {} has not been deleted".format(name_test_data, function_name)
            # Check if key 'Data' exist
            if 'Data' in response:
                for i in response['Data']:
                    if i[id_response_text] != id_test_data:
                        # Check if the created/added value exist using its ID
                        delete_msg_response = "{} {} has been deleted".format(name_test_data, function_name)
                        validation_result = 'Validation: Pass'

                print(delete_msg_response)
                logging.info(delete_msg_response)
                print(validation_result)
                logging.info(validation_result)

            # If key 'Data' does not exist
            else:
                for i in response:
                    if i[id_response_text] != id_test_data:
                        # Check if the deleted fmeda exist using its ID
                        delete_msg_response = "{} {} has been deleted".format(name_test_data, function_name)
                        validation_result = 'Validation: Pass'

                print(delete_msg_response)
                logging.info(delete_msg_response)
                print(validation_result)
                logging.info(validation_result)
        else:
            print('{} does not return data'.format(function_name))
            logging.warning('{} does not return data'.format(function_name))
    else:
        print('Error: {}{}'.format(delete_response.status_code, delete_response.text))
        logging.warning('Error: {}{}'.format(delete_response.status_code, delete_response.text))
        sys.exit(1)


def update_check_response_and_validate(add_update_response, get_all_response, id_name, id_value, original_name,
                                       name_response_text, updated_name, function_name):
    # Check the post rest api response call
    if add_update_response.status_code == 200:
        # Get all data to check if data is added
        get_all_data_response = get_all_response
        print('{} {}'.format(id_name, id_value))
        logging.info('{} {}'.format(id_name, id_value))

        # Check if FMEDA is added/updated
        if get_all_data_response.status_code == 200:
            response = json.loads(get_all_data_response.text)
            validation_result = 'Validation: Fail'

            # Check if key 'Data' exist
            if 'Data' in response:
                for i in response['Data']:

                    # Check if the updated/added value exist using its ID
                    if i[name_response_text] == updated_name:
                        print("{} {} has been updated to {}".format(original_name, function_name, updated_name))
                        logging.info("{} {} has been updated to {}".format(original_name, function_name, updated_name))
                        validation_result = 'Validation: Pass'
                print(validation_result)
                logging.info(validation_result)
            # If key 'Data' does not exist
            else:
                for i in response:

                    # Check if the created/added value exist using its ID
                    if i[name_response_text] == updated_name:
                        print("{} {} has been updated to {}".format(original_name, function_name, updated_name))
                        logging.info("{} {} has been updated to {}".format(original_name, function_name, updated_name))
                        validation_result = 'Validation: Pass'
                    print(validation_result)
                    logging.info(validation_result)
        else:
            print('{} does not return data'.format(function_name))
            logging.warning('{} does not return data'.format(function_name))
    else:
        print('Error: {}{}'.format(add_update_response.status_code, add_update_response.text))
        logging.warning('Error: {}{}'.format(add_update_response.status_code, add_update_response.text))
        sys.exit(1)


def generate_excel_export(response):
    # Check the rest api response call
    if response.status_code == 200:

        # Split the filename from the response body of get rest api call
        filename_split = response.headers.get('content-disposition')
        t = filename_split.split(';')[2]

        # Filename of the Fmeda excel file to export
        filename = t.split("filename*=UTF-8''")[1]

        # Join the file path and filename
        file_path = os.path.join('Excel', filename)

        # If path does not exist it will automatically created
        if not os.path.isdir('Excel'):
            os.mkdir('Excel')

        # Generate Fmeda excel file
        file = open(file_path, 'wb')
        file.write(response.content)
        file.close()
        print('Fmeda excel file has been exported')
        logging.info('Fmeda excel file has been exported')
    else:
        print("Error: {}{}".format(response.status_code, response.text))
        logging.warning("Error: {}{}".format(response.status_code, response.text))
        sys.exit(1)


