#!/bin/sh

echo ""
echo ">>> VERSION"
uname -a

echo ""
echo ">>> USER GROUPS"
groups

echo "" > /config/hvac_switch.cfg && \
	echo "{" >> /config/hvac_switch.cfg && \
	echo "    \"pin_on\": $ON," >> /config/hvac_switch.cfg && \
	echo "    \"pin_off\": $OFF," >> /config/hvac_switch.cfg && \
	echo "    \"api_key\": \"$KEY\"," >> /config/hvac_switch.cfg && \
	echo "    \"base_url\": \"$URL\"" >> /config/hvac_switch.cfg && \
	echo "}" >> /config/hvac_switch.cfg

echo ""
echo ">>> CONFIG"
cat /config/hvac_switch.cfg

echo ""
echo ">>> LET'S RUN"
python /exec/switch.py