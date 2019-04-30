#
# PySNMP MIB module SNA-LLC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNA-LLC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:59:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ObjectIdentity, iso, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, TimeTicks, experimental, ModuleIdentity, Gauge32, Integer32, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "iso", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "TimeTicks", "experimental", "ModuleIdentity", "Gauge32", "Integer32", "Counter64", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString", "RowStatus")
snaDLCexp = MibIdentifier((1, 3, 6, 1, 3, 51))
llc = MibIdentifier((1, 3, 6, 1, 3, 51, 1))
llcPortGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 1))
llcSapGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 2))
llcCcGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 3))
llcTraps = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 4))
llcConformance = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5))
llcCompliances = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 1))
llcGroups = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2))
llcCoreGroups = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1))
llcPortAdminTable = MibTable((1, 3, 6, 1, 3, 51, 1, 1, 1), )
if mibBuilder.loadTexts: llcPortAdminTable.setStatus('mandatory')
llcPortAdminEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: llcPortAdminEntry.setStatus('mandatory')
llcPortAdminName = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminName.setStatus('mandatory')
llcPortAdminState = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminState.setStatus('mandatory')
llcPortAdminMaxIPDUOctetsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminMaxIPDUOctetsSend.setStatus('mandatory')
llcPortAdminMaxIPDUOctetsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminMaxIPDUOctetsRcv.setStatus('mandatory')
llcPortAdminMaxUnackedIPDUsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminMaxUnackedIPDUsSend.setStatus('mandatory')
llcPortAdminMaxUnackedIPDUsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminMaxUnackedIPDUsRcv.setStatus('mandatory')
llcPortAdminMaxRetransmits = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 7), Integer32().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminMaxRetransmits.setStatus('mandatory')
llcPortAdminAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 8), TimeTicks().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminAckTimer.setStatus('mandatory')
llcPortAdminPbitTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 9), TimeTicks().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminPbitTimer.setStatus('mandatory')
llcPortAdminRejTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 10), TimeTicks().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminRejTimer.setStatus('mandatory')
llcPortAdminBusyTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 11), TimeTicks().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminBusyTimer.setStatus('mandatory')
llcPortAdminInactTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 12), TimeTicks().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminInactTimer.setStatus('mandatory')
llcPortAdminDelayAckCount = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 13), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminDelayAckCount.setStatus('mandatory')
llcPortAdminDelayAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 14), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminDelayAckTimer.setStatus('mandatory')
llcPortAdminSimRim = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2))).clone('no')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcPortAdminSimRim.setStatus('mandatory')
llcPortOperTable = MibTable((1, 3, 6, 1, 3, 51, 1, 1, 2), )
if mibBuilder.loadTexts: llcPortOperTable.setStatus('mandatory')
llcPortOperEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: llcPortOperEntry.setStatus('mandatory')
llcPortOperName = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortOperName.setStatus('mandatory')
llcPortOperISTATUS = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortOperISTATUS.setStatus('mandatory')
llcPortOperLastModifyTime = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortOperLastModifyTime.setStatus('mandatory')
llcPortOperLastFailTime = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortOperLastFailTime.setStatus('mandatory')
llcPortOperLastFailCause = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("undefined", 1), ("physical", 2))).clone('undefined')).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortOperLastFailCause.setStatus('mandatory')
llcPortStatsTable = MibTable((1, 3, 6, 1, 3, 51, 1, 1, 3), )
if mibBuilder.loadTexts: llcPortStatsTable.setStatus('mandatory')
llcPortStatsEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: llcPortStatsEntry.setStatus('mandatory')
llcPortStatsPhysicalFailures = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsPhysicalFailures.setStatus('mandatory')
llcPortStatsPollsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsPollsIn.setStatus('mandatory')
llcPortStatsPollsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsPollsOut.setStatus('mandatory')
llcPortStatsPollRspsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsPollRspsIn.setStatus('mandatory')
llcPortStatsPollRspsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsPollRspsOut.setStatus('mandatory')
llcPortStatsLocalBusies = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsLocalBusies.setStatus('mandatory')
llcPortStatsRemoteBusies = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsRemoteBusies.setStatus('mandatory')
llcPortStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsIFramesIn.setStatus('mandatory')
llcPortStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsIFramesOut.setStatus('mandatory')
llcPortStatsOctetsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsOctetsIn.setStatus('mandatory')
llcPortStatsOctetsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsOctetsOut.setStatus('mandatory')
llcPortStatsProtocolErrs = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsProtocolErrs.setStatus('mandatory')
llcPortStatsActivityTOs = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsActivityTOs.setStatus('mandatory')
llcPortStatsRetriesExps = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsRetriesExps.setStatus('mandatory')
llcPortStatsRetransmitsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsRetransmitsIn.setStatus('mandatory')
llcPortStatsRetransmitsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 1, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcPortStatsRetransmitsOut.setStatus('mandatory')
llcSapAdminTable = MibTable((1, 3, 6, 1, 3, 51, 1, 2, 1), )
if mibBuilder.loadTexts: llcSapAdminTable.setStatus('mandatory')
llcSapAdminEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcSapNumber"))
if mibBuilder.loadTexts: llcSapAdminEntry.setStatus('mandatory')
llcSapNumber = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapNumber.setStatus('mandatory')
llcSapAdminState = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminState.setStatus('mandatory')
llcSapAdminMaxIPDUOctetsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminMaxIPDUOctetsSend.setStatus('mandatory')
llcSapAdminMaxIPDUOctetsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminMaxIPDUOctetsRcv.setStatus('mandatory')
llcSapAdminMaxUnackedIPDUsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminMaxUnackedIPDUsSend.setStatus('mandatory')
llcSapAdminMaxUnackedIPDUsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminMaxUnackedIPDUsRcv.setStatus('mandatory')
llcSapAdminMaxRetransmits = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminMaxRetransmits.setStatus('mandatory')
llcSapAdminAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 8), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminAckTimer.setStatus('mandatory')
llcSapAdminPbitTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 9), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminPbitTimer.setStatus('mandatory')
llcSapAdminRejTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminRejTimer.setStatus('mandatory')
llcSapAdminBusyTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 11), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminBusyTimer.setStatus('mandatory')
llcSapAdminInactTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 12), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminInactTimer.setStatus('mandatory')
llcSapAdminDelayAckCount = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminDelayAckCount.setStatus('mandatory')
llcSapAdminDelayAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 1, 1, 14), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcSapAdminDelayAckTimer.setStatus('mandatory')
llcSapOperTable = MibTable((1, 3, 6, 1, 3, 51, 1, 2, 2), )
if mibBuilder.loadTexts: llcSapOperTable.setStatus('mandatory')
llcSapOperEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcSapNumber"))
if mibBuilder.loadTexts: llcSapOperEntry.setStatus('mandatory')
llcSapOperStatus = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapOperStatus.setStatus('mandatory')
llcSapStatsTable = MibTable((1, 3, 6, 1, 3, 51, 1, 2, 3), )
if mibBuilder.loadTexts: llcSapStatsTable.setStatus('mandatory')
llcSapStatsEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcSapNumber"))
if mibBuilder.loadTexts: llcSapStatsEntry.setStatus('mandatory')
llcSapStatsTESTsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsTESTsIn.setStatus('mandatory')
llcSapStatsTESTsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsTESTsOut.setStatus('mandatory')
llcSapStatsXIDsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsXIDsIn.setStatus('mandatory')
llcSapStatsXIDsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsXIDsOut.setStatus('mandatory')
llcSapStatsUIFramesIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsUIFramesIn.setStatus('mandatory')
llcSapStatsUIFramesOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 2, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcSapStatsUIFramesOut.setStatus('mandatory')
llcCcAdminTable = MibTable((1, 3, 6, 1, 3, 51, 1, 3, 1), )
if mibBuilder.loadTexts: llcCcAdminTable.setStatus('mandatory')
llcCcAdminEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcCcLSap"), (0, "SNA-LLC-MIB", "llcCcRSap"), (0, "SNA-LLC-MIB", "llcCcRMac"), (0, "SNA-LLC-MIB", "llcCcLMac"))
if mibBuilder.loadTexts: llcCcAdminEntry.setStatus('mandatory')
llcCcLSap = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcLSap.setStatus('mandatory')
llcCcRSap = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcRSap.setStatus('mandatory')
llcCcLMac = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcLMac.setStatus('mandatory')
llcCcRMac = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcRMac.setStatus('mandatory')
llcCcAdminState = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminState.setStatus('mandatory')
llcCcAdminMaxIPDUOctetsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminMaxIPDUOctetsSend.setStatus('mandatory')
llcCcAdminMaxIPDUOctetsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminMaxIPDUOctetsRcv.setStatus('mandatory')
llcCcAdminMaxUnackedIPDUsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminMaxUnackedIPDUsSend.setStatus('mandatory')
llcCcAdminMaxUnackedIPDUsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminMaxUnackedIPDUsRcv.setStatus('mandatory')
llcCcAdminMaxRetransmits = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminMaxRetransmits.setStatus('mandatory')
llcCcAdminAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 11), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminAckTimer.setStatus('mandatory')
llcCcAdminPbitTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 12), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminPbitTimer.setStatus('mandatory')
llcCcAdminRejTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 13), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminRejTimer.setStatus('mandatory')
llcCcAdminBusyTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 14), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminBusyTimer.setStatus('mandatory')
llcCcAdminInactTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 15), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminInactTimer.setStatus('mandatory')
llcCcAdminDelayAckCount = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminDelayAckCount.setStatus('mandatory')
llcCcAdminDelayAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 17), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminDelayAckTimer.setStatus('mandatory')
llcCcAdminRowStatus = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 1, 1, 18), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcAdminRowStatus.setStatus('mandatory')
llcCcOperTable = MibTable((1, 3, 6, 1, 3, 51, 1, 3, 2), )
if mibBuilder.loadTexts: llcCcOperTable.setStatus('mandatory')
llcCcOperEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcCcLSap"), (0, "SNA-LLC-MIB", "llcCcRSap"), (0, "SNA-LLC-MIB", "llcCcRMac"), (0, "SNA-LLC-MIB", "llcCcLMac"))
if mibBuilder.loadTexts: llcCcOperEntry.setStatus('mandatory')
llcCcOperRole = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("undefined", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperRole.setStatus('mandatory')
llcCcOperState = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("discontacted", 1), ("contactPending", 2), ("contacted", 3), ("discontactPending", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperState.setStatus('mandatory')
llcCcOperMaxIPDUOctetsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperMaxIPDUOctetsSend.setStatus('mandatory')
llcCcOperMaxIPDUOctetsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperMaxIPDUOctetsRcv.setStatus('mandatory')
llcCcOperMaxUnackedIPDUsSend = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperMaxUnackedIPDUsSend.setStatus('mandatory')
llcCcOperMaxUnackedIPDUsRcv = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperMaxUnackedIPDUsRcv.setStatus('mandatory')
llcCcOperMaxRetransmits = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperMaxRetransmits.setStatus('mandatory')
llcCcOperAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 8), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperAckTimer.setStatus('mandatory')
llcCcOperPbitTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 9), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperPbitTimer.setStatus('mandatory')
llcCcOperRejTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 10), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperRejTimer.setStatus('mandatory')
llcCcOperBusyTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 11), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperBusyTimer.setStatus('mandatory')
llcCcOperInactTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 12), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperInactTimer.setStatus('mandatory')
llcCcOperDelayAckCount = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperDelayAckCount.setStatus('mandatory')
llcCcOperDelayAckTimer = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 14), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: llcCcOperDelayAckTimer.setStatus('mandatory')
llcCcOperCreateTime = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 15), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperCreateTime.setStatus('mandatory')
llcCcOperLastModifyTime = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperLastModifyTime.setStatus('mandatory')
llcCcOperLastFailTime = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 17), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperLastFailTime.setStatus('mandatory')
llcCcOperLastFailCause = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("undefined", 1), ("rxFRMR", 2), ("txFRMR", 3), ("noResponse", 4), ("protocolErr", 5), ("noActivity", 6), ("discReceived", 7), ("dmReceived", 8), ("retriesExpired", 9))).clone('undefined')).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperLastFailCause.setStatus('mandatory')
llcCcOperLastFailFRMRInfo = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 2, 1, 19), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcOperLastFailFRMRInfo.setStatus('mandatory')
llcCcStatsTable = MibTable((1, 3, 6, 1, 3, 51, 1, 3, 3), )
if mibBuilder.loadTexts: llcCcStatsTable.setStatus('mandatory')
llcCcStatsEntry = MibTableRow((1, 3, 6, 1, 3, 51, 1, 3, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SNA-LLC-MIB", "llcCcLSap"), (0, "SNA-LLC-MIB", "llcCcRSap"), (0, "SNA-LLC-MIB", "llcCcRMac"), (0, "SNA-LLC-MIB", "llcCcLMac"))
if mibBuilder.loadTexts: llcCcStatsEntry.setStatus('mandatory')
llcCcStatsLocalBusies = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsLocalBusies.setStatus('mandatory')
llcCcStatsRemoteBusies = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsRemoteBusies.setStatus('mandatory')
llcCcStatsIFramesIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsIFramesIn.setStatus('mandatory')
llcCcStatsIFramesOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsIFramesOut.setStatus('mandatory')
llcCcStatsIOctetsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsIOctetsIn.setStatus('mandatory')
llcCcStatsIOctetsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsIOctetsOut.setStatus('mandatory')
llcCcStatsREJsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsREJsIn.setStatus('mandatory')
llcCcStatsREJsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsREJsOut.setStatus('mandatory')
llcCcStatsRetransmitsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsRetransmitsIn.setStatus('mandatory')
llcCcStatsRetransmitsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsRetransmitsOut.setStatus('mandatory')
llcCcStatsFRMRsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsFRMRsIn.setStatus('mandatory')
llcCcStatsFRMRsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsFRMRsOut.setStatus('mandatory')
llcCcStatsDISCsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsDISCsIn.setStatus('mandatory')
llcCcStatsDISCsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsDISCsOut.setStatus('mandatory')
llcCcStatsUAsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsUAsIn.setStatus('mandatory')
llcCcStatsUAsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsUAsOut.setStatus('mandatory')
llcCcStatsDMsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsDMsIn.setStatus('mandatory')
llcCcStatsDMsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsDMsOut.setStatus('mandatory')
llcCcStatsSABMEsIn = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsSABMEsIn.setStatus('mandatory')
llcCcStatsSABMEsOut = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsSABMEsOut.setStatus('mandatory')
llcCcStatsProtocolErrs = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsProtocolErrs.setStatus('mandatory')
llcCcStatsActivityTOs = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsActivityTOs.setStatus('mandatory')
llcCcStatsRetriesExps = MibTableColumn((1, 3, 6, 1, 3, 51, 1, 3, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: llcCcStatsRetriesExps.setStatus('mandatory')
llcPortStatusChange = NotificationType((1, 3, 6, 1, 3, 51, 1, 4) + (0,1)).setObjects(("SNA-LLC-MIB", "llcPortOperLastFailTime"), ("SNA-LLC-MIB", "llcPortOperLastFailCause"))
llcCcStatusChange = NotificationType((1, 3, 6, 1, 3, 51, 1, 4) + (0,2)).setObjects(("SNA-LLC-MIB", "llcCcOperState"), ("SNA-LLC-MIB", "llcCcAdminState"), ("SNA-LLC-MIB", "llcCcOperLastFailTime"), ("SNA-LLC-MIB", "llcCcOperLastFailCause"), ("SNA-LLC-MIB", "llcCcOperLastFailFRMRInfo"))
llcCorePortAdminGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 1))
llcCorePortOperGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 2))
llcCorePortStatsGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 3))
llcCoreCcAdminGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 4))
llcCoreCcOperGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 5))
llcCoreCcStatsGroup = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 2, 1, 6))
llcCoreCompliance = MibIdentifier((1, 3, 6, 1, 3, 51, 1, 5, 1, 1))
mibBuilder.exportSymbols("SNA-LLC-MIB", llcPortOperTable=llcPortOperTable, llcCcStatsIOctetsOut=llcCcStatsIOctetsOut, llcCcOperTable=llcCcOperTable, llcCcStatsIFramesOut=llcCcStatsIFramesOut, llcSapAdminAckTimer=llcSapAdminAckTimer, llcTraps=llcTraps, llcSapStatsTESTsIn=llcSapStatsTESTsIn, llcCcStatsUAsOut=llcCcStatsUAsOut, llcPortStatsRemoteBusies=llcPortStatsRemoteBusies, llcPortAdminEntry=llcPortAdminEntry, llcPortStatsPollRspsOut=llcPortStatsPollRspsOut, llcSapGroup=llcSapGroup, llcCcOperDelayAckTimer=llcCcOperDelayAckTimer, llcPortOperLastFailTime=llcPortOperLastFailTime, llcCompliances=llcCompliances, llcPortAdminMaxIPDUOctetsRcv=llcPortAdminMaxIPDUOctetsRcv, llcCcStatsIOctetsIn=llcCcStatsIOctetsIn, llcPortStatsPollsOut=llcPortStatsPollsOut, llcSapStatsTable=llcSapStatsTable, llcPortAdminMaxIPDUOctetsSend=llcPortAdminMaxIPDUOctetsSend, llcCcStatsTable=llcCcStatsTable, llcCcAdminDelayAckTimer=llcCcAdminDelayAckTimer, llcSapStatsTESTsOut=llcSapStatsTESTsOut, llcCcLMac=llcCcLMac, llcCcOperState=llcCcOperState, llcSapNumber=llcSapNumber, llcPortOperName=llcPortOperName, llcCcOperBusyTimer=llcCcOperBusyTimer, llcCcStatsRetransmitsIn=llcCcStatsRetransmitsIn, llcPortStatsRetransmitsIn=llcPortStatsRetransmitsIn, llcCcOperMaxUnackedIPDUsRcv=llcCcOperMaxUnackedIPDUsRcv, llcSapAdminEntry=llcSapAdminEntry, llcCcAdminAckTimer=llcCcAdminAckTimer, llcSapOperEntry=llcSapOperEntry, llcPortAdminMaxUnackedIPDUsRcv=llcPortAdminMaxUnackedIPDUsRcv, llcPortAdminPbitTimer=llcPortAdminPbitTimer, llcPortStatsEntry=llcPortStatsEntry, llcPortStatsIFramesIn=llcPortStatsIFramesIn, llcPortStatsTable=llcPortStatsTable, llcCcAdminState=llcCcAdminState, llcSapAdminDelayAckCount=llcSapAdminDelayAckCount, llcCcOperInactTimer=llcCcOperInactTimer, llcCcStatsActivityTOs=llcCcStatsActivityTOs, llcPortStatusChange=llcPortStatusChange, llcCcStatsUAsIn=llcCcStatsUAsIn, llcSapStatsEntry=llcSapStatsEntry, llcPortAdminAckTimer=llcPortAdminAckTimer, llcPortOperLastModifyTime=llcPortOperLastModifyTime, llcCcOperMaxIPDUOctetsSend=llcCcOperMaxIPDUOctetsSend, llcPortAdminDelayAckCount=llcPortAdminDelayAckCount, llcSapAdminPbitTimer=llcSapAdminPbitTimer, llcCcStatusChange=llcCcStatusChange, llcPortAdminDelayAckTimer=llcPortAdminDelayAckTimer, llcCcOperRole=llcCcOperRole, llcPortAdminRejTimer=llcPortAdminRejTimer, llcCcAdminMaxIPDUOctetsRcv=llcCcAdminMaxIPDUOctetsRcv, llcPortStatsPollRspsIn=llcPortStatsPollRspsIn, llcCcOperEntry=llcCcOperEntry, llcSapAdminState=llcSapAdminState, llcCcStatsDMsIn=llcCcStatsDMsIn, llcSapStatsUIFramesIn=llcSapStatsUIFramesIn, llcPortAdminInactTimer=llcPortAdminInactTimer, llcCcAdminBusyTimer=llcCcAdminBusyTimer, llcCorePortOperGroup=llcCorePortOperGroup, llcSapAdminMaxIPDUOctetsRcv=llcSapAdminMaxIPDUOctetsRcv, llcCcRMac=llcCcRMac, llcCcOperRejTimer=llcCcOperRejTimer, llcCoreCompliance=llcCoreCompliance, llcCcStatsDISCsOut=llcCcStatsDISCsOut, llcPortStatsProtocolErrs=llcPortStatsProtocolErrs, llcSapOperTable=llcSapOperTable, llcCoreCcAdminGroup=llcCoreCcAdminGroup, llcCcStatsRemoteBusies=llcCcStatsRemoteBusies, llcCorePortStatsGroup=llcCorePortStatsGroup, llcPortGroup=llcPortGroup, llcPortStatsOctetsIn=llcPortStatsOctetsIn, llcSapAdminDelayAckTimer=llcSapAdminDelayAckTimer, llcCcAdminMaxIPDUOctetsSend=llcCcAdminMaxIPDUOctetsSend, llcPortStatsIFramesOut=llcPortStatsIFramesOut, llcCcOperAckTimer=llcCcOperAckTimer, llcSapAdminRejTimer=llcSapAdminRejTimer, llcPortStatsPollsIn=llcPortStatsPollsIn, llcCcOperLastFailCause=llcCcOperLastFailCause, llcCcStatsRetransmitsOut=llcCcStatsRetransmitsOut, llc=llc, llcPortStatsOctetsOut=llcPortStatsOctetsOut, llcCcAdminMaxUnackedIPDUsRcv=llcCcAdminMaxUnackedIPDUsRcv, llcCcStatsRetriesExps=llcCcStatsRetriesExps, llcCcStatsSABMEsIn=llcCcStatsSABMEsIn, llcPortStatsRetransmitsOut=llcPortStatsRetransmitsOut, llcCcStatsEntry=llcCcStatsEntry, llcCoreCcOperGroup=llcCoreCcOperGroup, llcGroups=llcGroups, llcCcAdminRejTimer=llcCcAdminRejTimer, llcSapAdminMaxUnackedIPDUsRcv=llcSapAdminMaxUnackedIPDUsRcv, llcCcOperMaxRetransmits=llcCcOperMaxRetransmits, llcSapAdminMaxIPDUOctetsSend=llcSapAdminMaxIPDUOctetsSend, llcPortAdminMaxRetransmits=llcPortAdminMaxRetransmits, llcCcAdminPbitTimer=llcCcAdminPbitTimer, llcConformance=llcConformance, llcPortAdminTable=llcPortAdminTable, llcPortAdminMaxUnackedIPDUsSend=llcPortAdminMaxUnackedIPDUsSend, llcCcOperPbitTimer=llcCcOperPbitTimer, llcCcStatsFRMRsIn=llcCcStatsFRMRsIn, llcPortStatsPhysicalFailures=llcPortStatsPhysicalFailures, llcCcAdminMaxRetransmits=llcCcAdminMaxRetransmits, llcPortStatsActivityTOs=llcPortStatsActivityTOs, llcCcAdminInactTimer=llcCcAdminInactTimer, llcCcAdminRowStatus=llcCcAdminRowStatus, llcSapAdminInactTimer=llcSapAdminInactTimer, llcPortAdminName=llcPortAdminName, llcSapAdminBusyTimer=llcSapAdminBusyTimer, llcCcStatsREJsIn=llcCcStatsREJsIn, snaDLCexp=snaDLCexp, llcPortAdminBusyTimer=llcPortAdminBusyTimer, llcCorePortAdminGroup=llcCorePortAdminGroup, llcSapOperStatus=llcSapOperStatus, llcCcAdminDelayAckCount=llcCcAdminDelayAckCount, llcCcOperDelayAckCount=llcCcOperDelayAckCount, llcCcGroup=llcCcGroup, llcCcStatsREJsOut=llcCcStatsREJsOut, llcSapAdminMaxRetransmits=llcSapAdminMaxRetransmits, llcCcStatsDMsOut=llcCcStatsDMsOut, llcCcOperCreateTime=llcCcOperCreateTime, llcCoreCcStatsGroup=llcCoreCcStatsGroup, llcPortStatsLocalBusies=llcPortStatsLocalBusies, llcSapStatsXIDsOut=llcSapStatsXIDsOut, llcPortOperEntry=llcPortOperEntry, llcCcLSap=llcCcLSap, llcSapAdminMaxUnackedIPDUsSend=llcSapAdminMaxUnackedIPDUsSend, llcPortAdminSimRim=llcPortAdminSimRim, llcCcOperMaxUnackedIPDUsSend=llcCcOperMaxUnackedIPDUsSend, llcPortStatsRetriesExps=llcPortStatsRetriesExps, llcCcAdminEntry=llcCcAdminEntry, llcCcStatsSABMEsOut=llcCcStatsSABMEsOut, llcCcAdminTable=llcCcAdminTable, llcCcOperLastFailTime=llcCcOperLastFailTime, llcCcOperMaxIPDUOctetsRcv=llcCcOperMaxIPDUOctetsRcv, llcSapStatsUIFramesOut=llcSapStatsUIFramesOut, llcCcStatsDISCsIn=llcCcStatsDISCsIn, llcCcAdminMaxUnackedIPDUsSend=llcCcAdminMaxUnackedIPDUsSend, llcSapAdminTable=llcSapAdminTable, llcCcStatsIFramesIn=llcCcStatsIFramesIn, llcPortOperISTATUS=llcPortOperISTATUS, llcCoreGroups=llcCoreGroups, llcCcOperLastModifyTime=llcCcOperLastModifyTime, llcCcRSap=llcCcRSap, llcPortOperLastFailCause=llcPortOperLastFailCause, llcCcOperLastFailFRMRInfo=llcCcOperLastFailFRMRInfo, llcCcStatsProtocolErrs=llcCcStatsProtocolErrs, llcPortAdminState=llcPortAdminState, llcSapStatsXIDsIn=llcSapStatsXIDsIn, llcCcStatsFRMRsOut=llcCcStatsFRMRsOut, llcCcStatsLocalBusies=llcCcStatsLocalBusies)