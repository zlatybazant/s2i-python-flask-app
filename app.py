#!/usr/bin/python

# 1. Podaj mój adres IP - done
# 2. Wysyła odpowiedź na zapytanie w formacie xml,yaml,html,txt
# 3. Wyślij mi wszystkie adresy IP, które połączyły się z aplikacją
#   a. zapisz kazdy rekord polaczenia - TXT,XML - done
#   b. selekcja powtarzajacych sie IP

from flask import Flask, render_template, request
from xml.etree import ElementTree as ET
import string, socket, datetime, os.path

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    if request.method == 'GET':
        def getip():
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                #any ip addr to init connection
                s.connect(('10.255.8.8', 55))
                IP = s.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                s.close()

            with open('iplist.txt', 'a+') as iplist:
                iplist.seek(0)
                data = iplist.read(100)
                if len(data) > 0:
                    iplist.write('\n')
                    iplist.write(IP)
            #---zbudowanie drzewa XML - pierwszego pliku
            if not os.path.isfile('./listaIP.xml'):
                listaAdresow = ET.Element("listaAdresow")
                polaczenieIP = ET.SubElement(listaAdresow, "polaczenieIP")
                ET.SubElement(polaczenieIP, "pole1", name="adressIP").text = IP
               #ET.SubElement(polaczenieIP, "pole2", name="date").text = datestamp
                xmlTree = ET.ElementTree(listaAdresow)
                xmlTree.write("listaIP.xml")
            else:
                #---dodawanie wezla do istniejacego drzewa xml
                xmlTree = ET.parse("listaIP.xml")
                listaAdresow = xmlTree.getroot()
                polaczenieIP = ET.SubElement(listaAdresow, "polaczenieIP")
                ET.SubElement(polaczenieIP, "pole1", name="adressIP").text = IP
                #ET.SubElement(polaczenieIP, "pole2", name="date").text = datestamp
                xmlTree.write("listaIP.xml")

            return IP

        return render_template("index.html", value=getip(), value1='Twój adres IP:')

if __name__ == '__main__':
    app.run(port=8080, debug=True)

