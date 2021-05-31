##############################################
#### Written By: SATYAKI DE               ####
#### Written On: 30-May-2021              ####
#### Modified On 30-May-2021              ####
####                                      ####
#### Objective: Calling Twilio Voice API  ####
##############################################

import json
from clsConfig import clsConfig as cf
import logging
import os
from twilio.rest import Client

class clsVoiceAPI:
    def __init__(self):
        self.account_sid = cf.conf['TWILIO_ACCOUNT_SID']
        self.auth_token = cf.conf['TWILIO_AUTH_TOKEN']
        self.from_phone = cf.conf['FROM_PHONE']
        self.to_phone = cf.conf['TO_PHONE']

    def sendCall(self, msg):
        try:
            account_sid = self.account_sid
            auth_token = self.auth_token
            from_phone = self.from_phone
            to_phone = self.to_phone

            client = Client(account_sid, auth_token)

            call = client.calls.create(
                            twiml='<Response><Say>' + str(msg) + '</Say></Response>',
                            to=str(from_phone),
                            from_=str(to_phone)
                        )

            resTokenOutput = call.sid
            print('Final Respone: ' + str(resTokenOutput))

            resToken = 0

            return resToken

        except Exception as e:

            x = str(e)
            resToken = 1
            print(x)

            logging.info(x)

            return resToken
