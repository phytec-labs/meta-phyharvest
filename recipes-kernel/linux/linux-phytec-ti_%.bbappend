COMPATIBLE_MACHINE .= "|phyboard-lyra-am62xx-3"
COMPATIBLE_MACHINE .= "|phyboard-lyra-am62xx-3-k3r5"

FILESEXTRAPATHS:prepend := "${THISDIR}/files:"

SRC_URI += " file://phyharvest-spi0-hx1170-changes.patch \
	     file://fragment.cfg \
	   "
