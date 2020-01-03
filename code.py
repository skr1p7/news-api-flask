from flask import Flask, render_template, request, redirect, url_for
from newsapi import NewsApiClient

app = Flask(__name__)

newsapi = NewsApiClient(api_key='')
#results = newsapi.get_everything(q="huawei", page_size=10)

@app.route('/', methods=['GET','POST'])
def my_form_post():
    if request.method == "POST":
        text = request.form['text']
        results = newsapi.get_everything(q=str(text), page_size=10)
        a = results['articles'][0]['title']
        ima = results['articles'][0]['urlToImage']
        urla = results['articles'][0]['url']
        b = results['articles'][1]['title']
        imb = results['articles'][1]['urlToImage']
        urlb = results['articles'][1]['url']
        c = results['articles'][2]['title']
        imc = results['articles'][2]['urlToImage']
        urlc = results['articles'][2]['url']
        d = results['articles'][3]['title']
        imd = results['articles'][3]['urlToImage']
        urld = results['articles'][3]['url']
        e = results['articles'][4]['title']
        ime = results['articles'][4]['urlToImage']
        urle = results['articles'][4]['url']
        f = results['articles'][5]['title']
        imf = results['articles'][5]['urlToImage']
        urlf = results['articles'][5]['url']
        g = results['articles'][6]['title']
        img = results['articles'][6]['urlToImage']
        urlg = results['articles'][6]['url']
        h = results['articles'][7]['title']
        imh = results['articles'][7]['urlToImage']
        urlh = results['articles'][7]['url']
        i = results['articles'][8]['title']
        imi = results['articles'][8]['urlToImage']
        urli = results['articles'][8]['url']
        j = results['articles'][9]['title']
        imj = results['articles'][9]['urlToImage']
        urlj = results['articles'][9]['url']
        return render_template('base.html', a=a, b=b, c=c, d=d, e=e, f=f, g=g, h=h, i=i, j=j,ima=ima,imb=imb,imc=imc,imd=imd,ime=ime,imf=imf,img=img,imh=imh,imi=imi,imj=imj,urla=urla,urlb=urlb,urlc=urlc,urld=urld,urle=urle,urlf=urlf,urlg=urlg,urlh=urlh,urli=urli,urlj=urlj)

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run()