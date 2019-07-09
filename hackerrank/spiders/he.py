# -*- coding: utf-8 -*-
import scrapy
import requests



class HeSpider(scrapy.Spider):
    name = 'he'
    allowed_domains = ['hackerearth.com']
       
  
    def start_requests(self):
        users=[['abdul671','it'],['bharath593','it'],['deepan71','it'],['devasena7','it'],['hari1243','it'],
               ['gokul720','it'],['mugil4','it'],['mano94','it'],['peru3','it'],['jagadesh45','it'],
               ['selinajanetrachel','it'],['rishi584','it'],['rahul1525','it'],['pradeep1400','it'],
               ['vimal270','it'],['vishali79','it'],['mhd10','it'],['sowbarnika8','it'],['sharon159','it'],
               ['sugan15','it'],['srijena1','it'],['karthikeyan376','cse'],['yeswanth50','cse'],
               ['yogesh1228','cse'],['hrithick2','cse'],['hari1247','cse'],['Deepan72','cse'],['dhinesh110','cse'],
               ['randy52','cse'],['pongokuladharshini','cse'],['pradeepa57','cse'],['sugesh2','cse'],['subha133','cse'],
               ['sangeetha.m3','cse'],['vikash765','cse'],['swathi898','cse'],['gowtham708','cse'],['barath86','cse'],
               ['bharani82','cse'],['gokul722','cse'],['ashwin679','cse'],['manikandan353','cse'],['sajeesh8','cse'],
               ['rithick.m','cse'],['rohith462','cse'],['ramprasanth','cse'],['akshayaprisha','cse'],['velmurugan33','cse'],
               ['gokul723','cse'],['nithish130','cse'],['vinod723','cse'],['jaya540','cse'],['hari1246','cse'],
               ['lakshman131','cse'],['kaviya176','cse'],['vishnu238','cse'],['sathishkumar','cse'],['kamachi2','cse'],
               ['sobhika','cse'],['sanjai32','cse'],['shesha3','cse'],['dhinesh112','cse']]
        
       
        bin=[]
        for user in users:
            url="https://www.hackerearth.com/users/pagelets/"+user[0]+"/solved-practice-problems/"
            
            yield scrapy.Request(url=url,meta={'department':user[1],'username':user[0],'bin':bin})
        url = 'https://api.jsonbin.io/b/5d2448600e09805769fd5ad9'
        headers = {'Content-Type': 'application/json'}
        req = requests.put(url, json=bin, headers=headers)
        
 

    def parse(self, response):
        
        score=response.xpath("///a[@class='link-13']/text()").extract()
        
        score={ 
                'username':response.meta['username'],
                'department':response.meta['department'],               
                'problem':score,
                'total':len(score)                           
            } 
        (response.meta['bin']).append(score)
        
        yield score
