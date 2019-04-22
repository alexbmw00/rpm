# $Copyright: $
# Copyright (c) 1996 - 2009 by Steve Baker
# All Rights reserved
#
# This software is provided as is without any express or implied
# warranties, including, without limitation, the implied warranties
# of merchant-ability and fitness for a particular purpose.

prefix = /usr

CC=gcc

VERSION=0.1
TINY_DEST=tiny
BINDIR=${prefix}/bin
MAN=tiny.1
MANDIR=${prefix}/man/man1

# Uncomment options below for your particular OS:

# Linux defaults:
CFLAGS=-ggdb -Wall -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64
#CFLAGS=-O2 -Wall -fomit-frame-pointer -DLINUX -D_LARGEFILE64_SOURCE -D_FILE_OFFSET_BITS=64
#LDFLAGS=-s

#------------------------------------------------------------

all:	tiny

tiny:	tiny.o $(XOBJS)
	$(CC) $(LDFLAGS) -o $(TINY_DEST) tiny.o $(XOBJS)

tiny.o:	tiny.c

strverscmp.o:	strverscmp.c

clean:
	if [ -x $(TINY_DEST) ]; then rm $(TINY_DEST); fi
	if [ -f tiny.o ]; then rm *.o; fi
	rm -f *~

install: tiny
	install -d $(BINDIR)
	install -d $(MANDIR)
	if [ -e $(TINY_DEST) ]; then \
		install -s $(TINY_DEST) $(BINDIR)/$(TINY_DEST); \
	fi
	install man/$(MAN) $(MANDIR)/$(MAN)

distclean:
	if [ -f tiny.o ]; then rm *.o; fi
	rm -f *~
	

dist:	distclean
	tar zcf ../tiny-$(VERSION).tgz -C .. `cat .tarball`
