from html.parser import HTMLParser
class MyParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = 0
        self.label = 0
        self.response = []
    def handle_starttag(self, tag, attrs):
        if tag =='a标签': #
            self.flag =1
        if tag =='b标签':
            self.label = 'b'
        if tag == 'c标签':
            self.label = 'c'
        if tag == 'd标签':
            self.label = 'd'

    def handle_endtag(self, tag):
        if self.flag == 1 and tag == 'a标签':
            self.flag = 0  # a标签开头到第一个c标签结尾之间元素self.flag值都为1

    def handle_data(self, data):
        data = data.strip()
        if self.label and self.flag and data:
            if self.label == 'b':
                self.response.append({self.label:data})
            else:
                self.response[-1][self.label]=data
            self.label = 0
parser = MyParser()

parser.feed('''<a标签> text11
<b标签> text12<c标签>text13<d标签>text14</d标签></c标签></b标签>
</a标签>text15<a标签> text21
<b标签> text22<c标签>text23<d标签>text24</d标签></c标签></b标签>
</a标签>text25<a标签> text31
<b标签> text32<c标签>text33<d标签>text34</d标签></c标签></b标签>
</a标签>text35  ''')
print(parser.response)