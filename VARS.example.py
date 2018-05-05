SECRET_KEY = 'your_secret_key'
PUBLIC_KEY = 'your_public_key'
RIG_ID = 'YOUR_RIG_ID'
# Check your best server
URL = "https://paris.hiveos.farm/worker/eypiay.php"

"""
You need to pass it some parameters about your setup, and then parse it according to what you're looking for..
Select your cards and input power cost, click calculate, then copy the link and add ".json" after "coins" and you will get output based on what you fed into it.
https://www.reddit.com/r/gpumining/comments/7wwveu/how_to_read_whattomine_json/?st=jgt4s3wm&sh=7285ed6b
https://whattomine.com/
"""
SRC = {
    'whattomine': {
                'url': "https://whattomine.com/coins.json?utf8=%E2%9C%93&adapt_q_280x=0&adapt_q_380=0&adapt_q_fury=0&adapt_q_470=0&adapt_q_480=0&adapt_q_570=0&adapt_q_580=0&adapt_q_vega56=0&adapt_q_vega64=0&adapt_q_750Ti=0&adapt_q_1050Ti=0&adapt_q_10606=0&adapt_q_1070=0&adapt_q_1070Ti=0&adapt_q_1080=0&adapt_q_1080Ti=5&adapt_1080Ti=true&eth=true&factor%5Beth_hr%5D=175.0&factor%5Beth_p%5D=700.0&grof=true&factor%5Bgro_hr%5D=290.0&factor%5Bgro_p%5D=1050.0&x11gf=true&factor%5Bx11g_hr%5D=97.5&factor%5Bx11g_p%5D=850.0&cn=true&factor%5Bcn_hr%5D=4150.0&factor%5Bcn_p%5D=700.0&factor%5Bcn7_hr%5D=4150.0&factor%5Bcn7_p%5D=700.0&eq=true&factor%5Beq_hr%5D=3425.0&factor%5Beq_p%5D=950.0&lre=true&factor%5Blrev2_hr%5D=320000.0&factor%5Blrev2_p%5D=950.0&ns=true&factor%5Bns_hr%5D=7000.0&factor%5Bns_p%5D=950.0&factor%5Btt10_hr%5D=150.0&factor%5Btt10_p%5D=1000.0&factor%5Bx16r_hr%5D=75.0&factor%5Bx16r_p%5D=950.0&skh=true&factor%5Bskh_hr%5D=237.5&factor%5Bskh_p%5D=950.0&n5=true&factor%5Bn5_hr%5D=375.0&factor%5Bn5_p%5D=950.0&xn=true&factor%5Bxn_hr%5D=26.5&factor%5Bxn_p%5D=950.0&factor%5Bcost%5D=0.1&sort=Profit&volume=0&revenue=current&factor%5Bexchanges%5D%5B%5D=&factor%5Bexchanges%5D%5B%5D=binance&factor%5Bexchanges%5D%5B%5D=bitfinex&factor%5Bexchanges%5D%5B%5D=bittrex&factor%5Bexchanges%5D%5B%5D=cryptopia&factor%5Bexchanges%5D%5B%5D=hitbtc&factor%5Bexchanges%5D%5B%5D=poloniex&factor%5Bexchanges%5D%5B%5D=yobit&dataset=Main&commit=Calculate",
                        'sort_key': "profitability"
                            }
        }

#id_walet -> start script with the one which yout want and see the logs of this script
wallets = {
	'NeoScrypt': {
			'hive_name': 'neoscrypt',
			'algo': '',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'NeoScrypt - Nicehash'
			},
	'Equihash': {
			'hive_name': 'equihash',
			'algo': 'equihash',
			'miner': 'dstm',
			'id_wal': YOUR_ID,
			'wallet_name': 'Equihash - Nicehash'
			},
	'Lyra2REv2': {
			'hive_name': 'Lyra2REv2',
			'algo': 'lyra2rev2',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'Lyra2REv2 - Nicehash'
			},

	'NIST5': {
			'hive_name': 'NIST5',
			'algo': 'nist5',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'NIST5 - NiceHash'
			},
	'X11Gost': {
			'hive_name': 'X11Gost',
			'algo': '',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'X11Ghost - NiceHash'
			},
	'CryptoNight': {
			'hive_name': 'X11Gost',
			'algo': '',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'CryptoNight - NiceHash'
			},
	'Xevan': {
			'hive_name': 'Xevan',
			'algo': '',
			'miner': 'ccminer',
			'id_wal': YOUR_ID,
			'wallet_name': 'Xevan - Supernova'
			}
	}

