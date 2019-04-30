#
# PySNMP MIB module SC5520-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SC5520-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:52:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
dsu, = mibBuilder.importSymbols("DDS-MIB", "dsu")
SCinstance, = mibBuilder.importSymbols("GDCMACRO-MIB", "SCinstance")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Counter64, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Gauge32, Bits, IpAddress, Integer32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Counter64", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Gauge32", "Bits", "IpAddress", "Integer32", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sc5520 = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3))
sc5520MIBversion = MibScalar((1, 3, 6, 1, 4, 1, 498, 8, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520MIBversion.setStatus('mandatory')
sc5520UnitCfgTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 2), )
if mibBuilder.loadTexts: sc5520UnitCfgTable.setStatus('mandatory')
sc5520UnitCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520UnitCfgIndex"))
if mibBuilder.loadTexts: sc5520UnitCfgEntry.setStatus('mandatory')
sc5520UnitCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520UnitCfgIndex.setStatus('mandatory')
sc5520Nms510CompatibilityMode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520Nms510CompatibilityMode.setStatus('mandatory')
sc5520PtToPtSentryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520PtToPtSentryTime.setStatus('mandatory')
sc5520AlarmHystTime = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520AlarmHystTime.setStatus('mandatory')
sc5520MtpointRmRspIntrvl = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 127))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520MtpointRmRspIntrvl.setStatus('mandatory')
sc5520DtePortType = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("rs232", 1), ("v35", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DtePortType.setStatus('mandatory')
sc5520DteCtsDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ctsOn", 1), ("cts0mSec", 2), ("ctsFixed3Char", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DteCtsDelay.setStatus('mandatory')
sc5520DteCtsDelayExt = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ext0mSec", 1), ("ext30mSec", 2), ("ext60mSec", 3), ("ext90mSec", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DteCtsDelayExt.setStatus('mandatory')
sc5520BkPlaneFracNum = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520BkPlaneFracNum.setStatus('mandatory')
sc5520BkPlaneFracIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("highway1", 2), ("highway2", 3), ("highway3", 4), ("highway4", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520BkPlaneFracIfIndex.setStatus('mandatory')
sc5520FirmwareLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520FirmwareLevel.setStatus('mandatory')
sc5520FrontPanelInhibit = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpInhibited", 1), ("fpEnabled", 2), ("execute", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520FrontPanelInhibit.setStatus('mandatory')
sc5520FrontPanelEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("fpInhibited", 1), ("fpEnabled", 2), ("execute", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520FrontPanelEnable.setStatus('mandatory')
sc5520RemLoopAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("inhibit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520RemLoopAllowed.setStatus('mandatory')
sc5520RemLoopPattern = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("patternV54", 1), ("patternPn127", 2), ("patternGDC", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520RemLoopPattern.setStatus('mandatory')
sc5520RemLoopTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inhibit", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520RemLoopTimeout.setStatus('mandatory')
sc5520HdlcInvert = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("invert", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520HdlcInvert.setStatus('mandatory')
sc5520EIARemLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520EIARemLoop.setStatus('mandatory')
sc5520EIALineLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520EIALineLoop.setStatus('mandatory')
sc5520PiggyBackDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("not-installed", 1), ("installed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520PiggyBackDetect.setStatus('mandatory')
sc5520RateBroadcast = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520RateBroadcast.setStatus('mandatory')
sc5520CircuitType = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("point-to-point", 1), ("multipoint", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520CircuitType.setStatus('mandatory')
sc5520WakeUpRemote = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520WakeUpRemote.setStatus('mandatory')
sc5520ListOfRemotes = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520ListOfRemotes.setStatus('mandatory')
sc5520TelcoLatchingLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("inhibit", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520TelcoLatchingLoop.setStatus('mandatory')
sc5520MasterTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 3), )
if mibBuilder.loadTexts: sc5520MasterTable.setStatus('mandatory')
sc5520MasterTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520MasterIndex"))
if mibBuilder.loadTexts: sc5520MasterTableEntry.setStatus('mandatory')
sc5520MasterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520MasterIndex.setStatus('mandatory')
sc5520AddRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(18, 18)).setFixedLength(18)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520AddRemoteAddress.setStatus('mandatory')
sc5520DelRemoteAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(18, 18)).setFixedLength(18)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DelRemoteAddress.setStatus('mandatory')
sc5520EnableRemoteAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520EnableRemoteAlarm.setStatus('mandatory')
sc5520DisableRemoteAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DisableRemoteAlarm.setStatus('mandatory')
sc5520EnableAllRemoteAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520EnableAllRemoteAlarms.setStatus('obsolete')
sc5520DisableAllRemoteAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DisableAllRemoteAlarms.setStatus('obsolete')
sc5520AlarmData = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4))
sc5520NoResponseAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 1))
sc5520DiagRxErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 2))
sc5520PowerUpAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 3))
sc5520EEChkSumErrAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 4))
sc5520FpTestAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 5))
sc5520DSRLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 7))
sc5520DTRLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 8))
sc5520DTPLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 9))
sc5520DCDLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 10))
sc5520RXDLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 11))
sc5520TXDLossAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 12))
sc5520TmShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 13))
sc5520DcdShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 14))
sc5520DsrShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 15))
sc5520CtsShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 16))
sc5520RxdShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 17))
sc5520RxcShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 18))
sc5520TxcShortedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 19))
sc5520DBURequestForScanAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 20))
sc5520DBUOnAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 21))
sc5520DBUFailedAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 22))
sc5520CSULoopbackAlm = MibIdentifier((1, 3, 6, 1, 4, 1, 498, 8, 3, 4, 23))
sc5520MaintTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 5), )
if mibBuilder.loadTexts: sc5520MaintTable.setStatus('mandatory')
sc5520MaintEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520MaintIndex"))
if mibBuilder.loadTexts: sc5520MaintEntry.setStatus('mandatory')
sc5520MaintIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520MaintIndex.setStatus('mandatory')
sc5520LedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520LedStatus.setStatus('mandatory')
sc5520SoftReset = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("normal", 1), ("reset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520SoftReset.setStatus('mandatory')
sc5520SysUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520SysUpTime.setStatus('mandatory')
sc5520PrivateStorage1 = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520PrivateStorage1.setStatus('mandatory')
sc5520PrivateStorage2 = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520PrivateStorage2.setStatus('mandatory')
sc5520PrivateStorage3 = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520PrivateStorage3.setStatus('mandatory')
sc5520BlinkINS = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("notBlinking", 1), ("blinking", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520BlinkINS.setStatus('mandatory')
sc5520DiagCfgTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 6), )
if mibBuilder.loadTexts: sc5520DiagCfgTable.setStatus('mandatory')
sc5520DiagCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520DiagCfgIndex"))
if mibBuilder.loadTexts: sc5520DiagCfgEntry.setStatus('mandatory')
sc5520DiagCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagCfgIndex.setStatus('mandatory')
sc5520DiagSendCode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("sc5520SendOtherPattern", 1), ("sc5520Send511Pattern", 2), ("sc5520Send2047Pattern", 3), ("sc5520Send15BitPattern", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagSendCode.setStatus('mandatory')
sc5520DiagTestExceptions = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noExceptions", 1), ("blocksOutOfRange", 2), ("bitsOutOfRange", 3), ("blocksAndBitsOutOfRange", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagTestExceptions.setStatus('mandatory')
sc5520DiagBitErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagBitErrors.setStatus('mandatory')
sc5520DiagBlockErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagBlockErrors.setStatus('mandatory')
sc5520DiagTestReset = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noTestActive", 1), ("testActive", 2), ("resetTest", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagTestReset.setStatus('mandatory')
sc5520DiagTimeDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagTimeDelay.setStatus('mandatory')
sc5520ExcDiagTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 7), )
if mibBuilder.loadTexts: sc5520ExcDiagTable.setStatus('mandatory')
sc5520ExcDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520ExcDiagIndex"))
if mibBuilder.loadTexts: sc5520ExcDiagEntry.setStatus('mandatory')
sc5520ExcDiagIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520ExcDiagIndex.setStatus('mandatory')
sc5520DiagExtLineloop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("lineloopOff", 1), ("lineloopOn", 2), ("external", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagExtLineloop.setStatus('mandatory')
sc5520DiagIntLineloop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("lineloopOff", 1), ("lineloopOn", 2), ("blocks1", 3), ("blocks10", 4), ("blocks100", 5), ("blocks500", 6), ("blocks1000", 7), ("blocks5000", 8), ("blocks10000", 9), ("blocks50000", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagIntLineloop.setStatus('mandatory')
sc5520DiagExtDataloop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("dataloopOff", 1), ("dataloopOn", 2), ("external", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagExtDataloop.setStatus('mandatory')
sc5520DiagTestStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noTest", 1), ("externalLineloop", 2), ("internalLineloop", 3), ("externalDataloop", 4), ("serviceTestCenterLoop", 5), ("endToend", 6), ("remoteLoop", 7), ("remoteLoopWithSelfTest", 8), ("networkDelay", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520DiagTestStatus.setStatus('mandatory')
sc5520DiagExtRemoteLoop = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("remoteloopOff", 1), ("remoteloopOn", 2), ("external", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagExtRemoteLoop.setStatus('mandatory')
sc5520DiagRemLoopWithSelf = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 7, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("remoteloopOff", 1), ("remoteloopOn", 2), ("blocks1", 3), ("blocks10", 4), ("blocks100", 5), ("blocks500", 6), ("blocks1000", 7), ("blocks5000", 8), ("blocks10000", 9), ("blocks50000", 10)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DiagRemLoopWithSelf.setStatus('mandatory')
sc5520VersionTable = MibTable((1, 3, 6, 1, 4, 1, 498, 8, 3, 8), )
if mibBuilder.loadTexts: sc5520VersionTable.setStatus('mandatory')
sc5520VersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1), ).setIndexNames((0, "SC5520-MIB", "sc5520VersionIndex"))
if mibBuilder.loadTexts: sc5520VersionEntry.setStatus('mandatory')
sc5520VersionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 1), SCinstance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520VersionIndex.setStatus('mandatory')
sc5520ActiveFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520ActiveFirmwareRev.setStatus('mandatory')
sc5520StoredFirmwareRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520StoredFirmwareRev.setStatus('mandatory')
sc5520BootRev = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520BootRev.setStatus('mandatory')
sc5520StoredFirmwareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("statBlank", 1), ("statDownLoading", 2), ("statOK", 3), ("statCheckSumBad", 4), ("statUnZipping", 5), ("statBadUnZip", 6), ("statDownloadAborted", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sc5520StoredFirmwareStatus.setStatus('mandatory')
sc5520SwitchActiveFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("switchNorm", 1), ("switchActive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520SwitchActiveFirmware.setStatus('mandatory')
sc5520DownloadingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 498, 8, 3, 8, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disableAll", 1), ("enableAndWait", 2), ("enableAndSwitch", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sc5520DownloadingMode.setStatus('mandatory')
mibBuilder.exportSymbols("SC5520-MIB", sc5520DiagBitErrors=sc5520DiagBitErrors, sc5520LedStatus=sc5520LedStatus, sc5520TelcoLatchingLoop=sc5520TelcoLatchingLoop, sc5520AlarmData=sc5520AlarmData, sc5520DcdShortedAlm=sc5520DcdShortedAlm, sc5520NoResponseAlm=sc5520NoResponseAlm, sc5520EnableAllRemoteAlarms=sc5520EnableAllRemoteAlarms, sc5520CSULoopbackAlm=sc5520CSULoopbackAlm, sc5520RemLoopPattern=sc5520RemLoopPattern, sc5520DTPLossAlm=sc5520DTPLossAlm, sc5520DsrShortedAlm=sc5520DsrShortedAlm, sc5520MasterTable=sc5520MasterTable, sc5520EIARemLoop=sc5520EIARemLoop, sc5520RemLoopAllowed=sc5520RemLoopAllowed, sc5520DTRLossAlm=sc5520DTRLossAlm, sc5520SysUpTime=sc5520SysUpTime, sc5520DteCtsDelay=sc5520DteCtsDelay, sc5520DiagCfgIndex=sc5520DiagCfgIndex, sc5520DiagTimeDelay=sc5520DiagTimeDelay, sc5520BkPlaneFracIfIndex=sc5520BkPlaneFracIfIndex, sc5520TmShortedAlm=sc5520TmShortedAlm, sc5520FirmwareLevel=sc5520FirmwareLevel, sc5520PrivateStorage2=sc5520PrivateStorage2, sc5520TXDLossAlm=sc5520TXDLossAlm, sc5520DtePortType=sc5520DtePortType, sc5520CircuitType=sc5520CircuitType, sc5520ExcDiagTable=sc5520ExcDiagTable, sc5520HdlcInvert=sc5520HdlcInvert, sc5520DBUFailedAlm=sc5520DBUFailedAlm, sc5520CtsShortedAlm=sc5520CtsShortedAlm, sc5520RateBroadcast=sc5520RateBroadcast, sc5520DBURequestForScanAlm=sc5520DBURequestForScanAlm, sc5520ExcDiagIndex=sc5520ExcDiagIndex, sc5520DownloadingMode=sc5520DownloadingMode, sc5520DiagTestReset=sc5520DiagTestReset, sc5520DiagSendCode=sc5520DiagSendCode, sc5520DiagCfgTable=sc5520DiagCfgTable, sc5520VersionIndex=sc5520VersionIndex, sc5520DisableRemoteAlarm=sc5520DisableRemoteAlarm, sc5520UnitCfgIndex=sc5520UnitCfgIndex, sc5520ExcDiagEntry=sc5520ExcDiagEntry, sc5520DiagIntLineloop=sc5520DiagIntLineloop, sc5520MasterTableEntry=sc5520MasterTableEntry, sc5520MaintTable=sc5520MaintTable, sc5520RemLoopTimeout=sc5520RemLoopTimeout, sc5520DiagExtRemoteLoop=sc5520DiagExtRemoteLoop, sc5520DiagExtDataloop=sc5520DiagExtDataloop, sc5520PrivateStorage1=sc5520PrivateStorage1, sc5520DteCtsDelayExt=sc5520DteCtsDelayExt, sc5520ActiveFirmwareRev=sc5520ActiveFirmwareRev, sc5520DCDLossAlm=sc5520DCDLossAlm, sc5520FrontPanelEnable=sc5520FrontPanelEnable, sc5520RxdShortedAlm=sc5520RxdShortedAlm, sc5520SoftReset=sc5520SoftReset, sc5520BlinkINS=sc5520BlinkINS, sc5520WakeUpRemote=sc5520WakeUpRemote, sc5520BootRev=sc5520BootRev, sc5520EEChkSumErrAlm=sc5520EEChkSumErrAlm, sc5520BkPlaneFracNum=sc5520BkPlaneFracNum, sc5520VersionTable=sc5520VersionTable, sc5520Nms510CompatibilityMode=sc5520Nms510CompatibilityMode, sc5520DiagExtLineloop=sc5520DiagExtLineloop, sc5520DiagRemLoopWithSelf=sc5520DiagRemLoopWithSelf, sc5520StoredFirmwareStatus=sc5520StoredFirmwareStatus, sc5520VersionEntry=sc5520VersionEntry, sc5520DBUOnAlm=sc5520DBUOnAlm, sc5520DiagCfgEntry=sc5520DiagCfgEntry, sc5520MaintEntry=sc5520MaintEntry, sc5520EnableRemoteAlarm=sc5520EnableRemoteAlarm, sc5520DiagRxErrAlm=sc5520DiagRxErrAlm, sc5520SwitchActiveFirmware=sc5520SwitchActiveFirmware, sc5520FpTestAlm=sc5520FpTestAlm, sc5520DisableAllRemoteAlarms=sc5520DisableAllRemoteAlarms, sc5520TxcShortedAlm=sc5520TxcShortedAlm, sc5520DiagTestStatus=sc5520DiagTestStatus, sc5520AlarmHystTime=sc5520AlarmHystTime, sc5520=sc5520, sc5520UnitCfgEntry=sc5520UnitCfgEntry, sc5520ListOfRemotes=sc5520ListOfRemotes, sc5520PtToPtSentryTime=sc5520PtToPtSentryTime, sc5520DiagTestExceptions=sc5520DiagTestExceptions, sc5520MaintIndex=sc5520MaintIndex, sc5520AddRemoteAddress=sc5520AddRemoteAddress, sc5520PowerUpAlm=sc5520PowerUpAlm, sc5520MIBversion=sc5520MIBversion, sc5520RxcShortedAlm=sc5520RxcShortedAlm, sc5520StoredFirmwareRev=sc5520StoredFirmwareRev, sc5520UnitCfgTable=sc5520UnitCfgTable, sc5520EIALineLoop=sc5520EIALineLoop, sc5520FrontPanelInhibit=sc5520FrontPanelInhibit, sc5520PiggyBackDetect=sc5520PiggyBackDetect, sc5520DiagBlockErrors=sc5520DiagBlockErrors, sc5520RXDLossAlm=sc5520RXDLossAlm, sc5520MtpointRmRspIntrvl=sc5520MtpointRmRspIntrvl, sc5520PrivateStorage3=sc5520PrivateStorage3, sc5520DelRemoteAddress=sc5520DelRemoteAddress, sc5520DSRLossAlm=sc5520DSRLossAlm, sc5520MasterIndex=sc5520MasterIndex)