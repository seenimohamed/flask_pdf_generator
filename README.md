# PDF Generator using pdfkit via flask in python

## Steps to follow 

1. Clone the repo
2. Install the required packages. (P.S : If anything goes wrong, follow the installation step)
```
pip install -r requirements
```


3. Run the app
```python pdf.py```
4. Hit https://localhost:5000 - to check whats in pdf template

5. Hit https://locahost:5000/<any name> - to generate a pdf
  ```
  Eg : https://localhost:5000/Seeni 
  ``` 

Installation 
------------

1. Install python-pdfkit:
```
pip install pdfkit
```

2. Install wkhtmltopdf:
```
brew install Caskroom/cask/wkhtmltopdf
```
[link for further reference to download wkhtmltopdf](https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf)
