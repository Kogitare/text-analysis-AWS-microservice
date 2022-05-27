rm deployment_package.zip
mkdir build
cd src
echo "### Created build folder."

pipenv requirements > ../build/requirements.txt
cd ../build
python3 -m venv ./
source bin/activate
python3 -m pip install -r requirements.txt
deactivate
echo "### Installed dependencies in virtual environment."

cd lib/python3.10/site-packages
# removing unnecessary files
rm -r pip*
rm -r *.exe
zip -r ../../../../deployment_package.zip .
echo "### Created deployment_package.zip"

cd ../../../../src
zip -g ../deployment_package.zip ./*.py
echo "### Added main scripts to deployment_package.zip"

cd ../
rm -r build
echo "### Removed build folder."