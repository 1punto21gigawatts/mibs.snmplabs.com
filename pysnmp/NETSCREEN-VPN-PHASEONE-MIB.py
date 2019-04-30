#
# PySNMP MIB module NETSCREEN-VPN-PHASEONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-VPN-PHASEONE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
netscreenVpn, netscreenVpnMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVpn", "netscreenVpnMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ObjectIdentity, MibIdentifier, Gauge32, Bits, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity, TimeTicks, Counter32, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "Bits", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "IpAddress", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenVpnPhaseoneMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 4, 0, 5))
netscreenVpnPhaseoneMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2001-05-14 00:00',))
if mibBuilder.loadTexts: netscreenVpnPhaseoneMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVpnPhaseoneMibModule.setOrganization('Juniper Networks, Inc.')
nsVpnPhaseOneCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 4, 5))
nsVpnPhOneTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1), )
if mibBuilder.loadTexts: nsVpnPhOneTable.setStatus('current')
nsVpnPhOneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1), ).setIndexNames((0, "NETSCREEN-VPN-PHASEONE-MIB", "nsVpnPhOneIndex"))
if mibBuilder.loadTexts: nsVpnPhOneEntry.setStatus('current')
nsVpnPhOneIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneIndex.setStatus('current')
nsVpnPhOneName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneName.setStatus('current')
nsVpnPhOneAuthMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("preshare", 0), ("rsa-sig", 1), ("dsa-sig", 2), ("rsa-enc", 3), ("rsa-rev", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneAuthMethod.setStatus('current')
nsVpnPhOneDhGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneDhGroup.setStatus('current')
nsVpnPhOneEncryp = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("null", 0), ("des", 1), ("des3", 2), ("aes", 3), ("aes-192", 4), ("aes-256", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneEncryp.setStatus('current')
nsVpnPhOneHash = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("md5", 1), ("sha", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneHash.setStatus('current')
nsVpnPhOneLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneLifetime.setStatus('current')
nsVpnPhOneLifetimeMeasure = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("second", 0), ("minute", 1), ("hours", 2), ("days", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneLifetimeMeasure.setStatus('current')
nsVpnPhOneVsys = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 4, 5, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVpnPhOneVsys.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-VPN-PHASEONE-MIB", nsVpnPhaseOneCfg=nsVpnPhaseOneCfg, nsVpnPhOneVsys=nsVpnPhOneVsys, nsVpnPhOneIndex=nsVpnPhOneIndex, nsVpnPhOneEntry=nsVpnPhOneEntry, PYSNMP_MODULE_ID=netscreenVpnPhaseoneMibModule, netscreenVpnPhaseoneMibModule=netscreenVpnPhaseoneMibModule, nsVpnPhOneLifetime=nsVpnPhOneLifetime, nsVpnPhOneName=nsVpnPhOneName, nsVpnPhOneAuthMethod=nsVpnPhOneAuthMethod, nsVpnPhOneLifetimeMeasure=nsVpnPhOneLifetimeMeasure, nsVpnPhOneHash=nsVpnPhOneHash, nsVpnPhOneDhGroup=nsVpnPhOneDhGroup, nsVpnPhOneTable=nsVpnPhOneTable, nsVpnPhOneEncryp=nsVpnPhOneEncryp)