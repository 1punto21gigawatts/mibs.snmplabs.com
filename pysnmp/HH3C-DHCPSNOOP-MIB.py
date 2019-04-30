#
# PySNMP MIB module HH3C-DHCPSNOOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCPSNOOP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
hh3cdot1qVlanIndex, = mibBuilder.importSymbols("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, NotificationType, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Unsigned32, Gauge32, IpAddress, TimeTicks, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "NotificationType", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Unsigned32", "Gauge32", "IpAddress", "TimeTicks", "MibIdentifier", "Integer32")
DisplayString, TruthValue, TextualConvention, RowStatus, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus", "MacAddress")
hh3cDhcpSnoop = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 36))
if mibBuilder.loadTexts: hh3cDhcpSnoop.setLastUpdated('200501140000Z')
if mibBuilder.loadTexts: hh3cDhcpSnoop.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cDhcpSnoopMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1))
hh3cDhcpSnoopEnable = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopEnable.setStatus('current')
hh3cDhcpSnoopTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2), )
if mibBuilder.loadTexts: hh3cDhcpSnoopTable.setStatus('current')
hh3cDhcpSnoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1), ).setIndexNames((0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddressType"), (0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopClientIpAddress"))
if mibBuilder.loadTexts: hh3cDhcpSnoopEntry.setStatus('current')
hh3cDhcpSnoopClientIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 1), InetAddressType().clone('ipv4'))
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddressType.setStatus('current')
hh3cDhcpSnoopClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 2), InetAddress())
if mibBuilder.loadTexts: hh3cDhcpSnoopClientIpAddress.setStatus('current')
hh3cDhcpSnoopClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientMacAddress.setStatus('current')
hh3cDhcpSnoopClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientProperty.setStatus('current')
hh3cDhcpSnoopClientUnitNum = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDhcpSnoopClientUnitNum.setStatus('current')
hh3cDhcpSnoopTrustTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3), )
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustTable.setStatus('current')
hh3cDhcpSnoopTrustEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustEntry.setStatus('current')
hh3cDhcpSnoopTrustStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("untrusted", 0), ("trusted", 1))).clone('untrusted')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopTrustStatus.setStatus('current')
hh3cDhcpSnoopVlanTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4), )
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanTable.setStatus('current')
hh3cDhcpSnoopVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1), ).setIndexNames((0, "HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopVlanIndex"))
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEntry.setStatus('current')
hh3cDhcpSnoopVlanIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanIndex.setStatus('current')
hh3cDhcpSnoopVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 36, 1, 4, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDhcpSnoopVlanEnable.setStatus('current')
hh3cDhcpSnoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2))
hh3cDhcpSnoopTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0))
hh3cDhcpSnoopTrapsObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1))
hh3cDhcpSnoopSpoofServerMac = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 1), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerMac.setStatus('current')
hh3cDhcpSnoopSpoofServerIP = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 1, 2), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerIP.setStatus('current')
hh3cDhcpSnoopSpoofServerDetected = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 36, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("HH3C-LswVLAN-MIB", "hh3cdot1qVlanIndex"), ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerMac"), ("HH3C-DHCPSNOOP-MIB", "hh3cDhcpSnoopSpoofServerIP"))
if mibBuilder.loadTexts: hh3cDhcpSnoopSpoofServerDetected.setStatus('current')
mibBuilder.exportSymbols("HH3C-DHCPSNOOP-MIB", hh3cDhcpSnoopTrapsObject=hh3cDhcpSnoopTrapsObject, hh3cDhcpSnoopTrustEntry=hh3cDhcpSnoopTrustEntry, hh3cDhcpSnoopSpoofServerIP=hh3cDhcpSnoopSpoofServerIP, hh3cDhcpSnoopVlanEntry=hh3cDhcpSnoopVlanEntry, hh3cDhcpSnoopTrapsPrefix=hh3cDhcpSnoopTrapsPrefix, hh3cDhcpSnoopVlanTable=hh3cDhcpSnoopVlanTable, hh3cDhcpSnoopClientMacAddress=hh3cDhcpSnoopClientMacAddress, hh3cDhcpSnoopSpoofServerMac=hh3cDhcpSnoopSpoofServerMac, hh3cDhcpSnoopTrustTable=hh3cDhcpSnoopTrustTable, hh3cDhcpSnoopEntry=hh3cDhcpSnoopEntry, hh3cDhcpSnoopTable=hh3cDhcpSnoopTable, hh3cDhcpSnoopClientIpAddressType=hh3cDhcpSnoopClientIpAddressType, hh3cDhcpSnoopMibObject=hh3cDhcpSnoopMibObject, hh3cDhcpSnoopClientUnitNum=hh3cDhcpSnoopClientUnitNum, hh3cDhcpSnoop=hh3cDhcpSnoop, hh3cDhcpSnoopSpoofServerDetected=hh3cDhcpSnoopSpoofServerDetected, hh3cDhcpSnoopVlanEnable=hh3cDhcpSnoopVlanEnable, hh3cDhcpSnoopEnable=hh3cDhcpSnoopEnable, hh3cDhcpSnoopClientProperty=hh3cDhcpSnoopClientProperty, PYSNMP_MODULE_ID=hh3cDhcpSnoop, hh3cDhcpSnoopTrustStatus=hh3cDhcpSnoopTrustStatus, hh3cDhcpSnoopTraps=hh3cDhcpSnoopTraps, hh3cDhcpSnoopVlanIndex=hh3cDhcpSnoopVlanIndex, hh3cDhcpSnoopClientIpAddress=hh3cDhcpSnoopClientIpAddress)