FROM radioastro/meqtrees

ADD src/ src/

ADD kliko.yml src/

WORKDIR /src

CMD python scatterbrane_test.py



