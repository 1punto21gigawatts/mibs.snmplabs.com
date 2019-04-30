#
# PySNMP MIB module Unisphere-Data-COPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-COPS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Gauge32, TimeTicks, Integer32, Counter64, ModuleIdentity, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Counter64", "ModuleIdentity", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdName, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdName")
usdCopsProtocolMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37))
usdCopsProtocolMIB.setRevisions(('2002-01-14 19:01', '2000-02-22 00:00',))
if mibBuilder.loadTexts: usdCopsProtocolMIB.setLastUpdated('200201141901Z')
if mibBuilder.loadTexts: usdCopsProtocolMIB.setOrganization('Unisphere Networks, Inc.')
usdCopsProtocolObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1))
usdCopsProtocolCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 1))
usdCopsProtocolStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 2))
usdCopsProtocolStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3))
usdCopsProtocolSession = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4))
usdCopsProtocolStatisticsScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1))
usdCopsProtocolSessionsCreated = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionsCreated.setStatus('current')
usdCopsProtocolSessionsDeleted = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionsDeleted.setStatus('current')
usdCopsProtocolCurrentSessions = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolCurrentSessions.setStatus('current')
usdCopsProtocolBytesReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolBytesReceived.setStatus('current')
usdCopsProtocolPacketsReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolPacketsReceived.setStatus('current')
usdCopsProtocolBytesSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolBytesSent.setStatus('current')
usdCopsProtocolPacketsSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolPacketsSent.setStatus('current')
usdCopsProtocolKeepAlivesReceived = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesReceived.setStatus('current')
usdCopsProtocolKeepAlivesSent = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolKeepAlivesSent.setStatus('current')
usdCopsProtocolSessionTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1), )
if mibBuilder.loadTexts: usdCopsProtocolSessionTable.setStatus('current')
usdCopsProtocolSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1), ).setIndexNames((0, "Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionClientType"))
if mibBuilder.loadTexts: usdCopsProtocolSessionEntry.setStatus('current')
usdCopsProtocolSessionClientType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: usdCopsProtocolSessionClientType.setStatus('current')
usdCopsProtocolSessionRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRemoteAddress.setStatus('current')
usdCopsProtocolSessionRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRemotePort.setStatus('current')
usdCopsProtocolSessionBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesReceived.setStatus('current')
usdCopsProtocolSessionPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsReceived.setStatus('current')
usdCopsProtocolSessionBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionBytesSent.setStatus('current')
usdCopsProtocolSessionPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionPacketsSent.setStatus('current')
usdCopsProtocolSessionREQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionREQSent.setStatus('current')
usdCopsProtocolSessionDECReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionDECReceived.setStatus('current')
usdCopsProtocolSessionRPTSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionRPTSent.setStatus('current')
usdCopsProtocolSessionDRQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionDRQSent.setStatus('current')
usdCopsProtocolSessionSSQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionSSQSent.setStatus('current')
usdCopsProtocolSessionOPNSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionOPNSent.setStatus('current')
usdCopsProtocolSessionCATReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCATReceived.setStatus('current')
usdCopsProtocolSessionCCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCCSent.setStatus('current')
usdCopsProtocolSessionCCReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionCCReceived.setStatus('current')
usdCopsProtocolSessionSSCSent = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionSSCSent.setStatus('current')
usdCopsProtocolSessionLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 18), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionLocalAddress.setStatus('current')
usdCopsProtocolSessionTransportRouterName = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 1, 4, 1, 1, 19), UsdName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdCopsProtocolSessionTransportRouterName.setStatus('current')
usdCopsProtocolMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4))
usdCopsProtocolMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1))
usdCopsProtocolMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2))
usdCopsProtocolAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 1)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolAuthCompliance = usdCopsProtocolAuthCompliance.setStatus('obsolete')
usdCopsProtocolAuthCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 1, 2)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolAuthCompliance2 = usdCopsProtocolAuthCompliance2.setStatus('current')
usdCopsProtocolGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 1)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolGroup = usdCopsProtocolGroup.setStatus('obsolete')
usdCopsProtocolGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 37, 4, 2, 2)).setObjects(("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsCreated"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionsDeleted"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolCurrentSessions"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolKeepAlivesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemoteAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRemotePort"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionBytesSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionPacketsSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionREQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDECReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionRPTSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionDRQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSQSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionOPNSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCATReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionCCReceived"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionSSCSent"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionLocalAddress"), ("Unisphere-Data-COPS-MIB", "usdCopsProtocolSessionTransportRouterName"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdCopsProtocolGroup2 = usdCopsProtocolGroup2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-COPS-MIB", usdCopsProtocolSessionCCSent=usdCopsProtocolSessionCCSent, usdCopsProtocolMIBGroups=usdCopsProtocolMIBGroups, usdCopsProtocolCurrentSessions=usdCopsProtocolCurrentSessions, usdCopsProtocolSessionREQSent=usdCopsProtocolSessionREQSent, usdCopsProtocolStatisticsScalars=usdCopsProtocolStatisticsScalars, usdCopsProtocolAuthCompliance=usdCopsProtocolAuthCompliance, usdCopsProtocolMIB=usdCopsProtocolMIB, usdCopsProtocolSessionPacketsReceived=usdCopsProtocolSessionPacketsReceived, usdCopsProtocolSessionDRQSent=usdCopsProtocolSessionDRQSent, usdCopsProtocolSessionsCreated=usdCopsProtocolSessionsCreated, usdCopsProtocolSessionClientType=usdCopsProtocolSessionClientType, usdCopsProtocolKeepAlivesSent=usdCopsProtocolKeepAlivesSent, usdCopsProtocolSessionTransportRouterName=usdCopsProtocolSessionTransportRouterName, usdCopsProtocolSessionLocalAddress=usdCopsProtocolSessionLocalAddress, usdCopsProtocolSessionDECReceived=usdCopsProtocolSessionDECReceived, usdCopsProtocolSessionTable=usdCopsProtocolSessionTable, usdCopsProtocolSessionPacketsSent=usdCopsProtocolSessionPacketsSent, usdCopsProtocolBytesSent=usdCopsProtocolBytesSent, usdCopsProtocolSessionRPTSent=usdCopsProtocolSessionRPTSent, usdCopsProtocolPacketsSent=usdCopsProtocolPacketsSent, usdCopsProtocolMIBConformance=usdCopsProtocolMIBConformance, usdCopsProtocolGroup2=usdCopsProtocolGroup2, usdCopsProtocolObjects=usdCopsProtocolObjects, usdCopsProtocolCfg=usdCopsProtocolCfg, usdCopsProtocolSessionEntry=usdCopsProtocolSessionEntry, usdCopsProtocolSessionRemotePort=usdCopsProtocolSessionRemotePort, usdCopsProtocolSessionBytesReceived=usdCopsProtocolSessionBytesReceived, usdCopsProtocolSessionSSQSent=usdCopsProtocolSessionSSQSent, usdCopsProtocolSessionBytesSent=usdCopsProtocolSessionBytesSent, usdCopsProtocolSessionOPNSent=usdCopsProtocolSessionOPNSent, usdCopsProtocolBytesReceived=usdCopsProtocolBytesReceived, usdCopsProtocolMIBCompliances=usdCopsProtocolMIBCompliances, usdCopsProtocolStatistics=usdCopsProtocolStatistics, usdCopsProtocolKeepAlivesReceived=usdCopsProtocolKeepAlivesReceived, usdCopsProtocolSessionCCReceived=usdCopsProtocolSessionCCReceived, usdCopsProtocolPacketsReceived=usdCopsProtocolPacketsReceived, PYSNMP_MODULE_ID=usdCopsProtocolMIB, usdCopsProtocolSessionCATReceived=usdCopsProtocolSessionCATReceived, usdCopsProtocolSessionSSCSent=usdCopsProtocolSessionSSCSent, usdCopsProtocolSessionsDeleted=usdCopsProtocolSessionsDeleted, usdCopsProtocolGroup=usdCopsProtocolGroup, usdCopsProtocolSession=usdCopsProtocolSession, usdCopsProtocolAuthCompliance2=usdCopsProtocolAuthCompliance2, usdCopsProtocolStatus=usdCopsProtocolStatus, usdCopsProtocolSessionRemoteAddress=usdCopsProtocolSessionRemoteAddress)