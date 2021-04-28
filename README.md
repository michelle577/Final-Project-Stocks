# Final-Project-Stocks

Problem description: The objective of this project is to find some stocks that are worth buying. We are going to sneak a peak into what large institutional managers are doing by web scraping 13-F filings. In this case, we will scrape Berkshire Hathaway, the firm of Warren Buffett. Institutional managers have better insights than the ordinary lay person, so it is worth seeing what they are buying. 

Related work: This project is related to visualization and web scraping. I enjoyed learning about matplotlib and ggplot in module #10. So, I will be using a similar library called Plotly Esxpress, which has extremely similar methods for visualization.

Solution: I am using a time series approach combined with visualization to spot notable stocks within the dataset. Large stock holdings and recent buying trends may provide valuable indicators in which stocks to buy. I solved the problem by first scraping 13-F filings from SEC.gov with 13f_download.py. This creates a folder called 13f with all of the filings. Then I merged all of the 13-F data into one dataframe using merger.py, which creates a file called Berkshire 13-f.csv. Then I used analysis.py to pass the dataframe into plotly functions to creatse visualizations. Finally, I viewed the visualizations to see which stocks seem promising. 

Please see attached documents to see codes
