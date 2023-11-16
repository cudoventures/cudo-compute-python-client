rm -rf src
rm -rf swagger-codegen
git clone https://github.com/swagger-api/swagger-codegen
cp swagger/public.swagger.json swagger-codegen
cd swagger-codegen
./run-in-docker.sh mvn package
./run-in-docker.sh generate -i public.swagger.json \
    -l python -o /gen/out -DpackageName=src.cudo_compute
cd ..
cp -r swagger-codegen/out/src src

