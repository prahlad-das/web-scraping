# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 00:10:49 2021

@author: prahl
"""

# importing required libraries
import requests
from bs4 import BeautifulSoup
import time

# defining list of all the currencies 
currency = ['EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY', 'NZD', 'THB', 'HUF', 'AED', 'HKD', 'MXN', 'ZAR', 'PHP', 'SEK', 'IDR', 'SAR', 'BRL', 'TRY', 'KES', 'KRW', 'EGP', 'IQD', 'NOK', 'KWD', 'RUB', 'DKK', 'PKR', 'ILS', 'PLN', 'QAR', 'XAU', 'OMR', 'COP', 'CLP', 'TWD', 'ARS', 'CZK', 'VND', 'MAD', 'JOD', 'BHD', 'XOF', 'LKR', 'UAH', 'RON', 'BDT', 'PEN', 'GEL', 'XAF', 'FJD', 'VEF', 'VES', 'BYN', 'HRK', 'UZS', 'BGN', 'DZD', 'IRR', 'DOP', 'ISK', 'XAG', 'CRC', 'SYP', 'LYD', 'JMD', 'MUR', 'GHS', 'AOA', 'UYU', 'AFN', 'LBP', 'XPF', 'TTD', 'TZS', 'ALL', 'XCD', 'GTQ', 'NPR', 'BOB', 'ZWD', 'BBD', 'CUC', 'LAK', 'BND', 'BWP', 'HNL', 'PYG', 'ETB', 'NAD', 'PGK', 'SDG', 'MOP', 'NIO', 'BMD', 'KZT', 'PAB', 'BAM', 'GYD', 'YER', 'MGA', 'KYD', 'RSD', 'SCR', 'AMD', 'SBD', 'AZN', 'SLL', 'TOP', 'BZD', 'MWK', 'GMD', 'BIF', 'SOS', 'HTG', 'GNF', 'MVR', 'MNT', 'CDF', 'STN', 'TJS', 'KPW', 'MMK', 'LSL', 'LRD', 'KGS', 'GIP', 'XPT', 'MDL', 'CUP', 'KHR', 'MKD', 'VUV', 'MRU', 'ANG', 'SZL', 'CVE', 'SRD', 'XPD', 'SVC', 'BSD', 'XDR', 'RWF', 'AWG', 'DJF', 'BTN', 'KMF', 'WST', 'SPL', 'ERN', 'FKP', 'SHP', 'JEP', 'TMT', 'TVD', 'IMP', 'GGP', 'ZMW', 'XBT', 'FRF', 'VEB', 'ZMK', 'TRL', 'LVL', 'LTL', 'EEK', 'DEM', 'ROL', 'STD', 'TMM', 'ITL', 'ESP', 'MRO', 'BEF', 'NLG', 'IEP', 'CYP', 'SKK', 'MTL', 'GRD', 'PTE', 'ATS', 'FIM', 'SDD', 'LUF', 'SRG', 'SIT', 'GHC', 'MZM', 'MGF', 'AZM', 'VAL', 'BYR']

def currency_val():
    for i in range(len(currency)):
        st = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To='+currency[i]
        result = requests.get(st);
        
        src = result.content;
        soup = BeautifulSoup(src, 'lxml');
        search = soup.find('p', class_ = 'result__BigRate-sc-1bsijpp-1 iGrAod');
        print(search.text.strip());

    
currency_val()