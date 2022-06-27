from xml.dom.minidom import Document
from documentary_private import Documentary

m = Documentary('Mulan',2020,'action')
m.print_detail()
print(f'year : {m._Movie_year}')