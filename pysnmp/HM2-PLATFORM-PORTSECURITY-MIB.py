#
# PySNMP MIB module HM2-PLATFORM-PORTSECURITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-PORTSECURITY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hm2PlatformMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "hm2PlatformMibs", "HmEnabledStatus")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, IpAddress, Unsigned32, MibIdentifier, Counter64, ModuleIdentity, iso, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "IpAddress", "Unsigned32", "MibIdentifier", "Counter64", "ModuleIdentity", "iso", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "NotificationType", "ObjectIdentity")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
hm2PlatformPortSecurity = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 20))
hm2PlatformPortSecurity.setRevisions(('2011-07-12 00:00',))
if mibBuilder.loadTexts: hm2PlatformPortSecurity.setLastUpdated('201107120000Z')
if mibBuilder.loadTexts: hm2PlatformPortSecurity.setOrganization('Hirschmann Automation and Control GmbH')
hm2AgentPortSecurityGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 20, 1))
hm2AgentGlobalPortSecurityMode = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentGlobalPortSecurityMode.setStatus('current')
hm2AgentPortSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2), )
if mibBuilder.loadTexts: hm2AgentPortSecurityTable.setStatus('current')
hm2AgentPortSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hm2AgentPortSecurityEntry.setStatus('current')
hm2AgentPortSecurityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 1), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityMode.setStatus('current')
hm2AgentPortSecurityDynamicLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 600)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicLimit.setStatus('current')
hm2AgentPortSecurityStaticLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 64)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticLimit.setStatus('current')
hm2AgentPortSecurityViolationTrapMode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 4), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityViolationTrapMode.setStatus('current')
hm2AgentPortSecurityStaticMACs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1536))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticMACs.setStatus('current')
hm2AgentPortSecurityLastDiscardedMAC = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityLastDiscardedMAC.setStatus('current')
hm2AgentPortSecurityMACAddressAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityMACAddressAdd.setStatus('current')
hm2AgentPortSecurityMACAddressRemove = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityMACAddressRemove.setStatus('current')
hm2AgentPortSecurityMACAddressMove = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 10), HmEnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityMACAddressMove.setStatus('current')
hm2AgentPortSecurityDynamicCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicCount.setStatus('current')
hm2AgentPortSecurityStaticCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticCount.setStatus('current')
hm2AgentPortSecurityViolationTrapCount = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityViolationTrapCount.setStatus('current')
hm2AgentPortSecurityViolationTrapFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 23), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityViolationTrapFrequency.setStatus('current')
hm2AgentPortSecurityAutoDisable = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 248), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentPortSecurityAutoDisable.setStatus('current')
hm2AgentPortSecurityDynamicTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3), )
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicTable.setStatus('current')
hm2AgentPortSecurityDynamicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityDynamicVLANId"), (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityDynamicMACAddress"))
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicEntry.setStatus('current')
hm2AgentPortSecurityDynamicVLANId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicVLANId.setStatus('current')
hm2AgentPortSecurityDynamicMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityDynamicMACAddress.setStatus('current')
hm2AgentPortSecurityStaticTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10), )
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticTable.setStatus('current')
hm2AgentPortSecurityStaticEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityStaticVLANId"), (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityStaticMACAddress"))
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticEntry.setStatus('current')
hm2AgentPortSecurityStaticVLANId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticVLANId.setStatus('current')
hm2AgentPortSecurityStaticMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentPortSecurityStaticMACAddress.setStatus('current')
hm2AgentPortSecurityTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 20, 2))
hm2AgentPortSecurityViolation = NotificationType((1, 3, 6, 1, 4, 1, 248, 12, 20, 2, 1)).setObjects(("IF-MIB", "ifIndex"), ("HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityLastDiscardedMAC"))
if mibBuilder.loadTexts: hm2AgentPortSecurityViolation.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-PORTSECURITY-MIB", hm2AgentPortSecurityEntry=hm2AgentPortSecurityEntry, hm2AgentPortSecurityGroup=hm2AgentPortSecurityGroup, hm2AgentPortSecurityStaticLimit=hm2AgentPortSecurityStaticLimit, hm2AgentPortSecurityStaticCount=hm2AgentPortSecurityStaticCount, hm2AgentPortSecurityMode=hm2AgentPortSecurityMode, hm2AgentPortSecurityDynamicVLANId=hm2AgentPortSecurityDynamicVLANId, hm2PlatformPortSecurity=hm2PlatformPortSecurity, hm2AgentGlobalPortSecurityMode=hm2AgentGlobalPortSecurityMode, hm2AgentPortSecurityTraps=hm2AgentPortSecurityTraps, hm2AgentPortSecurityViolation=hm2AgentPortSecurityViolation, hm2AgentPortSecurityDynamicLimit=hm2AgentPortSecurityDynamicLimit, hm2AgentPortSecurityViolationTrapFrequency=hm2AgentPortSecurityViolationTrapFrequency, hm2AgentPortSecurityStaticEntry=hm2AgentPortSecurityStaticEntry, hm2AgentPortSecurityTable=hm2AgentPortSecurityTable, PYSNMP_MODULE_ID=hm2PlatformPortSecurity, hm2AgentPortSecurityStaticTable=hm2AgentPortSecurityStaticTable, hm2AgentPortSecurityLastDiscardedMAC=hm2AgentPortSecurityLastDiscardedMAC, hm2AgentPortSecurityStaticVLANId=hm2AgentPortSecurityStaticVLANId, hm2AgentPortSecurityDynamicMACAddress=hm2AgentPortSecurityDynamicMACAddress, hm2AgentPortSecurityViolationTrapCount=hm2AgentPortSecurityViolationTrapCount, hm2AgentPortSecurityMACAddressMove=hm2AgentPortSecurityMACAddressMove, hm2AgentPortSecurityDynamicEntry=hm2AgentPortSecurityDynamicEntry, hm2AgentPortSecurityMACAddressAdd=hm2AgentPortSecurityMACAddressAdd, hm2AgentPortSecurityDynamicCount=hm2AgentPortSecurityDynamicCount, hm2AgentPortSecurityViolationTrapMode=hm2AgentPortSecurityViolationTrapMode, hm2AgentPortSecurityMACAddressRemove=hm2AgentPortSecurityMACAddressRemove, hm2AgentPortSecurityAutoDisable=hm2AgentPortSecurityAutoDisable, hm2AgentPortSecurityStaticMACs=hm2AgentPortSecurityStaticMACs, hm2AgentPortSecurityDynamicTable=hm2AgentPortSecurityDynamicTable, hm2AgentPortSecurityStaticMACAddress=hm2AgentPortSecurityStaticMACAddress)