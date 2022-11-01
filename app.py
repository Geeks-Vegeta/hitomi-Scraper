from flask import Flask, render_template, url_for, send_from_directory, request, jsonify,send_file
import os
from flask import after_this_request
import requests
import random
import os
import io
import img2pdf
from bs4 import BeautifulSoup
import time
import re
from os import listdir
import shutil
from pdfrw import PdfReader, PdfWriter, PageMerge
from PyPDF2 import PdfFileReader, PdfFileWriter
import natsort


app = Flask(__name__)



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          './images/favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html", title="comixscrapper")


@app.route("/eight", methods=['GET'])
def eight():
    return render_template("eight.html", title="8muses")


@app.route("/king", methods=['GET'])
def king():
    return render_template("king.html", title="kingcomix")


@app.route("/nhentai", methods=['GET'])
def nhentai():
    return render_template("nhentai.html", title="nhentai")


@app.route("/porncomix", methods=['GET'])
def porncomix():
    return render_template("porncomix.html", title="porncomix")


@app.route("/xhamster", methods=['GET'])
def xhamster():
    return render_template("xhamster.html", title="xhamster")


# xhamster download
@app.route("/xhamster_download", methods=['POST'])
def xhamster_download():
    if request.method=="POST":

        realurl=request.form['search']
        

        rannumber=random.randint(0,11)
        directory=f"mypdf{rannumber}"
        os.mkdir(directory)
        try:
            # getting response
            response = requests.get(realurl)
            soup=BeautifulSoup(response.text,"html.parser")
            gather=soup.findAll("div" ,class_="image-thumb")
            urls=[images["data-lazy"] for images in gather]

            for i, url in enumerate(urls):
                filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
                if not filename:
                    Lab.config(text="Regex didn't match with the url: {}".format(url))
                    continue
                if i==1:
                    i="01"
                if i==2:
                    i="02"
                if i==3:
                    i="03"
                if i==4:
                    i="04"
                if i==5:
                    i="05"
                if i==6:
                    i="06"
                if i==7:
                    i="07"
                if i==8:
                    i="08"
                if i==9:
                    i="09"
                with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    
                    response = requests.get(url)
                    
                    f.write(response.content)
          
        except Exception as e:
          print(e)


        # creating pdf file
        ran_pdf=random.randint(1,11111)
        pdfname=f"comix{ran_pdf}.pdf"


        try:
            with open(pdfname,"wb") as f:
                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".png"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpeg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


        with open(pdfname,'rb') as file:
            return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory
        shutil.rmtree(directory)
        # deletring pdffile
        os.remove(pdfname)
        ran=random.randint(0,111)
        return send_file(return_data,as_attachment=True,mimetype='application/pdf',attachment_filename=f"xhmaster{ran}.pdf")



# nhentai download
@app.route("/nhentai_download", methods=['POST'])
def nhentai_download():
    if request.method=="POST":

        realurl=request.form['search']
        

        rannumber=random.randint(0,11)
        directory=f"mypdf{rannumber}"
        os.mkdir(directory)
        try:
            # getting response
            response = requests.get(realurl)
            soup=BeautifulSoup(response.text,"html.parser")
            images=soup.find_all('img')
            urls = [image['src'] for image in images]

            for i, url in enumerate(urls):
                filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
                if not filename:
                    Lab.config(text="Regex didn't match with the url: {}".format(url))
                    continue
                if i==1:
                    i="01"
                if i==2:
                    i="02"
                if i==3:
                    i="03"
                if i==4:
                    i="04"
                if i==5:
                    i="05"
                if i==6:
                    i="06"
                if i==7:
                    i="07"
                if i==8:
                    i="08"
                if i==9:
                    i="09"
                
                with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    
                    response = requests.get(url)
                    
                    f.write(response.content)
          
        except Exception as e:
          print(e)


        # it becomes difficult for pdf to add files in sequence 
        # so we came with a solution to change the name of files 
        # from 1.jpg to 01.jpg
        for file in os.listdir(directory):
            filepath = os.path.join(directory, file)



        # creating pdf file
        ran_pdf=random.randint(1,11111)
        pdfname=f"comix{ran_pdf}.pdf"


        try:
            with open(pdfname,"wb") as f:
                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".png"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpeg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

        # saving file in memonry
        with open(pdfname,'rb') as file:
            return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory
        shutil.rmtree(directory)
        # deleting pdffile
        os.remove(pdfname)
        ran=random.randint(0,111)
        return send_file(return_data,as_attachment=True,mimetype='application/pdf',attachment_filename=f"nhentaiio{ran}.pdf")




