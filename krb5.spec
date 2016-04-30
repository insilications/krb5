#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : krb5
Version  : 1.14.2
Release  : 8
URL      : https://github.com/krb5/krb5/archive/krb5-1.14.2-final.tar.gz
Source0  : https://github.com/krb5/krb5/archive/krb5-1.14.2-final.tar.gz
Summary  : An implementation of Kerberos network authentication
Group    : Development/Tools
License  : BSD-2-Clause MIT
Requires: krb5-bin
Requires: krb5-lib
Requires: krb5-data
Requires: krb5-locales
Requires: krb5-doc
BuildRequires : bison
BuildRequires : dejagnu
BuildRequires : e2fsprogs-data
BuildRequires : e2fsprogs-dev
BuildRequires : e2fsprogs-extras
BuildRequires : expect
BuildRequires : flex
BuildRequires : groff
BuildRequires : openssl-dev
BuildRequires : python-dev
BuildRequires : readline-dev
BuildRequires : yasm

%description
Kerberos Version 5, Release 1.14
Release Notes
The MIT Kerberos Team
---------------------------

%package bin
Summary: bin components for the krb5 package.
Group: Binaries
Requires: krb5-data

%description bin
bin components for the krb5 package.


%package data
Summary: data components for the krb5 package.
Group: Data

%description data
data components for the krb5 package.


%package dev
Summary: dev components for the krb5 package.
Group: Development
Requires: krb5-lib
Requires: krb5-bin
Requires: krb5-data
Provides: krb5-devel

%description dev
dev components for the krb5 package.


%package doc
Summary: doc components for the krb5 package.
Group: Documentation

%description doc
doc components for the krb5 package.


%package lib
Summary: lib components for the krb5 package.
Group: Libraries
Requires: krb5-data

%description lib
lib components for the krb5 package.


%package locales
Summary: locales components for the krb5 package.
Group: Default

%description locales
locales components for the krb5 package.


%prep
%setup -q -n krb5-krb5-1.14.2-final

%build
pushd src
%reconfigure --disable-static --with-system-es --with-system-et
make V=1  %{?_smp_mflags}
popd

%install
rm -rf %{buildroot}
pushd src
%make_install
popd
%find_lang mit-krb5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gss-client
/usr/bin/gss-server
/usr/bin/k5srvutil
/usr/bin/kadmin
/usr/bin/kadmin.local
/usr/bin/kadmind
/usr/bin/kdb5_util
/usr/bin/kdestroy
/usr/bin/kinit
/usr/bin/klist
/usr/bin/kpasswd
/usr/bin/kprop
/usr/bin/kpropd
/usr/bin/kproplog
/usr/bin/krb5-config
/usr/bin/krb5-send-pr
/usr/bin/krb5kdc
/usr/bin/ksu
/usr/bin/kswitch
/usr/bin/ktutil
/usr/bin/kvno
/usr/bin/sclient
/usr/bin/sim_client
/usr/bin/sim_server
/usr/bin/sserver
/usr/bin/uuclient
/usr/bin/uuserver

%files data
%defattr(-,root,root,-)
/usr/share/examples/krb5/kdc.conf
/usr/share/examples/krb5/krb5.conf
/usr/share/examples/krb5/services.append

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/gssapi/gssapi.h
/usr/include/gssapi/gssapi_ext.h
/usr/include/gssapi/gssapi_generic.h
/usr/include/gssapi/gssapi_krb5.h
/usr/include/gssapi/mechglue.h
/usr/include/gssrpc/auth.h
/usr/include/gssrpc/auth_gss.h
/usr/include/gssrpc/auth_gssapi.h
/usr/include/gssrpc/auth_unix.h
/usr/include/gssrpc/clnt.h
/usr/include/gssrpc/netdb.h
/usr/include/gssrpc/pmap_clnt.h
/usr/include/gssrpc/pmap_prot.h
/usr/include/gssrpc/pmap_rmt.h
/usr/include/gssrpc/rename.h
/usr/include/gssrpc/rpc.h
/usr/include/gssrpc/rpc_msg.h
/usr/include/gssrpc/svc.h
/usr/include/gssrpc/svc_auth.h
/usr/include/gssrpc/types.h
/usr/include/gssrpc/xdr.h
/usr/include/kadm5/admin.h
/usr/include/kadm5/chpass_util_strings.h
/usr/include/kadm5/kadm_err.h
/usr/include/krb5/ccselect_plugin.h
/usr/include/krb5/clpreauth_plugin.h
/usr/include/krb5/hostrealm_plugin.h
/usr/include/krb5/kadm5_hook_plugin.h
/usr/include/krb5/kdcpreauth_plugin.h
/usr/include/krb5/krb5.h
/usr/include/krb5/localauth_plugin.h
/usr/include/krb5/locate_plugin.h
/usr/include/krb5/plugin.h
/usr/include/krb5/preauth_plugin.h
/usr/include/krb5/pwqual_plugin.h
/usr/lib64/*.so
/usr/lib64/pkgconfig/*.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
%doc /usr/share/man/man8/*
%exclude /usr/share/man/man5/.k5identity.5
%exclude /usr/share/man/man5/.k5login.5

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
/usr/lib64/krb5/plugins/kdb/db2.so
/usr/lib64/krb5/plugins/preauth/otp.so
/usr/lib64/krb5/plugins/preauth/pkinit.so
/usr/lib64/krb5/plugins/preauth/test.so
/usr/lib64/krb5/plugins/tls/k5tls.so

%files locales -f mit-krb5.lang 
%defattr(-,root,root,-)

