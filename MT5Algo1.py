import MetaTrader5 as mt
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import MetaTrader5 as mt5

from streamlit_option_menu import option_menu

menu = option_menu('Menu',options=['Login','Trade','Analytics'])

if menu=='Login':
    with st.form('Login',clear_on_submit=True):
        login = st.text_input('Login')
        password= st.text_input('Password')

        submit = st.form_submit_button('Submit')
        if submit:
            mt.initialize()
            login=25063331
            password= "btiwLDUQ~.39"
            server="FivePercentOnline-Real"
            mt.login(login,password,server)

if menu=='Trade':
    with st.form('Trade Order',clear_on_submit=True):

        symbol = st.text_input('Symbol')
        volume= st.number_input('Lots')
        sl = st.number_input('Stop Loss')
        tp = st.number_input('Target Profit')

        BUY = st.form_submit_button('BUY')
        SELL =st.form_submit_button('SELL')

        if BUY:

            request = {
                "action": mt5.TRADE_ACTION_DEAL,  # Market order
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_BUY,  # Sell order
                "sl": sl,
                "tp": tp,
                "type_time": mt5.ORDER_TIME_GTC,  # Good till cancelled
                "type_filling": mt5.ORDER_FILLING_IOC,  # or mt5.ORDER_FILLING_FOK for Fill or Kill
    }
            
            result = mt5.order_send(request)
            st.write(result)

        if SELL:

            request = {
                "action": mt5.TRADE_ACTION_DEAL,  # Market order
                "symbol": symbol,
                "volume": volume,
                "type": mt5.ORDER_TYPE_SELL,  # Sell order
                "sl": sl,
                "tp": tp,
                "type_time": mt5.ORDER_TIME_GTC,  # Good till cancelled
                "type_filling": mt5.ORDER_FILLING_IOC,  # or mt5.ORDER_FILLING_FOK for Fill or Kill
    }
            
            result = mt5.order_send(request)
            st.write(result)

# if menu == 'Analytics':




        
        



    





# Initialize MetaTrader5
if not mt5.initialize():
    print("initialize() failed")
    mt5.shutdown()

def get_all_positions():
    """Closes all open positions, regardless of symbol."""
    positions = mt5.positions_get() 
    return positions # Get all open positions

    


print (result)

    #         if result.retcode != mt5.TRADE_RETCODE_DONE:
    #             print(f"Error closing position {position_id} ({symbol}): {result.comment}")
    #         else:
    #             print(f"Position {position_id} ({symbol}) closed successfully: {result}")
    # else:
    #     print("No open positions found.")



