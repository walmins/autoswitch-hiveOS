#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# v => 0.4
# by walmins
# python3
# last modification: 20180407
# source https://forum.hiveos.farm/discussion/192/hive-api
import requests
import json
import hmac
import hashlib
import urllib
import pycurl
import base64
import io
import datetime
import time
from VARS import *
import logging

greaterProfit = 20
debug = True

def minerHiveOS(params):
	params["public_key"] = PUBLIC_KEY
	post_data = urllib.parse.urlencode(params)
	HMAC = hmac.new(SECRET_KEY.encode(), post_data.encode(), hashlib.sha256).hexdigest()
	curl = pycurl.Curl()
	curl.setopt(pycurl.URL, URL)
	curl.setopt(pycurl.HTTPHEADER, ['HMAC: ' + str(HMAC)])
	curl.setopt(pycurl.POST, True)
	curl.setopt(pycurl.POSTFIELDS, post_data)
	curl.setopt(pycurl.CONNECTTIMEOUT, 10)
	curl.setopt(pycurl.TIMEOUT, 5)
	buf = io.BytesIO()
	curl.setopt(pycurl.WRITEFUNCTION, buf.write)
	try:
		curl.perform()
		response = buf.getvalue()

		# Uncomment to debug raw JSON response
		# self.__log("< " + response)
		http_code = curl.getinfo(pycurl.HTTP_CODE)
		curl.close()
		result = json.loads(response)
		return result
	except pycurl.error:
		# ret = e.args[0]
		# print ("error-- ",ret)
		return False

# Monitor stats for all the rigs
def getCurrentStats():
	logging.info("*** getCurrentStats ***")
	currentStats = {}
	params = {
		'method': 'getCurrentStats'
	}
	currentStats['rigID'] = str(RIG_ID)
	stats = minerHiveOS(params)
	if stats:
		#currentStats['algo'] = list(stats['result']['summary']['algo'].keys())[0]
		currentStats['miner'] = stats['result']['rigs'][currentStats['rigID']]['miner']
		currentStats['walletID'] = stats['result']['rigs'][currentStats['rigID']]['id_wal']
		currentStats['walletName'] =  stats['result']['rigs'][currentStats['rigID']]['wallet_name']
		return currentStats
	else:
		return False

# Sets parameters for rigs
def multiRocket(rig_ids_str, miner, id_wal):
	"""
	@param rig_ids_str coma separated string with rig ids "1,2,3,4"
	@param miner Miner to set. Leave it null if you do not want to change. "claymore", "claymore-z", "ewbf", ...
	@param miner2 Second miner to set. Leave it null if you do not want to change. "0" - if you want to unset it.
	@param id_wal ID of wallet. Leave it null if you do not want to change.
	@param id_oc ID of OC profile. Leave it null if you do not want to change.
	@return bool|mixed
	"""

	params = {
		'method': 'multiRocket',
		'rig_ids_str': rig_ids_str,
		'miner': miner,
		'id_wal': id_wal,
	}

	result = minerHiveOS(params)
	if 'error' in result:
		return False

	return result

def getProfitCoin():
	logging.info("*** getProfitCoin ***")
	profitability = {}
	url_opener = urllib.request.build_opener()
	url_opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
	try:
	    response = url_opener.open(SRC['whattomine']['url'])
	    string = response.read().decode('utf-8')
	    json_obj = json.loads(string)
	except:
	    json_obj = {'coins': {}}
	    print ("error")
	for coin_set in json_obj['coins'].items():
		coin = coin_set[1]
		if coin['algorithm'] in profitability:	
			if profitability.get(coin['algorithm']) < coin['profitability']:
				profitability[coin['algorithm']] = coin['profitability']
		else:
			profitability[coin['algorithm']] = coin['profitability']
	if debug == True:
		print (profitability)
	return profitability

if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
	logging.info("Start autoswitchHiveOS")
	while True:
		try:
			CurrentStats = getCurrentStats()
			logging.info("=== My Stats === ")
			logging.info("RIG ID: %s", CurrentStats['rigID'])
			logging.info("Wallet ID: %s", CurrentStats['walletID'])
			logging.info("Miner: %s", CurrentStats['miner'])
			#logging.info("Algo: %s", CurrentStats['algo'])		
			ProfitCoin = getProfitCoin()
			for coins in wallets.items():
				if CurrentStats['walletID'] == coins[1]['id_wal']:
					print (coins[0])
					CurrentStats['wtmAlgo'] = coins[0]
					if CurrentStats['wtmAlgo'] in ProfitCoin.keys():
						CurrentStats['profit'] = ProfitCoin[CurrentStats['wtmAlgo']]
					else:
						CurrentStats['profit'] = 0
			if 'wtmAlgo' in CurrentStats:
				if debug == True:
					print (CurrentStats)
				currentProfit = (ProfitCoin[list(ProfitCoin.keys())[0]])
				logging.info("Curent WTM Profit: %s (%s)", currentProfit, list(ProfitCoin.keys())[0])
				logging.info("My Profit: %s", CurrentStats['profit'])
				if currentProfit > (CurrentStats['profit'] + greaterProfit) and CurrentStats['wtmAlgo'] != list(ProfitCoin.keys())[0]:
					logging.info("Set to RIG: %s -> Algo: %s : Wallet ID: %s : Miner: %s",  CurrentStats['rigID'], wallets[list(ProfitCoin.keys())[0]]['algo'], wallets[list(ProfitCoin.keys())[0]]['id_wal'], wallets[list(ProfitCoin.keys())[0]]['miner'])
					if wallets[list(ProfitCoin.keys())[0]]['id_wal']:
						multiRocket(CurrentStats['rigID'], wallets[list(ProfitCoin.keys())[0]]['miner'], wallets[list(ProfitCoin.keys())[0]]['id_wal'])

		except KeyboardInterrupt:
			print ("Keyboard Interrupted! bye!")
		time.sleep(30)
