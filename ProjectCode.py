
# coding: utf-8

# In[ ]:




# In[61]:


import re, urllib2,os,sys,time
from bs4 import BeautifulSoup


# coding: utf-8

import urllib2,os,sys,time
browser=urllib2.build_opener()
urllib2.install_opener(browser)
browser.addheaders=[('User-agent', 'Mozilla/5.0')]
fwriter=open('moviedata.csv','w')
Headerstring='Title,Rating,Year,Duration,Mrating,Gener1,Gener2,Gener3,Gener4,Gener5,Gener6,Gener7,Gener8,Gener9,Gener10,Gener11,Gener12,Gener13,Gener14,Director,Actor1,Actor2,Actor3,Budget,Revenue,Profit\n'
fwriter.write(Headerstring)    
pagesToGet=100
page=1
for r in range(1,pagesToGet+1):
    url='http://www.imdb.com/search/title?countries=us&has=business-info&languages=en&production_status=released&release_date=2005,2015&start='+str(page)+'&title_type=feature&user_rating=1.0,10'
    
    try:
        response=browser.open(url)
    except Exception as e:
        error_type, error_obj, error_info = sys.exc_info()
        print 'ERROR FOR LINK:',url
        print error_type, 'Line:', error_info.tb_lineno
        continue
    html=response.read()
    html= re.sub('[\s+]', '', html)
    matches=re.finditer('(?:<trclass="evendetailed">.*?<tdclass="title">.*?<ahref="(.*?)">.*?</tr>)|(?:<trclass="odddetailed">.*?<tdclass="title">.*?<ahref="(.*?)">.*?</tr>)',html)
    for M in matches:
        if M.group(1):
            movieURL=M.group(1)
        else: 
            movieURL=M.group(2)
         
        MoviepageURL=' http://www.imdb.com'+str(movieURL)
        try:
            response=browser.open(MoviepageURL)
       
    #interests=re.finditer('<a class="gsc_co_int" .*?>(.*?)</a>',InterestString)
        except Exception as e:
            error_type, error_obj, error_info = sys.exc_info()
            print 'ERROR FOR LINK:',url
            print error_type, 'Line:', error_info.tb_lineno
            continue
        html_movie=response.read()
        #print 'processing' 
        #m1=re.search('<div class="title_bar_wrapper">(?:\s+|\S)*?<span itemprop="ratingValue">(.*)</span></strong>(?:\s+|\S)*?<div class="titleBar">(?:\s+|\S)*?<h1 itemprop="name" class="">(.*)<span id="titleYear">.<a href=".*">(.*)</a>.(?:\s+|\S)*?<time itemprop="duration" datetime="PT96M">\s+(.*)\s+</time>',html_movie)
                     #<div class="title_bar_wrapper">\s+<div class="ratings_wrapper">\s+.*\s+<div class="ratingValue">\s+.*span itemprop="ratingValue">(.*?)</span>',html_movie)
        #print 'processing' 
        #print 'Ratings:'+m1.group(1)
        #print 'Name:'+m1.group(2)
        #print 'Year Release:'+m1.group(3)
        tree=BeautifulSoup(html_movie)#prepare the tree

        ratingChunk = tree.find('span', {'itemprop':'ratingValue'}) # find all review Chunks
        rating=ratingChunk.text
        
        titleChunk=tree.find('h1', {'itemprop':'name'})#<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/customer-reviews/RTCU9IHUSOC3K/ref=cm_cr_pr_rvw_ttl?ie=UTF8&amp;ASIN=B00XKRWTUE">Very Good</a>
        t=re.search('(.*?)\((.*?)\)',titleChunk.text)
        title=t.group(1)
        Year=t.group(2)
        
        
        MRatingChunk=tree.find('div', {'class':'subtext'})#<a class="a-size-base a-link-normal review-title a-color-base a-text-bold" href="/gp/customer-reviews/RTCU9IHUSOC3K/ref=cm_cr_pr_rvw_ttl?ie=UTF8&amp;ASIN=B00XKRWTUE">Very Good</a>
        MRating=re.search('(.*?)\s\|',MRatingChunk.text)
        
        
        
        durationChunk=tree.find('time',{'itemprop':'duration'})#<a class="a-size-base a-link-normal author" href="/gp/pdp/profile/AZ0OW7VY5G26T/ref=cm_cr_pr_pdp?ie=UTF8">John McCarthy</a>
        duration=durationChunk.text
        
        generText=''
        genreChunk=tree.findAll('span',{'itemprop':'genre'})
        for RC in genreChunk:
            geneText=RC.text.strip()
            generText=generText+geneText+','
        
        Generstring=''
        M= re.search('Action',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Adventure',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Sci-Fi',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Fantacy',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Family',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Drama',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Comedy',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Thriller',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Horror',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Mistery',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Romance',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Biography',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Crime',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        M= re.search('Sport',generText)
        if M:
             Generstring=Generstring+M.group(0)+','
        else: 
             Generstring=Generstring+''+','
        

        
       
            
           
            
        profitChunk=tree.findAll('div',{'class':'txt-block'})
        budget=0
        for RC in profitChunk:
            txtC=RC.find('h4',{'class':'inline'})
            if txtC:
                if txtC.text=='Budget:':
                    Budget=re.search('(\$.*)',RC.text)
                    budg=Budget.group(1)
                    budg=re.sub(',', '', budg)
                    budget=1
                if txtC.text=='Gross:':
                    GrossRev=re.search('(\$.*)',RC.text)
                    Gross=GrossRev.group(1)
                    Gross=re.sub(',', '', Gross)
             
        
        directorChunk=tree.find('span',{'itemprop':'director'})#<a class="a-size-base a-link-normal author" href="/gp/pdp/profile/AZ0OW7VY5G26T/ref=cm_cr_pr_pdp?ie=UTF8">John McCarthy</a>
        director=re.sub(',', '',directorChunk.text.strip())
        
        
        actor=''
        AChunk=tree.findAll('span',{'itemprop':'actors'})
        for RC in AChunk:
            actorchunk=RC.find('span',{'itemprop':'name'})
            actor=actor+actorchunk.text+','
        
        profit=0
        if budget==1:
            budgInt=re.sub('$', '', budg.strip())
            GrossInt=re.sub('$', '', Gross.strip())
            if budgInt<GrossInt:
                profit=1
            
            CSVString=title+','+rating+','+Year+','+duration.strip()+','+MRating.group(1)+','+Generstring+director+','+actor+budg.strip()+','+Gross.strip()+','+str(profit)+'\n'
            CSVString = CSVString.encode('ascii', 'ignore').decode('ascii')
            fwriter.write(CSVString)
    
        time.sleep(3)
    
    time.sleep(3)
    page=page+50
        
fwriter.close()

  


# In[ ]:




# In[ ]:




# In[ ]:



