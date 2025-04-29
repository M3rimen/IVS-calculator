#!/bin/bash

# Exit if any command fails
set -e


# Set variables
SRC_DIR="src"
DIST_DIR="$SRC_DIR/dist"
CALCULATOR_EXECUTABLE="calculator"
STDDEV_EXECUTABLE="stddev"

if [[ "$1" != "clean" ]]; then
    # Step 1: Create executables using PyInstaller
    echo "Building executables with PyInstaller..."

    pyinstaller --onefile --paths=src --add-data "src/icon.png:." "$SRC_DIR/$CALCULATOR_EXECUTABLE.py"
    pyinstaller --onefile --add-data "src/math_lib.py:." "$SRC_DIR/$STDDEV_EXECUTABLE.py"

    # Step 2: Build Calculator installer
    echo "Building calculator DEB package..."

    mkdir -p build_calculator
    cd build_calculator

    cmake -DINSTALL_STDDEV=OFF -DINSTALL_CALCULATOR=ON -DCPACK_PACKAGE_NAME="ivs-calculator" ..
    cpack

    cd ..

    # Step 3: Build StdDev installer
    echo "Building stddev DEB package..."

    mkdir -p build_stddev
    cd build_stddev

    cmake -DINSTALL_CALCULATOR=OFF -DINSTALL_STDDEV=ON -DCPACK_PACKAGE_NAME="ivs-stddev" ..
    cpack

    cd ..

    # Step 4: Done
    echo "All done!"
    echo "Generated installers:"
    ls build_calculator/*.deb
    ls build_stddev/*.deb

    mv build_calculator/*.deb install/
    mv build_stddev/*.deb install/
fi

# Cleanup 
echo "Cleaning..."
rm -f calculator.spec
rm -f stddev.spec

rm -rf build
rm -rf build_calculator
rm -rf build_stddev
rm -rf dist
