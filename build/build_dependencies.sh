rm build/dependencies_package.zip
rm -r tmp_build
mkdir tmp_build
cd src
echo "### Created tmp_build folder."

pipenv requirements > ../tmp_build/requirements.txt
cd ../tmp_build
python3 -m venv ./
source bin/activate
python3 -m pip install -r requirements.txt
deactivate
echo "### Installed dependencies in virtual environment."

mkdir python
cd lib/python*/site-packages
rm -r _distutils_hack mpmath-* pip* pkg_resources setuptools* sympy-* distutils-precedence.pth
find . -type d -name __pycache__ -exec rm -r {} \;
cd ../../../
mv lib/python*/site-packages/* python/
zip -r ../build/dependencies_package.zip python
echo "### Created dependencies_package.zip"

cd ../
rm -r tmp_build
echo "### Removed tmp_build folder."