from lxml import html
import requests
import os
import urllib2
import subprocess
#def main():
 #   download_file("http://mensenhandel.nl/files/pdftest2.pdf")

def download_file(pdf_save_path, download_url):
    cmd='wget -O %s %s'%(pdf_save_path,download_url)
    #print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
    #print cmd
    if subprocess.call(cmd)!=0:
        print 'Failed'
    else:
        print 'Succeed'

    

def getPdf(pdf_save_root, pdf_name, url):

    # creat directoriey if is is not exist
    if not os.path.exists(pdf_save_root):
        os.makedirs(pdf_save_root)


    pdf_name=pdf_name.replace(' ','_')
    pdf_name=pdf_name.replace(':','_')
    pdf_name=pdf_name.replace('?','_')


    pdf_save_path = pdf_save_root+'\\'+pdf_name
    download_file(pdf_save_path, url)

    
def getPdfName(issue_val,issue_num, url, url_path, cite_path):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    url_list  = tree.xpath(url_path)
    cite_list = tree.xpath(cite_path)
    cite_dir = {}

    

    for item in cite_list:
        dict_key  = item.values()[0][10:17]
        split_str = item.text_content().split('(')
        dict_val  = split_str[1][0]
        cite_dir.setdefault(dict_key, dict_val)

    for item in url_list:
        left_ = item.values()[0]
        print '======================================================'
        print 'paperName:'+left_[27:]
        pdf_name=left_[27:]+'.pdf'
        #print 'pdfUrl:'+'http://ieeexplore.ieee.org'+item.values()[1]
        pdfUrl='http://ieeexplore.ieee.org/ielx7/6245522/%s/0%s.pdf'%(issue_num,item.values()[1][30:])
        #print pdfUrl

        pdf_save_root = 'M:\\download\\changshuo\\'+issue_val

        getPdf(pdf_save_root, pdf_name, pdfUrl)

        citation_file=pdf_save_root+'\\citation.txt'
        f=open(citation_file,'a')
        query_key = item.values()[1][30:]
        if cite_dir.has_key(query_key):
            cite_num = cite_dir[query_key]
        else:
            cite_num = '0'
        print 'cite_num:'+cite_num
        sss='cite num: '+cite_num+'  ==  '+pdf_name
        f.write(sss)
        f.write('\n')
        f.write('\n')
        f.close()
        print '======================================================'


if __name__ == "__main__":
    url = 'http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=6969784&punumber=6245522'
    url_path = '//div[1]/div[2]/a[3]'
    cite_path = '//ul/li[*]/div[1]/a'

    #issue_list    = ['Issue4', 'Issue5', 'Issue6']
    #issue_number  = ['7464113', '7489963', '7513193']

    #issue_list    = ['Issue7', 'Issue8', 'Issue9']
    #issue_number  = ['6895376', '6911078', '6969702']

    issue_list    = ['Issue10', 'Issue11', 'Issue12', 'Issue13', 'Issue14']
    issue_number  = ['6969784', '7004513', '7019830', '7022516', '7085375']

    url_left  = 'http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber='
    url_right = '&punumber=6245522'
    url_pdf   = 'http://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber='

    for i, issue_val in enumerate(issue_list):        
        url = url_left+issue_number[i]+url_right
        print 'downloading',issue_val
        #getPdfName(issue_val,issue_number[i], url, url_path, cite_path)
        if issue_val == 'Issue13':
            getPdfName(issue_val,issue_number[i], url, url_path, cite_path)
            url = 'http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=7022516&filter%3DAND%28p_IS_Number%3A7022516%29&pageNumber=2'
            getPdfName(issue_val,issue_number[i], url, url_path, cite_path)
        else:
            getPdfName(issue_val,issue_number[i], url, url_path, cite_path)

    print 'you have downloaded all the needed papers'


'''    issue_val='Issue10'
    issue_number0='6969784'
    url ='http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=6969784&punumber=6245522'
    

    getPdfName(issue_val,issue_number0, url, url_path, cite_path)
    print 'done'

 
    for i, issue_val in enumerate(issue_list):
        print 'downloading',issue_val
        url = url_left+issue_number[i]+url_right
        if issue_val == 'Issue13':
            getPdfName(issue_val, url, url_path, cite_path)
            url = 'http://ieeexplore.ieee.org/xpl/tocresult.jsp?isnumber=7022516&filter%3DAND%28p_IS_Number%3A7022516%29&pageNumber=2'
            getPdfName(issue_val, url, url_path, cite_path)
        else:
            getPdfName(issue_val, url, url_path, cite_path)
'''