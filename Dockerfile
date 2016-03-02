FROM radioastro/meqtrees

ADD src/ src/

WORKDIR /src

RUN python scatterbrane_test.py



