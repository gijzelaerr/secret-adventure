FROM radioastro/meqtrees

ADD src/ src/

RUN mkdir /input /output 

WORKDIR /src

RUN pyxis scatterbrane_test[parameters.json]