# xhamster download
@app.route("/eight_download", methods=['POST'])
def eight_download():
    if request.method=="POST":

        realurl=request.form['search']
        

        rannumber=random.randint(0,11)
        directory=f"mypdf{rannumber}"
        os.mkdir(directory)
        try:
            # getting response
            response = requests.get(realurl)
            soup=BeautifulSoup(response.text,"html.parser")
            images=soup.find_all('img')
            urls = [image['src'] for image in images]

            for i,url in enumerate(urls):
                filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$',url)
                if not filename:
                    Lab.config(text="Regex didn't match with the url: {}".format(url))
                    continue
                if i==1:
                    i="01"
                if i==2:
                    i="02"
                if i==3:
                    i="03"
                if i==4:
                    i="04"
                if i==5:
                    i="05"
                if i==6:
                    i="06"
                if i==7:
                    i="07"
                if i==8:
                    i="08"
                if i==9:
                    i="09"
                with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    
                    response = requests.get(url)
                    
                    f.write(response.content)
          
        except Exception as e:
          print(e)



        # it becomes difficult for pdf to add files in sequence 
        # so we came with a solution to change the name of files 
        # from 1.jpg to 01.jpg
        for file in os.listdir(directory):
            filepath = os.path.join(directory, file)



        # creating pdf file
        ran_pdf=random.randint(1,11111)
        pdfname=f"comix{ran_pdf}.pdf"


        try:
            with open(pdfname,"wb") as f:
                # img.convert('RGB')
                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".png"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpeg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


        with open(pdfname,'rb') as file:
            return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory
        shutil.rmtree(directory)
        # deleting pdffile
        os.remove(pdfname)
        ran=random.randint(0,111)
        return send_file(return_data,as_attachment=True,mimetype='application/pdf',attachment_filename=f"8muses{ran}.pdf")

    

# xhamster download
@app.route("/king_download", methods=['POST'])
def king_download():
    if request.method=="POST":

        realurl=request.form['search']
        

        rannumber=random.randint(0,11)
        directory=f"mypdf{rannumber}"
        os.mkdir(directory)
        try:
            # getting response
            response = requests.get(realurl)
            soup=BeautifulSoup(response.text,"html.parser")
            images = soup.find_all('figure')
            img = [image.img for image in images]
            urls = [image['data-src'] for image in img]

            for i, url in enumerate(urls):
                filename = re.search(r'([\w]-[\w*]+[.](png|jpg|gif))$',url)
                if not filename:
                    Lab.config(text="Regex didn't match with the url: {}".format(url))
                    continue
                if i==0:
                    i="00"
                if i==1:
                    i="01"
                if i==2:
                    i="02"
                if i==3:
                    i="03"
                if i==4:
                    i="04"
                if i==5:
                    i="05"
                if i==6:
                    i="06"
                if i==7:
                    i="07"
                if i==8:
                    i="08"
                if i==9:
                    i="09"
                with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    
                    response = requests.get(url)
                    
                    f.write(response.content)
          
        except Exception as e:
          print(e)


        # creating pdf file
        ran_pdf=random.randint(1,11111)
        pdfname=f"comix{ran_pdf}.pdf"

        
        # coping image to pdf
        try:
            with open(pdfname,"wb") as f:
                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".png"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpeg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)

        # saving file in memory
        with open(pdfname,'rb') as file:
            return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory 
        shutil.rmtree(directory)
        # deletring pdfile
        os.remove(pdfname)
        ran=random.randint(0,111)
        return send_file(return_data,as_attachment=True,mimetype='application/pdf',attachment_filename=f"king{ran}.pdf")




# xhamster download
@app.route("/porncomix_download", methods=['POST'])
def porncomix_download():
    if request.method=="POST":

        realurl=request.form['search']
        

        rannumber=random.randint(0,11)
        directory=f"mypdf{rannumber}"
        os.mkdir(directory)
        try:
            # getting response
            response = requests.get(realurl)
            soup=BeautifulSoup(response.text,"html.parser")
            images = soup.findAll("img")
            urls = [img['src'] for img in images]

            for i,url in enumerate(urls):
                # filename = re.search(r'([\w]-[\w*]+[.](png|jpg|gif))$',url)
                # if not filename:
                #     print("Regex didn't match with the url: {}".format(url))
                #     continue
                if i==1:
                    i="01"
                if i==2:
                    i="02"
                if i==3:
                    i="03"
                if i==4:
                    i="04"
                if i==5:
                    i="05"
                if i==6:
                    i="06"
                if i==7:
                    i="07"
                if i==8:
                    i="08"
                if i==9:
                    i="09"
                with open(directory+"/"+f"{i}.jpg", 'wb') as f:
                    if 'http' not in url:
                        # sometimes an image source can be relative 
                        # if it is provide the base url which also happens 
                        # to be the site variable atm. 
                        url = '{}{}'.format(site, url)
                    
                    response = requests.get(url)
                    
                    f.write(response.content)
          
        except Exception as e:
          print(e)




        # creating pdf file
        ran_pdf=random.randint(1,11111)
        pdfname=f"comix{ran_pdf}.pdf"


        try:
            with open(pdfname,"wb") as f:
                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".png"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)


                try:
                    imgs = []
                    for fname in os.listdir(directory):
                        if not fname.endswith(".jpeg"):
                            continue
                        path = os.path.join(directory, fname)
                        if os.path.isdir(path):
                            continue
                        imgs.append(path)
                    f.write(img2pdf.convert(natsort.natsorted(imgs)))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)


        with open(pdfname,'rb') as file:
            return_data = io.BytesIO(file.read())
        return_data.seek(0)
        # deleting directory
        shutil.rmtree(directory)
        # deletring pdf file
        os.remove(pdfname)
        ran=random.randint(0,111)
        return send_file(return_data,as_attachment=True,mimetype='application/pdf',attachment_filename=f"porncomix{ran}.pdf")





if __name__ == "__main__":
    app.run(debug=True)