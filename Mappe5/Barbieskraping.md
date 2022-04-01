Oppgaven her er å lage en tabell og lage en regresjonslinje av den tabellen

Nedenfor er det blitt brukt statestikk over barbie brutto salg over år


```python
from bs4 import BeautifulSoup
import requests

def fetch_html_tables(url):
    "Returns a list of tables in the html of url"
    page = requests.get(url)
    bs=BeautifulSoup(page.content)
    tables=bs.find_all('table')
    return tables

tables=fetch_html_tables('https://www.statista.com/statistics/370361/gross-sales-of-mattel-s-barbie-brand/')
table_html=tables[0]

#printing top
print(str(table_html)[:1000])
```

    <table class="table hidden" id="statTableHTML"><thead><tr><th>Characteristic</th><th>Gross sales in million U.S. dollars</th></tr></thead><tbody><tr><td>2020</td><td>1,350.1</td></tr><tr><td>2019</td><td>1,159.77</td></tr><tr><td>2018</td><td>1,088.95</td></tr><tr><td>2017</td><td>954.89</td></tr><tr><td>2016</td><td>971.8</td></tr><tr><td>2015</td><td>905.9</td></tr><tr><td>2014</td><td>1,009.5</td></tr><tr><td>2013</td><td>1,202.8</td></tr><tr><td>2012</td><td>1,275.3</td></tr></tbody></table>



```python
def html_to_table(html):
    "Returns the table defined in html as a list"
    #defining the table:
    table=[]
    #iterating over all rows
    for row in html.find_all('tr'):
        r=[]
        #finding all cells in each row:
        cells=row.find_all('td')
        
        #if no cells are found, look for headings
        if len(cells)==0:
            cells=row.find_all('th')
            
        #iterate over cells:
        for cell in cells:
            cell=format(cell)
            r.append(cell)
        
        #append the row to t:
        table.append(r)
    return table

def format(cell):
    "Returns a string after converting bs4 object cell to clean text"
    if cell.content is None:
        s=cell.text
    elif len(cell.content)==0:
        return ''
    else:
        s=' '.join([str(c) for c in cell.content])
        
    #here you can add additional characters/strings you want to 
    #remove, change punctuations or format the string in other
    #ways:
    s=s.replace('\xa0','')
    s=s.replace('\n','')
    return s

table=html_to_table(table_html)

#printing top
print(str(table)[:1000])
```

    [['Characteristic', 'Gross sales in million U.S. dollars'], ['2020', '1,350.1'], ['2019', '1,159.77'], ['2018', '1,088.95'], ['2017', '954.89'], ['2016', '971.8'], ['2015', '905.9'], ['2014', '1,009.5'], ['2013', '1,202.8'], ['2012', '1,275.3']]



```python
';'.join(table[0])
```




    'Characteristic;Gross sales in million U.S. dollars'




```python
def save_data(file_name,table):
    "Saves table to file_name"
    f=open(file_name,'w')
    for row in table:
        f.write(';'.join(row)+'\n')
    f.close()
    
save_data('barbiesalg.csv',table)
```


```python
import pandas as pd
pd.read_csv('barbiesalg.csv', delimiter=';', encoding='latin1')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Characteristic</th>
      <th>Gross sales in million U.S. dollars</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2020</td>
      <td>1,350.1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019</td>
      <td>1,159.77</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2018</td>
      <td>1,088.95</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2017</td>
      <td>954.89</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2016</td>
      <td>971.8</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2015</td>
      <td>905.9</td>
    </tr>
    <tr>
      <th>6</th>
      <td>2014</td>
      <td>1,009.5</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2013</td>
      <td>1,202.8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2012</td>
      <td>1,275.3</td>
    </tr>
  </tbody>
</table>
</div>




```python
from bs4 import BeautifulSoup
import requests

def scrape(url, file_name):
    table=[]
    tables=fetch_html_tables(url)
    #iterate over all tables, if there are more than one:
    for tbl in tables:
        #exends table so that table is a list containing elements 
        #from all tables:
        table.extend(html_to_table(tbl))
    #saving it:
    save_data(file_name,table)
    return table
```


```python
url='https://www.statista.com/statistics/370361/gross-sales-of-mattel-s-barbie-brand/'
file_name='barbiesalg.csv'

table=scrape(url,file_name)

s='\n'.join(['\t'.join(row) for row in table])


#printing top'
print(str(s)[:1000])
```

    Characteristic	Gross sales in million U.S. dollars
    2020	1,350.1
    2019	1,159.77
    2018	1,088.95
    2017	954.89
    2016	971.8
    2015	905.9
    2014	1,009.5
    2013	1,202.8
    2012	1,275.3
    
                            Free                    	                                                        $39 per month*                                                        (billed annually)                            
    	
    	
    
    	
    	
    	
    	                            Register                        	                            Purchase now                        

```python
import pandas as pd
g = pd.read_csv("barbiesalg.csv")#reading data
g


```python
import numpy as np
import matplotlib as mtp
import seaborn as sns

#legge til vekter

X= 'Characteristic'
Y= 'Gross sales in million U.S. dollars'
```


```python
from matplotlib import pyplot as plt

fig,ax=plt.subplots()
plt.plot(log(X, Y, 'o'))
```




    [<matplotlib.lines.Line2D at 0x7fae55592d00>]




    
![png](output_9_1.png)
    



```python
plt.plot(x, m*x+b)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Input In [359], in <module>
    ----> 1 plt.plot(x, m*x+b)


    NameError: name 'm' is not defined


Barbie ble solgt mest i 2012 og 2020 
Den med minst brutto salg ila året 2015 det kan eg se på regresjons linjen.

Det var stor popularitet ca 2010 også ble det mindre i en del år men så økte det ila covid åra. 


```python

```
