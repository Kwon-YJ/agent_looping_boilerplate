import ccxt

pb = "vuNT2At5voz7xSmGQqemDW8NdcdfipD02KGCMTGHhRDuqX2DJ4e6Yb0pIUL0eCdR"
sc = "sJrKdvG900Gyl2TFYnEDntiKuL71Bwp5t3LVg1hbeZhdLOdEPcga5aJbn4PgcfH6"


binance = ccxt.binance(
    {
        "options": {
            "defaultType": "future",
        },
        "timeout": 30000,
        "apiKey": pb,
        "secret": sc,
        "enableRateLimit": False,
    }
)

ticker = "BTC/USDT"
qty = 0.01

binance.create_order(
    ticker,
    'market',
    'sell',
    qty,
    None,
)

