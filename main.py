import os
from dotenv import load_dotenv
import pandas as pd
from twilio.rest import Client

load_dotenv()

months_list = ['january', 'february', 'march', 'april', 'may', 'june']

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
to_number = os.getenv('TWILIO_TO_NUMBER')
from_number = os.getenv('TWILIO_FROM_NUMBER')

client = Client(account_sid, auth_token)

for month in months_list:
    sells_table = pd.read_excel(f'{month}.xlsx')

    sells_table_target = sells_table['Vendas'] > 55000

    if (sells_table_target).any():

        winner_name = sells_table.loc[sells_table_target, 'Vendedor'].values[0]
        winner_amount = sells_table.loc[sells_table_target, 'Vendas'].values[0]

        print(
            f'At {month} the target has been done! Seller: {winner_name}, Sells amount: {winner_amount}')

        message = client.messages.create(
            to=to_number,
            from_=from_number,
            body=f'At {month} the target has been done! Seller: {winner_name}, Sells amount: {winner_amount}')

        print(message.sid)
