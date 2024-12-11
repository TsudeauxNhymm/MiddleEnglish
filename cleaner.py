from glob import iglob
from tqdm import tqdm
from bs4 import BeautifulSoup as b
#the files were initially stored as html files, despite the extension.
for ii in tqdm(iglob("*/*.txt")):
    with open(ii) as fb:
        soup = b(fb,"html.parser")
    lines = [ii.text for ii in soup.find_all("p")[:-1]]
    for jj in range(len(lines)):
        lines[jj] = lines[jj].lower()
        #These sometimes showed up as a way to denote page breaks or when an image appeared in the original book.
        for kk in ["[page]","[illustration]","/","|"]:
            lines[jj] = lines[jj].replace(kk,'')
    with open(ii,'w') as outfile:
        outfile.writelines([jj+"\n" for jj in lines])
    
