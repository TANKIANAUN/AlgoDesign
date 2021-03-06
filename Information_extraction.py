# install urrllib , beautifulsoup via pip
import urllib.request
import bs4
import string
import re
import nltk
nltk.download('stopwords')

modified_punctuation=string.punctuation
modified_punctuation=modified_punctuation.replace('\'','')

links=[]
links.append("https://www.thestar.com.my/opinion/letters/2019/06/28/strengthening-the-bus-system")  #bus1
links.append("https://www.freemalaysiatoday.com/category/nation/2020/04/22/bus-companies-cry-for-help-from-putrajaya/")  #bus2
links.append("https://www.thestar.com.my/metro/metro-news/2020/03/27/bus-and-train-services-also-affected")  #bus3
links.append("https://www.bernama.com/en/general/news.php?id=1823983")  #ferry1
links.append("https://www.freemalaysiatoday.com/category/nation/2020/03/23/pangkor-island-closed-labuan-ferry-services-cut/")  #ferry2
links.append("https://www.freemalaysiatoday.com/category/leisure/2019/07/04/butterworth-to-penang-by-ferry-a-relaxing-scenic-journey/")  #ferry3
links.append("https://www.freemalaysiatoday.com/category/nation/2020/05/29/high-speed-rail-project-with-singapore-likely-to-be-extended-beyond-may-31/")  #rail1
links.append("https://www.thestar.com.my/news/nation/2020/05/01/conditional-mco-lrt-mrt-bus-services-to-resume-normal-operating-hours-from-may-4")  #rail2
links.append("https://www.thestar.com.my/news/nation/2020/03/17/movement-control-prasarana-services-to-operate-as-usual")  #rail3
links.append("https://www.freemalaysiatoday.com/category/nation/2019/12/03/lacking-freedom-ktm-piles-up-rm2-8-billion-losses-audit-shows/")  #ktm1
links.append("https://www.thestar.com.my/news/nation/2020/03/22/covid-19-ktm-reducing-frequency-of-trains-during-mco") #ktm2
links.append("https://www.malaysiakini.com/news/525254")  #ktm3
links.append("https://www.thestar.com.my/opinion/letters/2018/10/29/why-grab-leads-the-way-in-transport-service") #grab1
links.append("https://fintechnews.my/23247/various/grab-covid-19-malaysia/") #grab2
links.append("https://www.reuters.com/article/us-grab-competition-malaysia-fine/malaysia-proposes-20-million-fine-on-grab-for-abusive-practices-idUSKBN1WI06D") #grab3
links.append("https://www.thestar.com.my/lifestyle/living/2020/05/01/nobody-is-hailing-taxis-now-woes-struggling-taxi-driver-pall-singh") #taxi1
links.append("https://www.thestar.com.my/metro/metro-news/2020/04/08/taxi-e-hailing-drivers-at-a-loss") #taxi2
links.append("https://www.piston.my/2020/04/14/pickngo-taxi-drivers-also-offer-delivery-services/") #taxi3
links.append("https://www.freemalaysiatoday.com/category/nation/2020/06/11/malaysia-airports-sees-increase-in-local-flights-under-rmco/") #flight1
links.append("https://www.thestar.com.my/news/nation/2020/06/08/malaysia-airlines-lifting-travel-restrictions-and-reopening-borders-will-allow-loved-ones-to-reunite")#flight2
links.append("https://www.malaysiaairports.com.my/media-centre/news/latest-updates-new-routes") #flight3


url_links=[]
for i in range(len(links)):
    url_links.append(urllib.request.urlopen((links[i])))


html_string_links=[]
for i in range(len(links)):
    html_string_links.append(url_links[i].read())

text_links=[]
for i in range(len(links)):
    text_links.append(bs4.BeautifulSoup(html_string_links[i],'html.parser').get_text())


for i in range(len(links)):
    text_links[i]=text_links[i].encode("ascii","ignore")


for i in range(len(links)):
    text_links[i]=text_links[i].decode()



for i in range(len(links)):
    for j in modified_punctuation:
        text_links[i]=text_links[i].replace(j," ")



for i in range(len(links)):
    text_links[i] = text_links[i].split()


text_list_links=[]
#  text_list_links is nested array
for i in range(len(links)):
    text_list_links.append([])

for i in range(len(links)):
    for j in text_links[i]:
        if j not in string.punctuation:
            text_list_links[i].append(j)


#TO lowercase all letters

for i in range(len(text_list_links)):
    for j in range(len(text_list_links[i])):
        text_list_links[i][j]=text_list_links[i][j].lower()


