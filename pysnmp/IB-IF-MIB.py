#
# PySNMP MIB module IB-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IB-IF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
infinibandMIB, IbIpoibClientIdentifier, IbVirtualLane = mibBuilder.importSymbols("IB-TC-MIB", "infinibandMIB", "IbIpoibClientIdentifier", "IbVirtualLane")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, NotificationType, TimeTicks, ModuleIdentity, Integer32, Unsigned32, Counter32, IpAddress, Counter64, MibIdentifier, Gauge32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "NotificationType", "TimeTicks", "ModuleIdentity", "Integer32", "Unsigned32", "Counter32", "IpAddress", "Counter64", "MibIdentifier", "Gauge32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibIfMIB = ModuleIdentity((1, 3, 6, 1, 3, 117, 2))
ibIfMIB.setRevisions(('2006-06-27 00:00',))
if mibBuilder.loadTexts: ibIfMIB.setLastUpdated('200606270000Z')
if mibBuilder.loadTexts: ibIfMIB.setOrganization('IETF IP over IB (IPOIB) Working Group')
ibIfObjects = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 1))
ibIfNotifications = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 2))
ibIfConformance = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3))
ibIfPortStatTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 1), )
if mibBuilder.loadTexts: ibIfPortStatTable.setStatus('current')
ibIfPortStatEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 1, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIfPortStatIfIndex"))
if mibBuilder.loadTexts: ibIfPortStatEntry.setStatus('current')
ibIfPortStatIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIfPortStatIfIndex.setStatus('current')
ibIfPortSymbolErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortSymbolErrs.setStatus('current')
ibIfPortLinkErrRecovery = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortLinkErrRecovery.setStatus('current')
ibIfPortLinkDowned = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortLinkDowned.setStatus('current')
ibIfPortStatLocalPhyErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatLocalPhyErrs.setStatus('current')
ibIfPortStatMalPktErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatMalPktErrs.setStatus('current')
ibIfPortStatRcvRemPhyErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatRcvRemPhyErrs.setStatus('current')
ibIfPortStatRcvConstrErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatRcvConstrErrs.setStatus('current')
ibIfPortStatInactDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatInactDiscards.setStatus('current')
ibIfPortStatNeighMTUDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatNeighMTUDiscards.setStatus('current')
ibIfPortStatSwLifetimeDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatSwLifetimeDiscards.setStatus('current')
ibIfPortStatHOQLifetimeDiscards = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatHOQLifetimeDiscards.setStatus('current')
ibIfPortStatLinkIntergrityErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatLinkIntergrityErrs.setStatus('current')
ibIfPortStatExcBufOverrunErrs = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatExcBufOverrunErrs.setStatus('current')
ibIfPortStatVL15Dropped = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfPortStatVL15Dropped.setStatus('current')
ibIfVLTrafficTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 2), )
if mibBuilder.loadTexts: ibIfVLTrafficTable.setStatus('current')
ibIfVLTrafficEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 2, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIfVLTrafficIfIndex"), (0, "IB-IF-MIB", "ibIfVLIndex"))
if mibBuilder.loadTexts: ibIfVLTrafficEntry.setStatus('current')
ibIfVLTrafficIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIfVLTrafficIfIndex.setStatus('current')
ibIfVLIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 2), IbVirtualLane())
if mibBuilder.loadTexts: ibIfVLIndex.setStatus('current')
ibIfVLOutOctets = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLOutOctets.setStatus('current')
ibIfVLOutPkts = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLOutPkts.setStatus('current')
ibIfVLInOctets = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLInOctets.setStatus('current')
ibIfVLInPkts = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIfVLInPkts.setStatus('current')
ibIpoibLinkLayerAddrTable = MibTable((1, 3, 6, 1, 3, 117, 2, 1, 3), )
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrTable.setStatus('current')
ibIpoibLinkLayerAddrEntry = MibTableRow((1, 3, 6, 1, 3, 117, 2, 1, 3, 1), ).setIndexNames((0, "IB-IF-MIB", "ibIpoibLinkLayerIfIndex"), (0, "IB-IF-MIB", "ibIpoibLinkLayerIndex"))
if mibBuilder.loadTexts: ibIpoibLinkLayerAddrEntry.setStatus('current')
ibIpoibLinkLayerIfIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: ibIpoibLinkLayerIfIndex.setStatus('current')
ibIpoibLinkLayerIndex = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: ibIpoibLinkLayerIndex.setStatus('current')
ibIpoibLinkLayerAddr = MibTableColumn((1, 3, 6, 1, 3, 117, 2, 1, 3, 1, 3), IbIpoibClientIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibIpoibLinkLayerAddr.setStatus('current')
ibIfCompliances = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3, 1))
ibIfMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 117, 2, 3, 2))
ibIfBasicCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 2, 3, 1, 1)).setObjects(("IB-IF-MIB", "ibIfStatMandatoryPortStatGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfBasicCompliance = ibIfBasicCompliance.setStatus('current')
ibIfFullCompliance = ModuleCompliance((1, 3, 6, 1, 3, 117, 2, 3, 1, 2)).setObjects(("IB-IF-MIB", "ibIfStatMandatoryPortStatGroup"), ("IB-IF-MIB", "ibIfStatOptionalPortStatGroup"), ("IB-IF-MIB", "ibIfVLTrafficGroup"), ("IB-IF-MIB", "ibIpoibLinkAddrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfFullCompliance = ibIfFullCompliance.setStatus('current')
ibIfStatMandatoryPortStatGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 1)).setObjects(("IB-IF-MIB", "ibIfPortSymbolErrs"), ("IB-IF-MIB", "ibIfPortLinkErrRecovery"), ("IB-IF-MIB", "ibIfPortLinkDowned"), ("IB-IF-MIB", "ibIfPortStatRcvRemPhyErrs"), ("IB-IF-MIB", "ibIfPortStatRcvConstrErrs"), ("IB-IF-MIB", "ibIfPortStatLinkIntergrityErrs"), ("IB-IF-MIB", "ibIfPortStatExcBufOverrunErrs"), ("IB-IF-MIB", "ibIfPortStatVL15Dropped"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfStatMandatoryPortStatGroup = ibIfStatMandatoryPortStatGroup.setStatus('current')
ibIfStatOptionalPortStatGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 2)).setObjects(("IB-IF-MIB", "ibIfPortStatLocalPhyErrs"), ("IB-IF-MIB", "ibIfPortStatMalPktErrs"), ("IB-IF-MIB", "ibIfPortStatInactDiscards"), ("IB-IF-MIB", "ibIfPortStatNeighMTUDiscards"), ("IB-IF-MIB", "ibIfPortStatSwLifetimeDiscards"), ("IB-IF-MIB", "ibIfPortStatHOQLifetimeDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfStatOptionalPortStatGroup = ibIfStatOptionalPortStatGroup.setStatus('current')
ibIfVLTrafficGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 3)).setObjects(("IB-IF-MIB", "ibIfVLOutOctets"), ("IB-IF-MIB", "ibIfVLOutPkts"), ("IB-IF-MIB", "ibIfVLInOctets"), ("IB-IF-MIB", "ibIfVLInPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIfVLTrafficGroup = ibIfVLTrafficGroup.setStatus('current')
ibIpoibLinkAddrGroup = ObjectGroup((1, 3, 6, 1, 3, 117, 2, 3, 2, 4)).setObjects(("IB-IF-MIB", "ibIpoibLinkLayerAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ibIpoibLinkAddrGroup = ibIpoibLinkAddrGroup.setStatus('current')
mibBuilder.exportSymbols("IB-IF-MIB", ibIfCompliances=ibIfCompliances, ibIfMIBGroups=ibIfMIBGroups, ibIfPortStatNeighMTUDiscards=ibIfPortStatNeighMTUDiscards, ibIfBasicCompliance=ibIfBasicCompliance, ibIpoibLinkLayerAddr=ibIpoibLinkLayerAddr, ibIfConformance=ibIfConformance, ibIfPortStatMalPktErrs=ibIfPortStatMalPktErrs, ibIfVLTrafficIfIndex=ibIfVLTrafficIfIndex, ibIpoibLinkLayerAddrEntry=ibIpoibLinkLayerAddrEntry, ibIpoibLinkAddrGroup=ibIpoibLinkAddrGroup, ibIfNotifications=ibIfNotifications, ibIfPortStatIfIndex=ibIfPortStatIfIndex, ibIfPortStatRcvConstrErrs=ibIfPortStatRcvConstrErrs, ibIfStatMandatoryPortStatGroup=ibIfStatMandatoryPortStatGroup, ibIfObjects=ibIfObjects, ibIfPortStatLinkIntergrityErrs=ibIfPortStatLinkIntergrityErrs, ibIfVLInOctets=ibIfVLInOctets, ibIfVLIndex=ibIfVLIndex, ibIfVLTrafficTable=ibIfVLTrafficTable, ibIfPortStatHOQLifetimeDiscards=ibIfPortStatHOQLifetimeDiscards, ibIfVLOutOctets=ibIfVLOutOctets, ibIfMIB=ibIfMIB, ibIpoibLinkLayerIndex=ibIpoibLinkLayerIndex, ibIfPortStatInactDiscards=ibIfPortStatInactDiscards, ibIfVLTrafficEntry=ibIfVLTrafficEntry, PYSNMP_MODULE_ID=ibIfMIB, ibIfPortLinkDowned=ibIfPortLinkDowned, ibIfPortStatExcBufOverrunErrs=ibIfPortStatExcBufOverrunErrs, ibIfPortStatSwLifetimeDiscards=ibIfPortStatSwLifetimeDiscards, ibIfVLOutPkts=ibIfVLOutPkts, ibIfPortStatVL15Dropped=ibIfPortStatVL15Dropped, ibIpoibLinkLayerAddrTable=ibIpoibLinkLayerAddrTable, ibIfPortStatEntry=ibIfPortStatEntry, ibIfPortLinkErrRecovery=ibIfPortLinkErrRecovery, ibIfPortStatRcvRemPhyErrs=ibIfPortStatRcvRemPhyErrs, ibIfVLInPkts=ibIfVLInPkts, ibIfPortSymbolErrs=ibIfPortSymbolErrs, ibIfVLTrafficGroup=ibIfVLTrafficGroup, ibIfPortStatLocalPhyErrs=ibIfPortStatLocalPhyErrs, ibIfPortStatTable=ibIfPortStatTable, ibIpoibLinkLayerIfIndex=ibIpoibLinkLayerIfIndex, ibIfFullCompliance=ibIfFullCompliance, ibIfStatOptionalPortStatGroup=ibIfStatOptionalPortStatGroup)