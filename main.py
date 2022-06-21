import pandas as pd

months_list = ['january', 'february', 'march', 'april', 'may', 'june']


for month in months_list:
    sells_table = pd.read_excel(f'{month}.xlsx')

    if (sells_table['Vendas'] > 55000).any():

        winner_name = sells_table.loc[sells_table['Vendas']
                                      > 55000, 'Vendedor'].values[0]
        winner_sells_amount = sells_table.loc[sells_table['Vendas']
                                              > 55000, 'Vendas'].values[0]

        print(
            f'At {month} the target has been done! Seller: {winner_name}, Sells amount: {winner_sells_amount}')
