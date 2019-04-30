#
# PySNMP MIB module CTRON-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-DHCP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
nwIpComponents, nwIpMibs, nwIpRouter, nwIpClientServices = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpComponents", "nwIpMibs", "nwIpRouter", "nwIpClientServices")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, Bits, Unsigned32, NotificationType, Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, iso, TimeTicks, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "Bits", "Unsigned32", "NotificationType", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "iso", "TimeTicks", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention, PhysAddress = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress")
ctDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2))
ctDhcpServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1))
ctDhcpInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2))
ctDhcpClientStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3))
ctDhcpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpAdminStatus.setStatus('mandatory')
ctDhcpOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOperStatus.setStatus('mandatory')
ctDhcpDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDiscovers.setStatus('mandatory')
ctDhcpOffers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOffers.setStatus('mandatory')
ctDhcpRequests = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpRequests.setStatus('mandatory')
ctDhcpDeclines = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDeclines.setStatus('mandatory')
ctDhcpReleases = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpReleases.setStatus('mandatory')
ctDhcpAcks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpAcks.setStatus('mandatory')
ctDhcpNaks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNaks.setStatus('mandatory')
ctDhcpOtherServers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOtherServers.setStatus('mandatory')
ctDhcpProtocolErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setStatus('mandatory')
ctDhcpServerTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpServerTime.setStatus('mandatory')
ctDhcpNoOfActiveClients = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setStatus('mandatory')
ctDhcpReclaimIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpReclaimIP.setStatus('mandatory')
ctDhcpServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1), )
if mibBuilder.loadTexts: ctDhcpServerIfTable.setStatus('mandatory')
ctDhcpServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpIfIndex"))
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setStatus('mandatory')
ctDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfIndex.setStatus('mandatory')
ctDhcpIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setStatus('mandatory')
ctDhcpIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setStatus('mandatory')
ctDhcpIfServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setStatus('mandatory')
ctDhcpIfNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setStatus('mandatory')
ctDhcpIfSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setStatus('mandatory')
ctDhcpIfLowestaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setStatus('mandatory')
ctDhcpIfHighestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setStatus('mandatory')
ctDhcpIfAddressesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setStatus('mandatory')
ctDhcpIfAddressesFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setStatus('mandatory')
ctDhcpIfLeasePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setStatus('mandatory')
ctDhcpIfDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setStatus('mandatory')
ctDhcpIfDomainNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setStatus('mandatory')
ctDhcpIfDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 14), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainName.setStatus('mandatory')
ctDhcpIfWINServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfWINServer.setStatus('mandatory')
ctDhcpClientStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1), )
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setStatus('mandatory')
ctDhcpClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpClientStatsID"))
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setStatus('mandatory')
ctDhcpClientStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientStatsID.setStatus('mandatory')
ctDhcpClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientName.setStatus('mandatory')
ctDhcpClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientIP.setStatus('mandatory')
ctDhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientID.setStatus('mandatory')
ctDhcpEndOfLease = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpEndOfLease.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-DHCP-MIB", ctDhcpIfDomainName=ctDhcpIfDomainName, ctDhcpProtocolErrors=ctDhcpProtocolErrors, ctDhcpServerTime=ctDhcpServerTime, ctDhcp=ctDhcp, ctDhcpIfServerAddress=ctDhcpIfServerAddress, ctDhcpIfSubnetMask=ctDhcpIfSubnetMask, ctDhcpClientStatsTable=ctDhcpClientStatsTable, ctDhcpClientStatsEntry=ctDhcpClientStatsEntry, ctDhcpClientStatsID=ctDhcpClientStatsID, ctDhcpIfAddressesUsed=ctDhcpIfAddressesUsed, ctDhcpNaks=ctDhcpNaks, ctDhcpClientName=ctDhcpClientName, ctDhcpIfNetworkAddress=ctDhcpIfNetworkAddress, ctDhcpNoOfActiveClients=ctDhcpNoOfActiveClients, ctDhcpServerIfTable=ctDhcpServerIfTable, ctDhcpReclaimIP=ctDhcpReclaimIP, ctDhcpIfIndex=ctDhcpIfIndex, ctDhcpIfLeasePeriod=ctDhcpIfLeasePeriod, ctDhcpIfDefaultGateway=ctDhcpIfDefaultGateway, ctDhcpDeclines=ctDhcpDeclines, ctDhcpDiscovers=ctDhcpDiscovers, ctDhcpIfDomainNameServer=ctDhcpIfDomainNameServer, ctDhcpIfAdminStatus=ctDhcpIfAdminStatus, ctDhcpReleases=ctDhcpReleases, ctDhcpEndOfLease=ctDhcpEndOfLease, ctDhcpIfAddressesFree=ctDhcpIfAddressesFree, ctDhcpInterfaceConfig=ctDhcpInterfaceConfig, ctDhcpOffers=ctDhcpOffers, ctDhcpOperStatus=ctDhcpOperStatus, ctDhcpServerIfEntry=ctDhcpServerIfEntry, ctDhcpIfLowestaddress=ctDhcpIfLowestaddress, ctDhcpServerStats=ctDhcpServerStats, ctDhcpRequests=ctDhcpRequests, ctDhcpIfWINServer=ctDhcpIfWINServer, ctDhcpClientID=ctDhcpClientID, ctDhcpAdminStatus=ctDhcpAdminStatus, ctDhcpAcks=ctDhcpAcks, ctDhcpClientIP=ctDhcpClientIP, ctDhcpIfHighestAddress=ctDhcpIfHighestAddress, ctDhcpOtherServers=ctDhcpOtherServers, ctDhcpIfOperStatus=ctDhcpIfOperStatus, ctDhcpClientStatusTable=ctDhcpClientStatusTable)