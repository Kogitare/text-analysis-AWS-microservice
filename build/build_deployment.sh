rm build/deployment_package.zip
rm -r tmp_build
mkdir tmp_build
echo "### Created tmp_build folder."

cd src
zip -r ../build/deployment_package.zip ./*.py
echo "### Added main scripts to deployment_package.zip"

cd ../
rm -r tmp_build
echo "### Removed tmp_build folder."