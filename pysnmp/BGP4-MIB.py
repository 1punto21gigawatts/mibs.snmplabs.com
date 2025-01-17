#
# PySNMP MIB module BGP4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BGP4-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:18:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Unsigned32, NotificationType, Counter32, Integer32, Bits, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, iso, ModuleIdentity, MibIdentifier, ObjectIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Unsigned32", "NotificationType", "Counter32", "Integer32", "Bits", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "iso", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bgp = ModuleIdentity((1, 3, 6, 1, 2, 1, 15))
if mibBuilder.loadTexts: bgp.setLastUpdated('9405050000Z')
if mibBuilder.loadTexts: bgp.setOrganization('IETF BGP Working Group')
bgpVersion = MibScalar((1, 3, 6, 1, 2, 1, 15, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpVersion.setStatus('current')
bgpLocalAs = MibScalar((1, 3, 6, 1, 2, 1, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpLocalAs.setStatus('current')
bgpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 15, 3), )
if mibBuilder.loadTexts: bgpPeerTable.setStatus('current')
bgpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 3, 1), ).setIndexNames((0, "BGP4-MIB", "bgpPeerRemoteAddr"))
if mibBuilder.loadTexts: bgpPeerEntry.setStatus('current')
bgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerIdentifier.setStatus('current')
bgpPeerState = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerState.setStatus('current')
bgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerAdminStatus.setStatus('current')
bgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerNegotiatedVersion.setStatus('current')
bgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalAddr.setStatus('current')
bgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalPort.setStatus('current')
bgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAddr.setStatus('current')
bgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemotePort.setStatus('current')
bgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAs.setStatus('current')
bgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdates.setStatus('current')
bgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutUpdates.setStatus('current')
bgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInTotalMessages.setStatus('current')
bgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutTotalMessages.setStatus('current')
bgpPeerLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLastError.setStatus('current')
bgpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTransitions.setStatus('current')
bgpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 16), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTime.setStatus('current')
bgpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerConnectRetryInterval.setStatus('current')
bgpPeerHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerHoldTime.setStatus('current')
bgpPeerKeepAlive = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerKeepAlive.setStatus('current')
bgpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerHoldTimeConfigured.setStatus('current')
bgpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerKeepAliveConfigured.setStatus('current')
bgpPeerMinASOriginationInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerMinASOriginationInterval.setStatus('current')
bgpPeerMinRouteAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerMinRouteAdvertisementInterval.setStatus('current')
bgpPeerInUpdateElapsedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 24), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdateElapsedTime.setStatus('current')
bgpIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 15, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpIdentifier.setStatus('current')
bgp4PathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 6), )
if mibBuilder.loadTexts: bgp4PathAttrTable.setStatus('current')
bgp4PathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 6, 1), ).setIndexNames((0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"), (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"), (0, "BGP4-MIB", "bgp4PathAttrPeer"))
if mibBuilder.loadTexts: bgp4PathAttrEntry.setStatus('current')
bgp4PathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrPeer.setStatus('current')
bgp4PathAttrIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefixLen.setStatus('current')
bgp4PathAttrIpAddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefix.setStatus('current')
bgp4PathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrOrigin.setStatus('current')
bgp4PathAttrASPathSegment = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrASPathSegment.setStatus('current')
bgp4PathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrNextHop.setStatus('current')
bgp4PathAttrMultiExitDisc = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrMultiExitDisc.setStatus('current')
bgp4PathAttrLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrLocalPref.setStatus('current')
bgp4PathAttrAtomicAggregate = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lessSpecificRrouteNotSelected", 1), ("lessSpecificRouteSelected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAtomicAggregate.setStatus('current')
bgp4PathAttrAggregatorAS = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAS.setStatus('current')
bgp4PathAttrAggregatorAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAddr.setStatus('current')
bgp4PathAttrCalcLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrCalcLocalPref.setStatus('current')
bgp4PathAttrBest = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrBest.setStatus('current')
bgp4PathAttrUnknown = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrUnknown.setStatus('current')
bgpTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 7))
bgpEstablished = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 1)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpEstablished.setStatus('current')
bgpBackwardTransition = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 2)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpBackwardTransition.setStatus('current')
mibBuilder.exportSymbols("BGP4-MIB", bgp4PathAttrUnknown=bgp4PathAttrUnknown, bgp4PathAttrIpAddrPrefix=bgp4PathAttrIpAddrPrefix, bgpLocalAs=bgpLocalAs, bgpPeerMinASOriginationInterval=bgpPeerMinASOriginationInterval, bgpPeerInUpdates=bgpPeerInUpdates, bgp4PathAttrAggregatorAS=bgp4PathAttrAggregatorAS, bgpIdentifier=bgpIdentifier, bgpEstablished=bgpEstablished, bgpPeerOutUpdates=bgpPeerOutUpdates, bgpPeerKeepAliveConfigured=bgpPeerKeepAliveConfigured, bgpBackwardTransition=bgpBackwardTransition, bgpPeerHoldTimeConfigured=bgpPeerHoldTimeConfigured, bgpPeerFsmEstablishedTransitions=bgpPeerFsmEstablishedTransitions, bgpPeerRemoteAs=bgpPeerRemoteAs, bgpPeerIdentifier=bgpPeerIdentifier, bgpPeerRemoteAddr=bgpPeerRemoteAddr, bgpPeerOutTotalMessages=bgpPeerOutTotalMessages, bgp4PathAttrTable=bgp4PathAttrTable, bgpPeerEntry=bgpPeerEntry, bgpPeerAdminStatus=bgpPeerAdminStatus, bgpPeerState=bgpPeerState, bgpPeerLastError=bgpPeerLastError, bgp=bgp, bgpPeerConnectRetryInterval=bgpPeerConnectRetryInterval, bgp4PathAttrAtomicAggregate=bgp4PathAttrAtomicAggregate, bgp4PathAttrAggregatorAddr=bgp4PathAttrAggregatorAddr, bgpPeerHoldTime=bgpPeerHoldTime, bgpPeerRemotePort=bgpPeerRemotePort, bgpPeerKeepAlive=bgpPeerKeepAlive, bgpVersion=bgpVersion, bgp4PathAttrBest=bgp4PathAttrBest, bgp4PathAttrCalcLocalPref=bgp4PathAttrCalcLocalPref, PYSNMP_MODULE_ID=bgp, bgpPeerLocalPort=bgpPeerLocalPort, bgp4PathAttrIpAddrPrefixLen=bgp4PathAttrIpAddrPrefixLen, bgpTraps=bgpTraps, bgp4PathAttrOrigin=bgp4PathAttrOrigin, bgp4PathAttrMultiExitDisc=bgp4PathAttrMultiExitDisc, bgp4PathAttrEntry=bgp4PathAttrEntry, bgpPeerInTotalMessages=bgpPeerInTotalMessages, bgpPeerFsmEstablishedTime=bgpPeerFsmEstablishedTime, bgpPeerLocalAddr=bgpPeerLocalAddr, bgpPeerMinRouteAdvertisementInterval=bgpPeerMinRouteAdvertisementInterval, bgp4PathAttrPeer=bgp4PathAttrPeer, bgp4PathAttrNextHop=bgp4PathAttrNextHop, bgp4PathAttrASPathSegment=bgp4PathAttrASPathSegment, bgpPeerTable=bgpPeerTable, bgpPeerNegotiatedVersion=bgpPeerNegotiatedVersion, bgpPeerInUpdateElapsedTime=bgpPeerInUpdateElapsedTime, bgp4PathAttrLocalPref=bgp4PathAttrLocalPref)
