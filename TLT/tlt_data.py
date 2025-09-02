import yfinance as yf

tlt = yf.Ticker("TLT")
hist = tlt.history(period="1y")  # 最近1年
print(hist[["Close"]])
