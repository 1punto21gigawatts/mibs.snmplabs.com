#
# PySNMP MIB module NMS-EPON-OAM-REMOTE-LOOPBACK (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NMS-EPON-OAM-REMOTE-LOOPBACK
# Produced by pysmi-0.3.4 at Mon Apr 29 20:11:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
llidIfIndex, = mibBuilder.importSymbols("NMS-EPON-LLID", "llidIfIndex")
nmsEPONGroup, = mibBuilder.importSymbols("NMS-SMI", "nmsEPONGroup")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, TimeTicks, IpAddress, MibIdentifier, Integer32, Counter32, Counter64, Bits, ModuleIdentity, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "IpAddress", "MibIdentifier", "Integer32", "Counter32", "Counter64", "Bits", "ModuleIdentity", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso")
TextualConvention, PhysAddress, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "PhysAddress", "DisplayString", "RowStatus")
nmsEponOltOamRemoteLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3))
nmsEponOltOamRemoteLoopbackTable = MibTable((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1), )
if mibBuilder.loadTexts: nmsEponOltOamRemoteLoopbackTable.setStatus('mandatory')
nmsEponOltOamRemoteLoopbackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1), ).setIndexNames((0, "NMS-EPON-LLID", "llidIfIndex"))
if mibBuilder.loadTexts: nmsEponOltOamRemoteLoopbackEntry.setStatus('mandatory')
oltTxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(64, 1518))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oltTxFrameSize.setStatus('mandatory')
oltTxFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oltTxFrameCount.setStatus('mandatory')
oltRxFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltRxFrameCount.setStatus('mandatory')
oltOutOfSequenceFrameCount = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltOutOfSequenceFrameCount.setStatus('mandatory')
oltLossPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltLossPercentage.setStatus('mandatory')
oltMinRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltMinRtt.setStatus('mandatory')
oltAverageRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltAverageRtt.setStatus('mandatory')
oltMaxRtt = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oltMaxRtt.setStatus('mandatory')
oltLoopbackRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11606, 10, 101, 3, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: oltLoopbackRowStatus.setStatus('mandatory')
mibBuilder.exportSymbols("NMS-EPON-OAM-REMOTE-LOOPBACK", nmsEponOltOamRemoteLoopbackTable=nmsEponOltOamRemoteLoopbackTable, oltMinRtt=oltMinRtt, oltTxFrameCount=oltTxFrameCount, oltLossPercentage=oltLossPercentage, nmsEponOltOamRemoteLoopback=nmsEponOltOamRemoteLoopback, oltRxFrameCount=oltRxFrameCount, oltTxFrameSize=oltTxFrameSize, oltLoopbackRowStatus=oltLoopbackRowStatus, oltAverageRtt=oltAverageRtt, oltOutOfSequenceFrameCount=oltOutOfSequenceFrameCount, oltMaxRtt=oltMaxRtt, nmsEponOltOamRemoteLoopbackEntry=nmsEponOltOamRemoteLoopbackEntry)