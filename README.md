# IFTTT webhooks notifications

## Bitcoin notification price

```python
python bitcoin_ifttt_notification.py <ifttt_webhook_key>
```

- I find my key here: `https://ifttt.com/services/maker_webhooks/settings`

- Each execution check if there are some recently price on DB, if not check it in coinmarketcap api and save it on DB. If the price reach the limit configured use another ifttt webhook. 

Based on https://realpython.com/python-bitcoin-ifttt/#sending-a-test-ifttt-notification 
