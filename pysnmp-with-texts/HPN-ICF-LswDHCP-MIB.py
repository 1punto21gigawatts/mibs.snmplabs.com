#
# PySNMP MIB module HPN-ICF-LswDHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswDHCP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Counter64, iso, Gauge32, MibIdentifier, TimeTicks, ModuleIdentity, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Counter64", "iso", "Gauge32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "IpAddress", "Bits")
MacAddress, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "RowStatus", "TextualConvention", "DisplayString")
hpnicfLswDhcpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8))
hpnicfLswDhcpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLswDhcpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hpnicfLswDhcpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswDhcpMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfLswDhcpMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLswDhcpMib.setDescription('')
hpnicfLswDhcpMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1))
hpnicfDhcpGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1), )
if mibBuilder.loadTexts: hpnicfDhcpGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpGroupTable.setDescription('A table containing the information of dhcp group ')
hpnicfDhcpGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpGroupID"))
if mibBuilder.loadTexts: hpnicfDhcpGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpGroupEntry.setDescription('A table entry containing the information of dhcp group ')
hpnicfDhcpGroupID = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDhcpGroupID.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpGroupID.setDescription(' DHCP group identifier ')
hpnicfIpDhcpServerAddress1 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpDhcpServerAddress1.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpDhcpServerAddress1.setDescription(' The first IP address of DHCP server group ')
hpnicfIpDhcpServerAddress2 = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfIpDhcpServerAddress2.setStatus('current')
if mibBuilder.loadTexts: hpnicfIpDhcpServerAddress2.setDescription(' The second IP address of DHCP server group ')
hpnicfDhcpRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDhcpRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpRowStatus.setDescription(' Operation status of this table entry ')
hpnicfDhcpSecurityTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2), )
if mibBuilder.loadTexts: hpnicfDhcpSecurityTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpSecurityTable.setDescription('A table containing the information of dhcp security ')
hpnicfDhcpSecurityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1), ).setIndexNames((0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpClientIpAddress"))
if mibBuilder.loadTexts: hpnicfDhcpSecurityEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpSecurityEntry.setDescription('A table containing the information of dhcp security ')
hpnicfDhcpClientIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDhcpClientIpAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpClientIpAddress.setDescription(" DHCP client's net ip address ")
hpnicfDhcpClientMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 2), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDhcpClientMacAddress.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpClientMacAddress.setDescription(" DHCP client's mac address ")
hpnicfDhcpClientProperty = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDhcpClientProperty.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpClientProperty.setDescription(' Property of client address ')
hpnicfDhcpClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDhcpClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpClientRowStatus.setDescription(" status of this table's entry. ")
hpnicfDhcpToL3IfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3), )
if mibBuilder.loadTexts: hpnicfDhcpToL3IfTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3IfTable.setDescription('A table configuring dhcp for layer 3 interface')
hpnicfDhcpToL3IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1), ).setIndexNames((0, "HPN-ICF-LswDHCP-MIB", "hpnicfDhcpToL3VlanIfIndex"))
if mibBuilder.loadTexts: hpnicfDhcpToL3IfEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3IfEntry.setDescription('A table configuring dhcp for layer 3 interface ')
hpnicfDhcpToL3VlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfDhcpToL3VlanIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3VlanIfIndex.setDescription(' vlan virtual interface index ')
hpnicfDhcpToL3GroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDhcpToL3GroupId.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3GroupId.setDescription(' DHCP group id for this vlan virtual interface')
hpnicfDhcpToL3AddressCheck = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfDhcpToL3AddressCheck.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3AddressCheck.setDescription(' If dhcp security check enabled for this vlan virtual interface ')
hpnicfDhcpToL3RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 8, 1, 3, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfDhcpToL3RowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfDhcpToL3RowStatus.setDescription(" status of this table's entry. ")
mibBuilder.exportSymbols("HPN-ICF-LswDHCP-MIB", hpnicfDhcpRowStatus=hpnicfDhcpRowStatus, hpnicfDhcpClientIpAddress=hpnicfDhcpClientIpAddress, hpnicfDhcpClientProperty=hpnicfDhcpClientProperty, hpnicfIpDhcpServerAddress2=hpnicfIpDhcpServerAddress2, hpnicfDhcpGroupID=hpnicfDhcpGroupID, hpnicfDhcpToL3GroupId=hpnicfDhcpToL3GroupId, hpnicfDhcpClientMacAddress=hpnicfDhcpClientMacAddress, hpnicfDhcpToL3IfEntry=hpnicfDhcpToL3IfEntry, PYSNMP_MODULE_ID=hpnicfLswDhcpMib, hpnicfLswDhcpMibObject=hpnicfLswDhcpMibObject, hpnicfIpDhcpServerAddress1=hpnicfIpDhcpServerAddress1, hpnicfDhcpToL3IfTable=hpnicfDhcpToL3IfTable, hpnicfDhcpSecurityTable=hpnicfDhcpSecurityTable, hpnicfDhcpToL3RowStatus=hpnicfDhcpToL3RowStatus, hpnicfLswDhcpMib=hpnicfLswDhcpMib, hpnicfDhcpGroupTable=hpnicfDhcpGroupTable, hpnicfDhcpClientRowStatus=hpnicfDhcpClientRowStatus, hpnicfDhcpToL3AddressCheck=hpnicfDhcpToL3AddressCheck, hpnicfDhcpSecurityEntry=hpnicfDhcpSecurityEntry, hpnicfDhcpGroupEntry=hpnicfDhcpGroupEntry, hpnicfDhcpToL3VlanIfIndex=hpnicfDhcpToL3VlanIfIndex)