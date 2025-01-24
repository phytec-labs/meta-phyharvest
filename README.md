# meta-phyharvest 

To see about the demo visit the Hacker project here: https://www.hackster.io/MadelynT/crabmas-in-the-sand-a-techy-food-donation-box-5557a8#overview

Yocto meta-layer for PhyHarvest Food box with custom recipes for load cell scales, HX711 ADC, and festive sound effects.

This meta-layer enables the phyHarvest Food Drive Box demo. This layers inherits PHYTEC's phyCORE-AM62x Development Kit (MACHINE=phyboard-lyra-am62xx-3) and can serve as a basis for further customizing reference meta-layer for preparing production-ready software images. 

This was tested with BSP-Yocto-Ampliphy-AM62x-PD24.1.0

## Requirements:
  - PCM-071-5432DE11I.A0 (HS-FS SOM)
  - NHD-0420D3Z-NSW-BBW-V3 LCD Module connected to SPI0
  - Load Cells and HX711 Module connected to GPIO0_36 (DOUT) and GPIO1_13 (PD_SCK)
  - Audio Jack Speaker
  - TXS0104E Boost Converter for SPI0 signals (3V3 -> 5V0)
  - Ubuntu 22.04 LTS, 64-bit Host Machine with root permission.
      - If using a virtual machine, VMWare Workstation, VMWare Player, and VirtualBox are all viable solutions.
      - At least 100GB disk space free
      - At least 8GB of RAM
      - At least 4x processing cores available to the Host Machine
      - Active Internet connection

## Meta Layer provides:
  - systemd service to poll the weight scale and display the weight on the SPI display
  - systemd service to poll the weight scale and play crabmas music when a change in weight is detected and when weight milestones are reached (goal 300lbs)

## Instructions: 
In order to evaluate this in your phyCORE-AM62x BSP setup:

Navigate to your BSP's sources directory: 

```sh
cd $BUILDDIR/../sources
```

clone this repo and branch: 

```sh
git clone https://github.com/phytec-labs/meta-phyharvest.git -b main
```

Enable the layer in your build: 

```sh
cd $BUILDDIR
bitbake-layers add-layer ../sources/meta-phyharvest
```

Build your target's image with bitbake

```sh
bitbake phytec-headless-image
```

Verify build, by confirming main script file is present in working directory

```sh
find ./tmp-ampliphy-xwayland/work -name "displaylbs.py"
```
