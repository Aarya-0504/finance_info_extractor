import openai
from openai_key import openai_key
openai.api_key=openai_key
import json
import pandas as pd
#calling openai's chat completion api
'''def get_response():
    prompt='Write a poem on wadapav. Only 4 lines please.'
response=openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "user", "content": "Write a poem on wadapav. Only 4 lines please."},        
    ]
)
print(response['choices'][0]['message']['content'])'''
def get_financial_data():
    return '''Please retrieve company name, revenue, net income and earnings per share (a.k.a. EPS)
    from the following news article. If you can't find the information from this article 
    then return "". Do not make things up.    
    Then retrieve a stock symbol corresponding to that company. For this you can use
    your general knowledge (it doesn't have to be from this article). Always return your
    response as a valid JSON string. The format of that string should be this, 
    {
        "Company Name": "Walmart",
        "Stock Symbol": "WMT",
        "Revenue": "12.34 million",
        "Net Income": "34.78 million",
        "EPS": "2.1 $"
    }
    News Article:
    ============'''
def extract_financial_data(text):
    question=get_financial_data()+text
    response=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": question},        
    ]
)
    result=response.choices[0]['message']['content']
    try:
        dict_data=json.loads(result)
        return pd.DataFrame(dict_data.items(),columns=["Measure","Value"])
    except(json.JSONDecodeError, IndexError):
        pass 

    #if nothing found, then returning empty dataframe using pandas
    return pd.DataFrame({
        "Measure":["company name","Stock", "Revenue","Net Income", "Eps"],
        "Value":["","","","",""]
    })
if __name__=='__main__':
    text='''Tesla's Earning news in text format: Tesla's earning this quarter blew all the estimates. They reported 4.5 billion $ profit against a revenue of 30 billion $. Their earnings per share was 2.3 $'''
    datafram=extract_financial_data(text)
    print(datafram.to_string())