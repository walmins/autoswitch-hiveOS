#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python2
'''

Hive OS API usage example

Install curl:
easy_install pycurl
pip install pycurl
'''


import pycurl
import sys
import datetime
import urllib
import hmac
import hashlib
import StringIO
import json


argv = sys.argv
argc = len(sys.argv)
null = 0


class HiveAPIExample:

    def __init__(self):
        pass

    __SECRET_KEY = 'my_secret_key'
    """
        Your secret API key, you sign the message with it
        @var string 64 hex chars
        """

    __PUBLIC_KEY = 'my_public_key'
    """
        This is a public key
        @var string 64 hex chars
        """

    __URL = "https://api.hiveos.farm/worker/eypiay.php"
    """
        Api connection URL
        Please use HTTPS, not HTTP for calls for better security.
        @var string
        """


    def run(self):
        self.__log("=== Hive API example ===")

        method = argv[1]

        if method != "multiRocket":
            # run this class methods by name
            m = getattr(self, method)
            result = m()
        else:
            if argc >= 4:
                # at least rig ids and miner required
                # take the arguments from commandline
                result = self.multiRocket(argv[2], argv[3], argv[4], argv[5], argv[6])
            else:
                # To use rocket you have to know what you are doing. Then delete these lines and edit the following.
                self.log("Please edit the source to use multiRocket method")
                exit()

                # this is just an example, use some of your real ids which you get with other methods

                # set everything to rigs ids 1, 2 and 3
                result = self.multiRocket("1,2,3", "claymore", "xmrig", 107800, 800)

                # set bminer to rigs ids 4 and 5, unset second miner
                # ??? result = self.multiRocket("4,5", "bminer", "0", null, null)

        if result is not None:
            # print_r($result);
            print json.dumps(result, indent=4)
            print

    def request(self, params):
        """
            Make API request with given params. Signs the request with secret key.
            @param: array params
            @return array
            """
        params["public_key"] = self.__PUBLIC_KEY
        post_data = urllib.urlencode(params)
	print post_data
        hmac_ = hmac.new(self.__SECRET_KEY, post_data, hashlib.sha256).hexdigest()

        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, self.__URL)
        curl.setopt(pycurl.HTTPHEADER, ['HMAC: ' + str(hmac_)])
        curl.setopt(pycurl.POST, True)
        curl.setopt(pycurl.POSTFIELDS, post_data)
        curl.setopt(pycurl.CONNECTTIMEOUT, 10)
        curl.setopt(pycurl.TIMEOUT, 5)

        buf = StringIO.StringIO()
        curl.setopt(pycurl.WRITEFUNCTION, buf.write)
        curl.perform()

        response = buf.getvalue()

        # Uncomment to debug raw JSON response
        # self.__log("< " + response)

        http_code = curl.getinfo(pycurl.HTTP_CODE)

        curl.close()

        result = json.loads(response)

        if http_code != 200:
            if result["error"]:
                # 404 with some valid JSON
                self.__log("ERROR: HTTP " + str(http_code) + ": " + json.dumps(result["error"]))
            else:
                self.__log("ERROR: HTTP " + str(http_code) + ": " + response)
        else:
            if result is None:
                self.__log("ERROR: Unparsable JSON " + response)
            else:
                if 'error' in result:  # || !$result["result"]
                    self.__log("ERROR: " + json_encode(result["error"]))
                else:
                    result = result["result"]

        return result

    @staticmethod
    def __log(msg):
        str_ = '[' + str(datetime.datetime.today()) + '] ' + msg
        print str_
        # with open(loggerFilename) as log_file:
        #     log_file.write(str_)

    def getRigs(self):
        """
        Rigs list
        """
        params = {
            'method': 'getRigs'
        }
        rigs = self.request(params)
        if 'error ' in rigs:
            return False

        return rigs

    def getWallets(self):
        """
        Wallets list
        """
        params = {
            'method': 'getWallets'
        }
        wallets = self.request(params)
        if 'error' in wallets:
            return False

        return wallets

    def getOC(self):
        """
        Overclocking profiles
        """
        params = {
            'method': 'getOC'
        }
        ocs = self.request(params)
        if 'error' in ocs:
            return False

        return ocs

    def getCurrentStats(self):
        """
        Monitor stats for all the rigs
        """
        params = {
            'method': 'getCurrentStats'
        }
        stats = self.request(params)
        if 'error' in stats:
            return False

        return stats

    def multiRocket(self, rig_ids_str, miner, miner2, id_wal, id_oc):
        """
        Sets parameters for rigs

        @param rig_ids_str coma separated string with rig ids "1,2,3,4"
        @param miner Miner to set. Leave it null if you do not want to change. "claymore", "claymore-z", "ewbf", ...
        @param miner2 Second miner to set. Leave it null if you do not want to change. "0" - if you want to unset it.
        @param id_wal ID of wallet. Leave it null if you do not want to change.
        @param id_oc ID of OC profile. Leave it null if you do not want to change.
        @return bool|mixed
        """
        if rig_ids_str is not None:
            self.log("Rigs ids required")
            exit()

        params = {
            'method': 'multiRocket',
            'rig_ids_str': rig_ids_str,
            'miner': miner,
            'miner2': miner2,
            'id_wal': id_wal,
            'id_oc': id_oc
        }

        result = self.request(params)
        if 'error' in result:
            return False

        return result


if argc <= 1:
    script = sys.argv[0]
    print "Usage: " + script + " methodName aguments"
    print "Examples:"
    print "\t" + script + " getRig"
    print "\t" + script + " getWallets"
    print "\t" + script + " getCurrentStats"
    print "\t" + script + " multiRocket \"rig1,rig2\" [miner] [miner2] [id_wal] [id_oc]"
else:
    api = HiveAPIExample()
    api.run()
