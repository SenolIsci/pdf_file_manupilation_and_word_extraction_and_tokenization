# #on anaconda shell:
# set CONDA_FORCE_32BIT=1 # to install a 32bit interpreter
# conda create -n pdfext python=3.8.0
# conda activate pdfext
# #to run spyder with env interpreter  
# pip install spyder-kernels
# conda install -c conda-forge matplotlib
# conda install -c conda-forge pypdf2
# pip install PyMuPDF
# pip install textract
# conda install -c anaconda nltk
# #list packages
# conda list
# pip ist
# #deactivate
# conda deactivate
## select from spyders preferences interpreter file location to env interpreter address
## 'C:\\Users\\User\\Anaconda3\\envs\\pdfext\\python.exe'
##find python interpreter name and path
#import sys; sys.executable
##if necessry remove enironment and start over
#conda remove --name pdfext --all
##view list of environments
#!conda info --envs


import fitz  #pyMuPDF library
print(fitz.__doc__)

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


#Write a for-loop to open many files (leave a comment if you'd like to learn how).

file_path1 = './pdf_files/pymupdf_readthedocs_io_en_latest_faq_faq.pdf' 
file_path2= './pdf_files/pymupdf_readthedocs_io_en_latest_tutorial.pdf'
file_path3='./pdf_files/pymupdf_readthedocs_io_en_latest_tutorial_pdf_maintenance.pdf'
file_path4='./pdf_files/MERGED.pdf'
file_path5='./pdf_files/first-and-last-10.pdf'
#open allows you to read the file.

text=""

doc1 = fitz.open(file_path1) 
doc2 = fitz.open(file_path2) 
doc3 = fitz.open(file_path3) 


#Joining and Splitting PDF Documents

doc4 = fitz.open()                 # new empty PDF
# append complete doc2 to the end of doc1
doc4.insertPDF(doc1)
doc4.insertPDF(doc2)
doc4.insertPDF(doc3)
doc4.save(file_path4)


#Here is a snippet that splits doc1 and doc2. It creates a new document of its first and its last 10 pages:
doc5 = fitz.open()                 # new empty PDF
doc5.insertPDF(doc1, to_page = 9)  # first 10 pages
doc5.insertPDF(doc2, from_page = len(doc1) - 10) # last 10 pages
doc5.save(file_path5)

# close files
doc1.close()
doc2.close()
doc3.close()
doc4.close()
doc5.close()


#open pdf file
doc4 = fitz.open(file_path4)  
#metadata
metadata=doc4.metadata
#table of contents
toc = doc4.getToC()
#page counts
page_count=doc4.pageCount
for page in doc4:
    # do something with 'page'
    pcontent = page.getText('text')
    
    #create html version of the page
    phtml=page.getText('text')
    #print(pcontent)
    text=text+pcontent
    
    # get all links on a page
    links = page.getLinks()
    
    #Rendering a Page
    #This  creates a raster image of a page’s content:
    zoom_x = 2.0  # horizontal zoom
    zomm_y = 2.0  # vertical zoom
    mat = fitz.Matrix(zoom_x, zomm_y)  # zoom factor 2 in each dimension
    pix = page.getPixmap(matrix = mat)  # use 'mat' instead of the identity matrix
   
    #Saving the Page Image in a File
    #We can simply store the image in a PNG file:
    pix.writeImage("./image_folder/page-%i.png" % page.number)

doc4.close()
 
#Convert text into keywords
#The word_tokenize() function will break our text phrases into individual words.
tokens = word_tokenize(text)
#We'll create a new list that contains punctuation we wish to clean.
punctuations = ['(',')',';',':','[',']',',','!','”','“','<','>','?','’','.',"'", '-']
#We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.
stop_words = stopwords.words('english')
#We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
#print(keywords)

x=[]
y=[]
#freq of tokens and printing
freqdic=dict((x,keywords.count(x)) for x in set(keywords))
for key, value in sorted(freqdic.items(), key=lambda item: item[1], reverse=True):
    x.append(key)
    y.append(value)
    print("%s: %s" % (key, value))


plt.figure()
#freq of tokens and plotting using nltk
fd = nltk.FreqDist(keywords)
fd.plot(30,cumulative=False)



