import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

print (df.head())

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume', ]]

print (df.head())
df['HL_PCT'] = df['Adj. High'] - df['Adj. Close'] / df['Adj. Close'] * 100.
#
df['PCT_CHNG'] = df['Adj. Close'] - df['Adj. Open'] / df['Adj. Open'] * 100.0
#
df = df[['Adj. Close', 'HL_PCT', 'PCT_CHNG', 'Adj. Volume']]


print (df.head())

