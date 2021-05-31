#########################################################
#### Written By: SATYAKI DE                          ####
#### Written On: 30-May-2021                         ####
#### Modified On 30-May-2021                         ####
####                                                 ####
#### Objective: Main calling scripts -               ####
#### This Python script will consume an              ####
#### source API data from Azure-Cloud & publish the  ####
#### data into an Oracle Streaming platform,         ####
#### which is compatible with Kafka. Later, another  ####
#### consumer app will read the data from the stream.####
#########################################################

from clsConfig import clsConfig as cf
import clsL as cl
import logging
import datetime
import clsVoiceAPI as ca

# Disbling Warning
def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn

# Lookup functions from
# Azure cloud SQL DB

var = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def main():
    try:
        # Declared Variable
        ret_1 = 0
        debug_ind = 'Y'
        res_2 = ''

        # Defining Generic Log File
        general_log_path = str(cf.conf['LOG_PATH'])

        # Enabling Logging Info
        logging.basicConfig(filename=general_log_path + 'TwillioAPICall.log', level=logging.INFO)

        # Initiating Log Class
        l = cl.clsL()

        # Moving previous day log files to archive directory
        log_dir = cf.conf['LOG_PATH']

        tmpR0 = "*" * 157

        logging.info(tmpR0)
        tmpR9 = 'Start Time: ' + str(var)
        logging.info(tmpR9)
        logging.info(tmpR0)

        print()

        print("Log Directory::", log_dir)
        tmpR1 = 'Log Directory::' + log_dir
        logging.info(tmpR1)

        print('Welcome to the Twilio Voice Calling Program: ')
        print('*' * 160)
        print()

        # Provide a short input text for calls
        voiceCallText = 'Voice From Satyaki, Welcome to the Python World!'

        # Create the instance of the Twilio Voice API Class
        x1 = ca.clsVoiceAPI()

        # Let's pass this to our map section
        resSID = x1.sendCall(voiceCallText)

        if resSID == 0:
            print('Successfully send Audio Message!')
        else:
            print('Failed to send Audio Message!')

        print()


        print('Finished Sending Automated Calls..')
        print("*" * 160)
        logging.info('FFinished Sending Automated Calls..')
        logging.info(tmpR0)

        tmpR10 = 'End Time: ' + str(var)
        logging.info(tmpR10)
        logging.info(tmpR0)

    except ValueError as e:
        print(str(e))
        print("Invalid option!")
        logging.info("Invalid option!")

    except Exception as e:
        print("Top level Error: args:{0}, message{1}".format(e.args, e.message))

if __name__ == "__main__":
    main()