for i in range(len(text_list_links)):
    for j in text_list_links[i]:
        temp=""
        for k in j:
            if k in string.ascii_lowercase:
                temp=temp+k
        j=temp

#TO remove stop words
#stopwords actually depend what u want, language keep changing.
#different library different stopwords
#download stopwords via nltk, go google
from nltk.corpus import stopwords
all_stopwords=stopwords.words('english')
all_stopwords.append('has')
print("Stopword:", all_stopwords)


#can actually done using shorter codes..... can actually do with python in or NLTK
# for i in all_stopwords:
#     if i in text_list:
#         text_list.remove(i)

#to complete assignment, we use string matching algorithm, in fact binary search would be much faster T(n)= logn


newtext_links=[]
for i in range (len(text_list_links)):
    newtext2=" "
    for j in text_list_links[i]:
        newtext2=newtext2+j+" "
    newtext_links.append(newtext2)


num_allchars=256
def badCharSet(stringg,size):
    badChar=[-1]*num_allchars
    for i in range(size):
        badChar[ord(stringg[i])]=i

    return badChar

def boyer_moore(txt,pat,num):
    m=len(pat)
    n=len(txt)
    txt2=txt

    badChar=badCharSet(pat,m)
    # s is shift of the pattern with respect to text
    s=0
    while(s<=n-m):
        j=m-1
        front_space = False
        back_space = False

        # front_space and back_space used to check whether its a full word
        if s+j+1<len(txt):
            if txt[s+j+1]==" ":
                back_space=True
        # comparing the last character consequently to front
        while j>=0 and pat[j]==txt[s+j]:
            j-=1

        if txt[s+j]==" ":
            front_space=True
        if j < 0 and front_space==True and back_space==True:
            txt2=re.sub(" "+pat+" "," ",txt2)
            num=num+1
            # s will shift to the next position where the pattern is matched
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            # s will shift to the next position by choosing 1 or the maximum shifting
            s += max(1, j - badChar[ord(txt[s + j])])

    return txt2,num


dictionary_list_stopwords=[]
for i in range(len(newtext_links)):
    dictionary_stopwords={}
    for j in all_stopwords:
        num=0
        newtext_links[i],num=boyer_moore(newtext_links[i],j,num)
        if num>0:
            dictionary_stopwords[j]=num
    dictionary_list_stopwords.append(dictionary_stopwords)

# print("Stopwords: ",dictionary_list_stopwords)
# print("Length: ",len(dictionary_list_stopwords))

total_stopwords=[]
for i in range(len(dictionary_list_stopwords)):
    sum=0
    for j in dictionary_list_stopwords[i]:
        sum=sum+dictionary_list_stopwords[i][j]
    total_stopwords.append(sum)
print("Sum: ",total_stopwords)


newtext_list_links=[]
for i in range(len(newtext_links)):
    newtext_list_links.append(newtext_links[i].split())


dictt_links=[]
for i in range(len(newtext_list_links)):
    dictt_links.append({})

for i in range(len(newtext_list_links)):
    for j in newtext_list_links[i]:
        if j in dictt_links[i]:
            dictt_links[i][j]=dictt_links[i][j]+1
        else:
            dictt_links[i][j]=1

for i in range(len(dictt_links)):
    print(dictt_links[i])

#index
#0,1,2 - bus
#3,4,5 - ferry
#6,7,8 - rail
#9,10,11 - flight
#12,13,14 - grab
#15,16,17 - taxi
#18,19,20 - KTM
print("\nBest Time Complexity of Boyer Moore: O(n/m)")
print("Worst Time Complexity of Boyer Moore: O(mn)")
print("Average Time Complexity of Boyer Moore: O(n)")

print(("In this case, overall time complexity would times L and S"))

#plot
import plotly.graph_objs as go
import plotly.offline as ply

x = []
y=[0]*21
y1=total_stopwords

for i in range(len(dictt_links)):  #21 article
     x.append(i+1)
     for j in dictt_links[i].keys():
         num=int(dictt_links[i][j])
         y[i]=y[i]+num

graph1 = go.Scatter(x=x,y=y,name='line for word count')
graph2 = go.Scatter(x=x,y=y,name='dot for word count',mode='markers')
graph3 = go.Scatter(x=x,y=y1,name='line for stopword')
graph4 = go.Scatter(x=x,y=y1,name='dot for stopword',mode='markers')

data = [graph1, graph2,graph3,graph4]
layout = go.Layout(title={'text': 'Graph Word Count/ stopword vs Article', 'x': 0.5},
                   xaxis=dict(title='Article'),
                   yaxis=dict(title='Word Count / Stop word'))
fig = dict(data=data, layout=layout)
ply.plot(fig, filename='Word Count.html')


