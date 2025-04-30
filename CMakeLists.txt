cmake_minimum_required(VERSION 3.10)
project(IVS_tools)

# Options to choose what to install
option(INSTALL_CALCULATOR "Install calculator" ON)
option(INSTALL_STDDEV "Install stddev" ON)

# Install calculator executable
if(INSTALL_CALCULATOR)
    install(PROGRAMS ${CMAKE_SOURCE_DIR}/dist/calculator DESTINATION bin)
endif()

# Install stddev executable
if(INSTALL_STDDEV)
    install(PROGRAMS ${CMAKE_SOURCE_DIR}/dist/stddev DESTINATION bin)
endif()

# Install README
# install(FILES README.md DESTINATION share/doc/IVS_tools)

# CPACK settings
set(CPACK_PACKAGE_VERSION "1.0.0")
# set(CPACK_PACKAGE_CONTACT "your_email@example.com")
set(CPACK_GENERATOR "DEB")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Lucenext")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python3")

include(CPack)
