# Copyright (C) 2025 MadelynBrown <mtreloar@phytec.com>
# Released under the MIT license (see COPYING.MIT for the terms)

SUMMARY = "phyHaverst Food Drive - weight-scale service recipe"
LICENSE = "CLOSED"

RDEPENDS:${PN} += "bash"

inherit systemd

SYSTEMD_AUTO_ENABLE:${PN} = "enable"
SYSTEMD_SERVICE:${PN} = "phyharvest.service"


SRC_URI = " \
    file://my_panel.py \
    file://displaylbs.py \
    file://readlbs.sh \
    file://phyharvest.service \
    file://wav/applause-01-253125.wav \
    file://wav/CHEERING_AND_CLAPPING_cct.wav \
    file://wav/merry-christmas-sung-89258.wav \
    file://wav/sound2.wav \
    file://wav/sound3.wav \
    file://wav/sound4.wav \
    file://wav/sound9.wav \
    file://wav/thank-you-sweet-man-235977.wav \
    file://wav/w_zen3gzka.wav \
    file://wav/special/almost.wav \
    file://wav/special/final-countdown.wav \
    file://wav/special/goal-reached1.wav \
    file://wav/special/goal-reached2.wav \
    file://wav/special/halfway.wav \
    file://wav/special/quarter.wav \
"

FILES:${PN} += " \
    ${systemd_unitdir}/system/phyharvest.service \
    ${bindir}/my_panel.py \
    ${bindir}/displaylbs.py \
    ${bindir}/readlbs.sh \
    ${bindir}/wav/applause-01-253125.wav \
    ${bindir}/wav/CHEERING_AND_CLAPPING_cct.wav \
    ${bindir}/wav/merry-christmas-sung-89258.wav \
    ${bindir}/wav/sound2.wav \
    ${bindir}/wav/sound3.wav \
    ${bindir}/wav/sound4.wav \
    ${bindir}/wav/sound9.wav \
    ${bindir}/wav/thank-you-sweet-man-235977.wav \
    ${bindir}/wav/w_zen3gzka.wav \
    ${bindir}/wav/special/almost.wav \
    ${bindir}/wav/special/final-countdown.wav \
    ${bindir}/wav/special/goal-reached1.wav \
    ${bindir}/wav/special/goal-reached2.wav \
    ${bindir}/wav/special/halfway.wav \
    ${bindir}/wav/special/quarter.wav \
"

do_install:append() {
  install -d ${D}/${systemd_unitdir}/system
  install -m 0644 ${WORKDIR}/phyharvest.service ${D}/${systemd_unitdir}/system/phyharvest.service

  install -d ${D}/${bindir}
  install -m 0755 ${WORKDIR}/my_panel.py ${D}/${bindir}/my_panel.py
  install -m 0755 ${WORKDIR}/displaylbs.py ${D}/${bindir}/displaylbs.py
  install -m 0755 ${WORKDIR}/readlbs.sh ${D}/${bindir}/readlbs.sh
  install -d 0755 ${WORKDIR}/wav  ${D}/${bindir}/wav
  install -m 0755 ${WORKDIR}/wav/applause-01-253125.wav  ${D}/${bindir}/wav/applause-01-253125.wav 
  install -m 0755 ${WORKDIR}/wav/CHEERING_AND_CLAPPING_cct.wav  ${D}/${bindir}/wav/CHEERING_AND_CLAPPING_cct.wav
  install -m 0755 ${WORKDIR}/wav/merry-christmas-sung-89258.wav  ${D}/${bindir}/wav/merry-christmas-sung-89258.wav
  install -m 0755 ${WORKDIR}/wav/sound2.wav  ${D}/${bindir}/wav/sound2.wav
  install -m 0755 ${WORKDIR}/wav/sound3.wav  ${D}/${bindir}/wav/sound3.wav
  install -m 0755 ${WORKDIR}/wav/sound4.wav  ${D}/${bindir}/wav/sound4.wav
  install -m 0755 ${WORKDIR}/wav/sound9.wav  ${D}/${bindir}/wav/sound9.wav
  install -m 0755 ${WORKDIR}/wav/thank-you-sweet-man-235977.wav  ${D}/${bindir}/wav/thank-you-sweet-man-235977.wav
  install -m 0755 ${WORKDIR}/wav/w_zen3gzka.wav  ${D}/${bindir}/wav/w_zen3gzka.wav
  install -d 0755 ${WORKDIR}/wav/special  ${D}/${bindir}/wav/special
  install -m 0755 ${WORKDIR}/wav/special/almost.wav  ${D}/${bindir}/wav/special/almost.wav
  install -m 0755 ${WORKDIR}/wav/special/final-countdown.wav  ${D}/${bindir}/wav/special/final-countdown.wav
  install -m 0755 ${WORKDIR}/wav/special/goal-reached1.wav  ${D}/${bindir}/wav/special/goal-reached1.wav
  install -m 0755 ${WORKDIR}/wav/special/goal-reached2.wav  ${D}/${bindir}/wav/special/goal-reached2.wav
  install -m 0755 ${WORKDIR}/wav/special/halfway.wav  ${D}/${bindir}/wav/special/halfway.wav
  install -m 0755 ${WORKDIR}/wav/special/quarter.wav  ${D}/${bindir}/wav/special/quarter.wav
}

COMPATIBLE_MACHINE .= "|phyboard-lyra-am62xx-3"
COMPATIBLE_MACHINE .= "|phyboard-lyra-am62xx-3-k3r5"
