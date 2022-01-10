Podsumowanie zadania:

1. Przygotowałem build na s2i dla wybranego dockera centos7
	a. przygotowałem Dockerfile
	b. przygotowałem skrypty assemble, run, usage
	c. wykonałem deploy aplikacji z jej dependencjami

2. Napisałem prostą aplikację z użyciem Python+Flask
	a. pobieram adres IP klienta i wyświetlam w index.html
	b. każde połączenie i adres IP zapisuje w 2 osobnych plikach .txt i .xml

Kroki do deployu:
1. z lokalizacji Makefile wykonać: make
2. następnie: s2i build app/ python-centos7 sample-app
3. uruchomienie aplikacji z dockerem przez: docker run --name nameDocker -p 80:80 sample-app
4. połączenie przez przeglądarkę IP zaproponowany przez Flask port 80
5. przegladnie plików można przez zalogowanie do powłoki dockera

