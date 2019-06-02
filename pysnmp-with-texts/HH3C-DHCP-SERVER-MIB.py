#
# PySNMP MIB module HH3C-DHCP-SERVER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-DHCP-SERVER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:25:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
hh3cCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3cCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, iso, Unsigned32, Counter64, MibIdentifier, ModuleIdentity, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "iso", "Unsigned32", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
RowStatus, DisplayString, TextualConvention, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "MacAddress")
hh3cDHCPServer = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 2, 101))
hh3cDHCPServer.setRevisions(('2009-05-06 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cDHCPServer.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hh3cDHCPServer.setLastUpdated('200905060000Z')
if mibBuilder.loadTexts: hh3cDHCPServer.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: hh3cDHCPServer.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: hh3cDHCPServer.setDescription('The MIB module is used for DHCP server.')
hh3cDHCPServerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1))
hh3cDHCPServerIPPoolUsage = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerIPPoolUsage.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerIPPoolUsage.setDescription('Usage factor of DHCP server ip pool.')
hh3cDHCPServerReqTimes = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerReqTimes.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerReqTimes.setDescription('Number of requests received by the DHCP server.')
hh3cDHCPServerReqSuccessTimes = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPServerReqSuccessTimes.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerReqSuccessTimes.setDescription('Number of requests success responses sent by the DHCP server.')
hh3cDHCPServerAvgIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUseThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUseThreshold.setDescription('Threshold of average IP useage of a DHCP server pool in 5 minutes.')
hh3cDHCPServerMaxIpUseThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUseThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUseThreshold.setDescription('Threshold of maximum IP useage of a DHCP server pool in 5 minutes.')
hh3cDHCPServerAllocateThreshold = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPServerAllocateThreshold.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAllocateThreshold.setDescription('Threshold of DHCP server allocated IP address in 5 minutes.')
hh3cDHCPServerTables = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2))
hh3cDHCPServerPoolName = MibScalar((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hh3cDHCPServerPoolName.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerPoolName.setDescription('DHCP server pool name.')
hh3cDHCPSrvGlobalPoolTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolTable.setDescription('A table for creating DHCP server global pools.')
hh3cDHCPSrvGlobalPoolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEntry.setDescription('An entry containing objects for creating or deleting a global pool for the DHCP server.')
hh3cDHCPSrvGlobalPoolName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolName.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolName.setDescription('DHCP server global pool name.')
hh3cDHCPSrvGlobalPoolRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy.')
hh3cDHCPSrvGlobalPoolConfigTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigTable.setDescription('A table containing the configurations of dhcp server global pools.')
hh3cDHCPSrvGlobalPoolConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolConfigEntry.setDescription('An entry containing the objects for configuring the network ip or host ip etc. to global pools for DHCP server.')
hh3cDHCPSrvGlobalPoolType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("null", 0), ("host", 1), ("network", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolType.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolType.setDescription('Type of a DHCP global pool. Any operations of this object will be bound with the operations of hh3cDHCPSrvGlobalPoolNetwork, hh3cDHCPSrvGlobalPoolHostIPAddr, or hh3cDHCPSrvGlobalPoolHostHAddr. That means any operation of this object alone will be regarded as invalid operation.')
hh3cDHCPSrvGlobalPoolNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetwork.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetwork.setDescription('Network ip of a DHCP global pool. To delete a configured network ip, please set hh3cDHCPSrvGlobalPoolCfgUndoFlag to 1.')
hh3cDHCPSrvGlobalPoolNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetworkMask.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolNetworkMask.setDescription('Net mask of a DHCP global pool(network). The SET operation to this object ought to be with the SET of hh3cDHCPSrvGlobalPoolNetwork together, and any SET operation alone to this object will be regarded as an invalid operation. When a network ip of a DHCP global pool was deleted, the net mask would also be deleted automatically, and no further operation needed.')
hh3cDHCPSrvGlobalPoolHostIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostIPAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostIPAddr.setDescription('Host ip of a DHCP global pool. To delete a configured network ip, please set hh3cDHCPSrvGlobalPoolCfgUndoFlag to 2.')
hh3cDHCPSrvGlobalPoolHostMask = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostMask.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostMask.setDescription('Net mask of a DHCP global pool(host) The SET operation to this object ought to be with the SET of hh3cDHCPSrvGlobalPoolHostIPAddr together, and any SET operation alone to this object will be regarded as an invalid operation. When a host ip of a DHCP global pool was deleted, the net mask would also be deleted automatically, and no further operation needed.')
hh3cDHCPSrvGlobalPoolHostHAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 6), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostHAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolHostHAddr.setDescription('Hardware address of a DHCP global pool(host). To delete a configured hardware address, please set hh3cDHCPSrvGlobalPoolCfgUndoFlag to 3.')
hh3cDHCPSrvGlobalPoolCfgUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("undonetworkip", 1), ("undohostip", 2), ("undohosthaddr", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolCfgUndoFlag.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolCfgUndoFlag.setDescription('Flag of undo operation for hh3cDHCPSrvGlobalPoolConfigTable.')
hh3cDHCPSrvGlobalPoolStartAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStartAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStartAddr.setDescription('Start IP of a DHCP global pool. To delete a configured start IP, please set hh3cDHCPSrvGlobalPoolStartAddr to 0. It takes effect only when hh3cDHCPSrvGlobalPoolNetwork is set.')
hh3cDHCPSrvGlobalPoolEndAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 3, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEndAddr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolEndAddr.setDescription('End ip of a DHCP global pool.')
hh3cDHCPSrvGlobalPoolParaTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaTable.setDescription('A table for configuring parameters to DHCP global pools.')
hh3cDHCPSrvGlobalPoolParaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolParaEntry.setDescription('An entry containing the objects for the configurations of parameters of DHCP global pools.')
hh3cDHCPSrvGlbPoolLeaseDay = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 365)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseDay.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseDay.setDescription('Number of days of the lease.')
hh3cDHCPSrvGlbPoolLeaseHour = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseHour.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseHour.setDescription('Number of hours of the lease.')
hh3cDHCPSrvGlbPoolLeaseMinute = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseMinute.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseMinute.setDescription('Number of minutes of the lease.')
hh3cDHCPSrvGlbPoolLeaseUnlimited = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("unlimited", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseUnlimited.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseUnlimited.setDescription('A flag denoting if the lease of a pool is unlimited.')
hh3cDHCPSrvGlbPoolDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolDomainName.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolDomainName.setDescription('Domain name for DHCP clients.')
hh3cDHCPSrvGlbPoolCliGWIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPStr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPStr.setDescription('String of gateway ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, a string is defined to get or configure 8 ip ip at a time.')
hh3cDHCPSrvGlbPoolCliGWIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPUndo.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliGWIPUndo.setDescription('A gateway ip address to delete. This object is only for deleting a given ip of gateway router.')
hh3cDHCPSrvGlbPoolCliDNSIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPStr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPStr.setDescription('String of DNS server ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, a string is defined to get or configure 8 ip at a time.')
hh3cDHCPSrvGlbPoolCliDNSIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPUndo.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliDNSIPUndo.setDescription('A DNS server ip address to delete. This object is only for deleting a given ip of DNS server.')
hh3cDHCPSrvGlbPoolCliNetbiosType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8))).clone(namedValues=NamedValues(("null", 0), ("bnode", 1), ("pnode", 2), ("mnode", 4), ("hnode", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNetbiosType.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNetbiosType.setDescription('NetBios node type for DHCP clients.')
hh3cDHCPSrvGlbPoolCliNbnsIPStr = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPStr.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPStr.setDescription('String of NetBios server ip addresses for DHCP clients. Since mostly 8 ip can be configured for a pool totally, so a string is defined to get or configure 8 ip at a time.')
hh3cDHCPSrvGlbPoolCliNbnsIPUndo = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolCliNbnsIPUndo.setDescription('A NetBios server ip address to delete. This object is only for deleting a given ip of NetBios server.')
hh3cDHCPSrvGlbPoolParaUndoFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("undoDomain", 1), ("undoLease", 2), ("undoGateway", 3), ("undoDns", 4), ("undoNbns", 5), ("undoNbType", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolParaUndoFlag.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolParaUndoFlag.setDescription('Flag of undo-operation for hh3cDHCPSrvGlobalPoolParaTable.')
hh3cDHCPSrvGlbPoolIPInUseReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPInUseReset.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPInUseReset.setDescription('Reset the auto binding ip of the given global pool for DHCP server.')
hh3cDHCPSrvGlbPoolLeaseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 15), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseTime.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseTime.setDescription('Number of timeticks of the lease.')
hh3cDHCPSrvGlbPoolPrimaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 16), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolPrimaryDNSIP.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolPrimaryDNSIP.setDescription('The Primary DNS server IP address to be assigned to the client. To delete a configured Primary DNS server IP, please set hh3cDHCPSrvGlbPoolPrimaryDNSIP to 0. It takes effect only when hh3cDHCPSrvGlobalPoolNetwork is set.')
hh3cDHCPSrvGlbPoolSecondaryDNSIP = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 17), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSecondaryDNSIP.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSecondaryDNSIP.setDescription('The Secondary DNS server IP address to be assigned to the client. To delete a configured Secondary DNS server IP, please set hh3cDHCPSrvGlbPoolSecondaryDNSIP to 0. It takes effect only when hh3cDHCPSrvGlobalPoolNetwork is set.')
hh3cDHCPSrvGlbPoolLeaseSecond = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 4, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 59))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseSecond.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolLeaseSecond.setDescription('Number of seconds of the lease.')
hh3cDHCPSrvGlobalPoolOptionTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionTable.setDescription('A table for configuring options to DHCP global pools.')
hh3cDHCPSrvGlobalPoolOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"), (0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlbPoolOptCode"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolOptionEntry.setDescription('An entry containing the objects for configuring options to DHCP global pools.')
hh3cDHCPSrvGlbPoolOptCode = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 254))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptCode.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptCode.setDescription('Option code.')
hh3cDHCPSrvGlbPoolOptType = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ascii", 1), ("hex", 2), ("ip", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptType.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptType.setDescription('Option type.')
hh3cDHCPSrvGlbPoolOptAscii = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptAscii.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptAscii.setDescription('Ascii string of an option.')
hh3cDHCPSrvGlbPoolOptHexString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 143))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptHexString.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptHexString.setDescription("Hex string of an option. 1st to 16th hex strings, which are 2 bytes, 4 bytes, 6 bytes or 8 bytes, can be configured at most simultaneously. That means the format of each string must be '12', '1234', '123456' or '12345678'.")
hh3cDHCPSrvGlbPoolOptIPString = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 129))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptIPString.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptIPString.setDescription('Ip string of an option. 1 to 8 ip addresses can be configured at most simultaneously.')
hh3cDHCPSrvGlbPoolOptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptRowStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolOptRowStatus.setDescription('RowStatus. Three actions are used: active, createAndGo, destroy.')
hh3cDHCPSrvGlobalPoolStatTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6), )
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatTable.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatTable.setDescription('The statistics of each DHCP address pool.')
hh3cDHCPSrvGlobalPoolStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1), ).setIndexNames((0, "HH3C-DHCP-SERVER-MIB", "hh3cDHCPSrvGlobalPoolName"))
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlobalPoolStatEntry.setDescription('An entry containing the statistics of each DHCP address pool.')
hh3cDHCPSrvGlbPoolIPPoolUsage = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPPoolUsage.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolIPPoolUsage.setDescription('Utilization rate of IP addresses in each DHCP address pool, in percentage.')
hh3cDHCPSrvGlbPoolReqTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolReqTimes.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolReqTimes.setDescription('Number of requests received by each DHCP address pool.')
hh3cDHCPSrvGlbPoolSuccessTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 2, 101, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSuccessTimes.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPSrvGlbPoolSuccessTimes.setDescription('Number of positive responses sent by each DHCP address pool.')
hh3cDHCPServerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3))
hh3cDHCPServerTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0))
hh3cDHCPServerAddrExhaust = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 1)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaust.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaust.setDescription('This trap is generated when the device DHCP server address exhaust.')
hh3cDHCPServerAddrExhaustRecover = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 2)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaustRecover.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAddrExhaustRecover.setDescription('This trap is generated when the device DHCP server address exhaust recover.')
hh3cDHCPServerAvgIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 3)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUsageOverflow.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAvgIpUsageOverflow.setDescription('This trap is generated when the average IP address usage of DHCP server pool in 5 minutes overflows.')
hh3cDHCPServerMaxIpUsageOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 4)).setObjects(("HH3C-DHCP-SERVER-MIB", "hh3cDHCPServerPoolName"))
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUsageOverflow.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerMaxIpUsageOverflow.setDescription('This trap is generated when the maximun IP address usage of DHCP server pool in 5 minutes overflows.')
hh3cDHCPServerAllocateOverflow = NotificationType((1, 3, 6, 1, 4, 1, 25506, 2, 101, 3, 0, 5))
if mibBuilder.loadTexts: hh3cDHCPServerAllocateOverflow.setStatus('current')
if mibBuilder.loadTexts: hh3cDHCPServerAllocateOverflow.setDescription('This trap is generated when the number of DHCP server allocated IP address in 5 minutes overflows.')
mibBuilder.exportSymbols("HH3C-DHCP-SERVER-MIB", hh3cDHCPServer=hh3cDHCPServer, hh3cDHCPSrvGlbPoolLeaseDay=hh3cDHCPSrvGlbPoolLeaseDay, hh3cDHCPSrvGlobalPoolOptionEntry=hh3cDHCPSrvGlobalPoolOptionEntry, hh3cDHCPSrvGlbPoolCliNetbiosType=hh3cDHCPSrvGlbPoolCliNetbiosType, hh3cDHCPSrvGlobalPoolOptionTable=hh3cDHCPSrvGlobalPoolOptionTable, hh3cDHCPServerPoolName=hh3cDHCPServerPoolName, hh3cDHCPServerReqSuccessTimes=hh3cDHCPServerReqSuccessTimes, hh3cDHCPSrvGlobalPoolCfgUndoFlag=hh3cDHCPSrvGlobalPoolCfgUndoFlag, hh3cDHCPSrvGlobalPoolStatEntry=hh3cDHCPSrvGlobalPoolStatEntry, hh3cDHCPSrvGlbPoolLeaseTime=hh3cDHCPSrvGlbPoolLeaseTime, hh3cDHCPSrvGlbPoolLeaseUnlimited=hh3cDHCPSrvGlbPoolLeaseUnlimited, hh3cDHCPSrvGlbPoolCliGWIPStr=hh3cDHCPSrvGlbPoolCliGWIPStr, hh3cDHCPServerAvgIpUsageOverflow=hh3cDHCPServerAvgIpUsageOverflow, hh3cDHCPSrvGlobalPoolStartAddr=hh3cDHCPSrvGlobalPoolStartAddr, hh3cDHCPServerTraps=hh3cDHCPServerTraps, hh3cDHCPSrvGlbPoolOptType=hh3cDHCPSrvGlbPoolOptType, hh3cDHCPSrvGlbPoolLeaseHour=hh3cDHCPSrvGlbPoolLeaseHour, hh3cDHCPSrvGlobalPoolName=hh3cDHCPSrvGlobalPoolName, hh3cDHCPSrvGlbPoolCliGWIPUndo=hh3cDHCPSrvGlbPoolCliGWIPUndo, hh3cDHCPSrvGlbPoolSuccessTimes=hh3cDHCPSrvGlbPoolSuccessTimes, hh3cDHCPServerAllocateOverflow=hh3cDHCPServerAllocateOverflow, hh3cDHCPSrvGlbPoolCliDNSIPUndo=hh3cDHCPSrvGlbPoolCliDNSIPUndo, hh3cDHCPServerObjects=hh3cDHCPServerObjects, hh3cDHCPSrvGlbPoolLeaseMinute=hh3cDHCPSrvGlbPoolLeaseMinute, hh3cDHCPSrvGlbPoolReqTimes=hh3cDHCPSrvGlbPoolReqTimes, hh3cDHCPServerAvgIpUseThreshold=hh3cDHCPServerAvgIpUseThreshold, hh3cDHCPSrvGlbPoolCliDNSIPStr=hh3cDHCPSrvGlbPoolCliDNSIPStr, hh3cDHCPSrvGlobalPoolHostHAddr=hh3cDHCPSrvGlobalPoolHostHAddr, hh3cDHCPSrvGlobalPoolEntry=hh3cDHCPSrvGlobalPoolEntry, hh3cDHCPSrvGlobalPoolHostIPAddr=hh3cDHCPSrvGlobalPoolHostIPAddr, hh3cDHCPSrvGlbPoolIPPoolUsage=hh3cDHCPSrvGlbPoolIPPoolUsage, hh3cDHCPSrvGlbPoolIPInUseReset=hh3cDHCPSrvGlbPoolIPInUseReset, PYSNMP_MODULE_ID=hh3cDHCPServer, hh3cDHCPSrvGlbPoolCliNbnsIPUndo=hh3cDHCPSrvGlbPoolCliNbnsIPUndo, hh3cDHCPSrvGlbPoolParaUndoFlag=hh3cDHCPSrvGlbPoolParaUndoFlag, hh3cDHCPSrvGlbPoolOptIPString=hh3cDHCPSrvGlbPoolOptIPString, hh3cDHCPSrvGlobalPoolHostMask=hh3cDHCPSrvGlobalPoolHostMask, hh3cDHCPSrvGlbPoolOptRowStatus=hh3cDHCPSrvGlbPoolOptRowStatus, hh3cDHCPServerAddrExhaustRecover=hh3cDHCPServerAddrExhaustRecover, hh3cDHCPSrvGlobalPoolParaEntry=hh3cDHCPSrvGlobalPoolParaEntry, hh3cDHCPServerAddrExhaust=hh3cDHCPServerAddrExhaust, hh3cDHCPSrvGlbPoolOptCode=hh3cDHCPSrvGlbPoolOptCode, hh3cDHCPSrvGlobalPoolStatTable=hh3cDHCPSrvGlobalPoolStatTable, hh3cDHCPSrvGlbPoolOptHexString=hh3cDHCPSrvGlbPoolOptHexString, hh3cDHCPSrvGlobalPoolRowStatus=hh3cDHCPSrvGlobalPoolRowStatus, hh3cDHCPSrvGlbPoolSecondaryDNSIP=hh3cDHCPSrvGlbPoolSecondaryDNSIP, hh3cDHCPSrvGlbPoolOptAscii=hh3cDHCPSrvGlbPoolOptAscii, hh3cDHCPSrvGlobalPoolConfigTable=hh3cDHCPSrvGlobalPoolConfigTable, hh3cDHCPSrvGlobalPoolEndAddr=hh3cDHCPSrvGlobalPoolEndAddr, hh3cDHCPSrvGlobalPoolParaTable=hh3cDHCPSrvGlobalPoolParaTable, hh3cDHCPServerIPPoolUsage=hh3cDHCPServerIPPoolUsage, hh3cDHCPServerReqTimes=hh3cDHCPServerReqTimes, hh3cDHCPSrvGlobalPoolConfigEntry=hh3cDHCPSrvGlobalPoolConfigEntry, hh3cDHCPSrvGlbPoolCliNbnsIPStr=hh3cDHCPSrvGlbPoolCliNbnsIPStr, hh3cDHCPSrvGlbPoolLeaseSecond=hh3cDHCPSrvGlbPoolLeaseSecond, hh3cDHCPSrvGlbPoolDomainName=hh3cDHCPSrvGlbPoolDomainName, hh3cDHCPSrvGlbPoolPrimaryDNSIP=hh3cDHCPSrvGlbPoolPrimaryDNSIP, hh3cDHCPServerAllocateThreshold=hh3cDHCPServerAllocateThreshold, hh3cDHCPSrvGlobalPoolTable=hh3cDHCPSrvGlobalPoolTable, hh3cDHCPSrvGlobalPoolNetworkMask=hh3cDHCPSrvGlobalPoolNetworkMask, hh3cDHCPServerMaxIpUsageOverflow=hh3cDHCPServerMaxIpUsageOverflow, hh3cDHCPServerMaxIpUseThreshold=hh3cDHCPServerMaxIpUseThreshold, hh3cDHCPSrvGlobalPoolNetwork=hh3cDHCPSrvGlobalPoolNetwork, hh3cDHCPServerTrapPrefix=hh3cDHCPServerTrapPrefix, hh3cDHCPSrvGlobalPoolType=hh3cDHCPSrvGlobalPoolType, hh3cDHCPServerTables=hh3cDHCPServerTables)