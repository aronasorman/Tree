from django.http import HttpResponse

from django.shortcuts import render_to_response

from django.template import RequestContext

import json

from collections import Counter

from random import randrange


def clean_node(node,addr,html):

	title= node['title']
	colors= ['#FA8072','#ADFF2F','pink','#87CEEB','#D2B48C','#00FF7F','#F4A460','#FFDAB9','#FFDEAD','#00FF00']  # set of colours for display
        rand_no= randrange(5)  # variable for generation of random colours
	if node['slug']==addr:
		if node['kind'] == 'Topic':
			
			k= len(node['children'])
			
			html += "<html> <title> %s </title> " %title + "<body bgcolor=%s>" %colors[rand_no] + "<h3 style='font-size:20px' > <nav ><pre>"   # use of <nav> & <pre> to set links in horizontal line viz. inline
			#html +="li{display:inline;}"

			for i in range(0,k):	                                                                           
	   			d = new_node(node['children'][i])  # return title of children
	   			e = next_node(node['children'][i]) # return slug of children
				
				html += " <a href=\"%s\" style=\"text-decoration:none;\">" %e  
				html +=" &nbsp; &nbsp; &nbsp; &nbsp; %s </b> </a> " %d   #use of backslash for separation

			html += "</pre></nav></body></html>"
			return html	
			
		else:
			rand_no= randrange(10)
			d = node['content']
			e = node['slug'] + '.jpg'
			e = '../../../../../../media/' + e   # defining path for extraction of image
	   		html ="<html> <title> %s </title>" %title +"<body bgcolor=%s>"  %colors[rand_no] + "<h1 style='font-size:50px'> <center>%s</center> </h1>"%title+ "<center>"+ " <img src=%s>" %e + "<br><br> <textarea wrap='hard' rows=\'5\' cols=\'100\'> %s </textarea></center>" %d +  "</body></html>"  # display of image & content in textarea using hard wrap
			h=html
	else:   
	        
		if node['kind'] == 'Topic':		
			for child in node['children']:
				html=clean_node(child,addr,html)	     
		


	                                                                          
	return html
	




def new_node(node):
	b= node['title']
	return b

def next_node(node):
	e= node['slug']
	return e

def dynamic(node,a):


	
	c= "'}  ),"
	d= "/$', load ,{'addr' : '"

	if node['kind'] == 'Topic':	
		a += node['slug']
		prev=a
		a +=d
		a += node['slug']
		a +=c
		print a		
		for i in node['children'] :                                                                     
			dynamic(i,prev+"/") 
	else:
		a += node['slug']
		a +=d
		a += node['slug']
		a +=c
		print a		
			

	with open("../tree/tree/urls.py", "a+") as myfile:
    		myfile.write(a+"\n")	
		myfile.close()

	
	 #url(r'^stories-and-literature/$', load ,{'addr' : 'stories-and-literature'}  ),
					
			#k= len(node['children']) # returns number of children
			
def gen_url(request):
	json1_file = open('json1.json')    
     	json1_str = json1_file.read()
     	json1_data = json.loads(json1_str) #returns json data into python dict type
	
	fo = open("../tree/tree/urls.py", "r")
	fo.seek(-5,2)
	if fo.read(5)=="#Done":
		fo.close()
		return HttpResponse("URL Already Generated")
	
	with open("../tree/tree/urls.py", "a+") as myfile:
   		myfile.write("urlpatterns += patterns('',\n")
		myfile.close()

	dynamic(json1_data,"\turl(r'^")	

	with open("../tree/tree/urls.py", "a+") as myfile:
   		myfile.write(")\n#Done")	
		myfile.close()
	
	return HttpResponse("URL Generated")



def load(request,addr):
	html=""
	json1_file = open('json1.json')    
     	json1_str = json1_file.read()
     	json1_data = json.loads(json1_str)                                              
	html= clean_node(json1_data,addr,html)
	return HttpResponse(html)
