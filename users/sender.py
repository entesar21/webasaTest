from kavenegar import *
#import ghasedak
import requests



def send_otp(otp):
    # print("otp password")
    # print(otp.password)
    # print(otp.receiver)
    # sms = ghasedak.Ghasedak("6e4fc36673e14ecb73e5505c69ceea57a28e5dd0b5f362f5b59244c613ae89a0")
    # sms.send({'message': otp.password, 'receptor': otp.receiver, 'linenumber': "10008566"})
    #
    #

    try:
        print("otp password")
        print(otp.password)
        print(otp.receiver)
        # api = KavenegarAPI('31525A514A637A554361795035644E4475495A654C36472B377755636F767830494A482F686768525038493D')
        # params = {'sender': '10008663', 'receptor': otp.receiver, 'message': otp.password}
        # # print(str(params))
        # #print(str(api.sms_send(params)))
        # response = api.sms_send(params)
        # # print (response)
    except APIException as e:
        print (str(e))
    except HTTPException as e:
        print (str(e))
