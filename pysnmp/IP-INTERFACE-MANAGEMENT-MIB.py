#
# PySNMP MIB module IP-INTERFACE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IP-INTERFACE-MANAGEMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:44:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
cjnMgmt, = mibBuilder.importSymbols("Cajun-ROOT", "cjnMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Integer32, IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, Bits, ObjectIdentity, Unsigned32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Integer32", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "Bits", "ObjectIdentity", "Unsigned32", "iso", "Counter64")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
cjnIpIfMgmt = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1))
if mibBuilder.loadTexts: cjnIpIfMgmt.setLastUpdated('9902110000Z')
if mibBuilder.loadTexts: cjnIpIfMgmt.setOrganization("Lucent's Concord Technology Center (CTC)")
cjnIpIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1))
cjnIpIfNextIndex = MibScalar((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpIfNextIndex.setStatus('current')
cjnIpIfTable = MibTable((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2), )
if mibBuilder.loadTexts: cjnIpIfTable.setStatus('current')
cjnIpIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1), ).setIndexNames((0, "IP-INTERFACE-MANAGEMENT-MIB", "cjnIpIfIndex"))
if mibBuilder.loadTexts: cjnIpIfEntry.setStatus('current')
cjnIpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpIfIndex.setStatus('current')
cjnIpIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfRowStatus.setStatus('current')
cjnIpIfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIpAddress.setStatus('current')
cjnIpIfIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIpSubnetMask.setStatus('current')
cjnIpIfMacFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ethernetV2", 0), ("snap", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfMacFormat.setStatus('current')
cjnIpIfVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfVlanIfIndex.setStatus('current')
cjnIpIfName = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfName.setStatus('current')
cjnIpIfIpRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("routingAndMgmt", 0), ("mgmtOnly", 1), ("routingOnly", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIpRouting.setStatus('current')
cjnIpIfSpoofCheckEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfSpoofCheckEnabled.setStatus('current')
cjnIpIfProxyArpEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(2)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfProxyArpEnabled.setStatus('current')
cjnIpIfIcmpRedirEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfIcmpRedirEnabled.setStatus('current')
cjnIpIfUdpRbcastMode = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("disable", 0), ("inbound", 1), ("outbound", 2), ("both", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfUdpRbcastMode.setStatus('current')
cjnIpIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfAdminStatus.setStatus('current')
cjnIpIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cjnIpIfStatus.setStatus('current')
cjnIpIfBootpDhcpGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 1751, 2, 43, 3, 1, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cjnIpIfBootpDhcpGateway.setStatus('current')
mibBuilder.exportSymbols("IP-INTERFACE-MANAGEMENT-MIB", cjnIpIfSpoofCheckEnabled=cjnIpIfSpoofCheckEnabled, cjnIpIfMgmt=cjnIpIfMgmt, cjnIpIfIpSubnetMask=cjnIpIfIpSubnetMask, PYSNMP_MODULE_ID=cjnIpIfMgmt, cjnIpIfIndex=cjnIpIfIndex, cjnIpIfIcmpRedirEnabled=cjnIpIfIcmpRedirEnabled, cjnIpIfGroup=cjnIpIfGroup, cjnIpIfUdpRbcastMode=cjnIpIfUdpRbcastMode, cjnIpIfTable=cjnIpIfTable, cjnIpIfEntry=cjnIpIfEntry, cjnIpIfVlanIfIndex=cjnIpIfVlanIfIndex, cjnIpIfName=cjnIpIfName, cjnIpIfRowStatus=cjnIpIfRowStatus, cjnIpIfIpRouting=cjnIpIfIpRouting, cjnIpIfAdminStatus=cjnIpIfAdminStatus, cjnIpIfProxyArpEnabled=cjnIpIfProxyArpEnabled, cjnIpIfBootpDhcpGateway=cjnIpIfBootpDhcpGateway, cjnIpIfStatus=cjnIpIfStatus, cjnIpIfMacFormat=cjnIpIfMacFormat, cjnIpIfIpAddress=cjnIpIfIpAddress, cjnIpIfNextIndex=cjnIpIfNextIndex)