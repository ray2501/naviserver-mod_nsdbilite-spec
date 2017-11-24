#!/usr/bin/tclsh

set arch "x86_64"
set base "naviserver-mod_nsdbilite-0.2"

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb naviserver-mod_nsdbilite.spec]
exec >@stdout 2>@stderr {*}$buildit
