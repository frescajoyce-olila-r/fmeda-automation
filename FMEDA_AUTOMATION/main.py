# Import FMEDA_test_steps to call all test steps
import FMEDA_test_steps
# Import and configure logging
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log', level=logging.DEBUG)

if __name__ == '__main__':
    logging.info('--------------------------------------------------')
    logging.info('----- Running FMEDA AUTOMATION script -----')
    logging.info('--------------------------------------------------')
    print('--------------------------------------------------')
    print('----- Running FMEDA AUTOMATION script -----')
    print('--------------------------------------------------')

    # Add FMEDA using rest api call
    FMEDA_test_steps.add_fmeda()

    # Update FMEDA using rest api call
    FMEDA_test_steps.update_fmeda_name()

    # Add TLSRS using rest api call
    FMEDA_test_steps.add_tlsrs()

    # Add create configuration using rest api call
    FMEDA_test_steps.create_configuration()

    # Add cycling phase mission profile using rest api call
    FMEDA_test_steps.add_cycling_phase_mission_profile()

    # Add temperature phase mission profile using rest api call
    FMEDA_test_steps.add_temperature_phase_mission_profile()

    # Add circuit type using rest api call
    FMEDA_test_steps.add_circuit_types()

    # Add safety mechanism using rest api call
    FMEDA_test_steps.add_safety_mechanism()

    # Check results using rest api call
    FMEDA_test_steps.check_results()

    # Export fmeda excel using rest api call
    FMEDA_test_steps.export_fmeda_excel()

    # Delete FMEDA using rest api call
    # FMEDA_test_steps.delete_fmeda()