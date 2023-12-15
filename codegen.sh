rm -rf src
rm -rf swagger-codegen
git clone https://github.com/swagger-api/swagger-codegen
cp swagger/public.swagger.json swagger-codegen
cd swagger-codegen
./run-in-docker.sh mvn package
./run-in-docker.sh generate -i public.swagger.json \
    -l python -o /gen/out -DpackageName=src.cudo_compute
cd ..
cp swagger-codegen/out/README.md docs
cp -r swagger-codegen/out/docs/ docs
cp -r swagger-codegen/out/src/ docs
#rm -rf swagger-codegen

cp helpers/* docs/src/cudo_compute
echo "import src.cudo_compute.auth_config as AuthConfig" >> src/cudo_compute/__init__.py
echo "import cudo_compute.cudo_api as cudo_api" >> src/cudo_compute/__init__.py

python3 tools/authfix.py