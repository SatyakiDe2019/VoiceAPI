###############################################
#### Written By: SATYAKI DE                ####
#### Written On: 30-May-2021               ####
####                                       ####
#### Objective: This script is a config    ####
#### file, contains all the keys for       ####
#### Twilio Voice API. Application will    ####
#### process these information & perform   ####
#### the call to our registered customers  ####
#### using this configurations.            ####
###############################################

import os
import platform as pl

class clsConfig(object):
    Curr_Path = os.path.dirname(os.path.realpath(__file__))

    os_det = pl.system()
    if os_det == "Windows":
        sep = '\\'
    else:
        sep = '/'

    conf = {
        'APP_ID': 1,
        "comp": "ocid1.compartment.oc1..xxxxxxxxxxxxxxxxxxxxxxxxyyyyyyyyyyyyyyyyyyxxxxxx",
        "TWILIO_ACCOUNT_SID":"AC630f34xxxxxxxxxxxx719yyyyyyyf",
        "TWILIO_AUTH_TOKEN":"62867foeoeoeoeoeoeoeoeoeo2575715",
        "FROM_PHONE":"+18048048484",
        "TO_PHONE":"+15557770396",
        "appType":"application/json",
        "conType":"keep-alive",
        "limRec":10,
        "CACHE":"no-cache",
        "colList": "date, state, positive, negative",
        "typSel": "Cols",
        "LOG_PATH":Curr_Path + sep + 'log' + sep,
        "STREAM_NAME":"Covid19-Stream",
        "PARTITIONS":1
    }
