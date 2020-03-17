# Debian File

This is a very simple python script to search package names in the stable/amd64 distribution.

Run

    pipenv install

and then for example:

    pipenv run python debf.py README.txt

It will show you something like...

    avce00 /usr/share/doc/avce00/README.TXT
    cain-examples /usr/share/cain/examples/sbml/dsmts31/README.txt
    code-aster-gui /usr/share/astk/BWidget-1.7.0/README.txt
    dbus-tests /usr/lib/dbus-1.0/debug-build/libexec/installed-tests/dbus/data/sha-1/Readme.txt
    dbus-tests /usr/lib/dbus-1.0/installed-tests/dbus/data/sha-1/Readme.txt
    dynare-doc /usr/share/doc/dynare/examples/dynare++/README.txt
    golang-github-docker-notary-dev /usr/share/gocode/src/github.com/theupdateframework/notary/fixtures/compatibility/notary0.1/README.txt
    imagemagick-6-doc /usr/share/doc/imagemagick-6-common/html/www/Magick++/README.txt
    kadu-common /usr/share/kadu/syntax/chat/Modern Bubbling (Compact)/Readme.txt
    libaacs0 /usr/share/doc/libaacs0/README.txt
    libagg-dev /usr/share/doc/libagg-dev/examples/X11/readme.txt
    libagg2-dev /usr/share/doc/libagg2-dev/examples/X11/readme.txt
    libcapnp-0.7.0 /usr/share/doc/libcapnp-0.7.0/README.txt
    libclang-common-6.0-dev /usr/lib/llvm-6.0/lib/clang/6.0.1/README.txt
    ...

No explanation needed, is it?
