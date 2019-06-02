#
# PySNMP MIB module Wellfleet-ACCT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Wellfleet-ACCT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:39:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Unsigned32, Gauge32, NotificationType, Bits, TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, NotificationType, ObjectIdentity, ModuleIdentity, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Unsigned32", "Gauge32", "NotificationType", "Bits", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Integer32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
wfAcctGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfAcctGroup")
class RtrTimeStamp(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

wfAcct = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1))
wfAcctCreate = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCreate.setDescription('Used to create or delete the Accounting Service. If set to deleted, the wfAcct instance will be deleted from the MIB and all accounting data will be deleted from the data table. No further snapshots of data will be collected until the Accounting Service is created.')
wfAcctEnable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctEnable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctEnable.setDescription('Used to enable or disable the Accounting Service. If the Accounting Service is disabled after it has been allowed to run for a period of time, the snapshots of accounting data currently in the data table will be maintained, however no further snapshots will be taken until the service is once again enabled.')
wfAcctOperState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2))).clone('down')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctOperState.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctOperState.setDescription('This field indicates the actual state of the Accounting Service. If up, the Accounting Service is currently running and collecting snapshots of data if accounting is configured on any interfaces and queues. If down, the Accounting Service is not running or collecting snapshots.')
wfAcctLogLevel = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2031616, 65536, 131072, 262144, 524288, 1048576, 917504))).clone(namedValues=NamedValues(("all", 2031616), ("debug", 65536), ("info", 131072), ("warning", 262144), ("fault", 524288), ("trace", 1048576), ("infofaultwarning", 917504))).clone('infofaultwarning')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctLogLevel.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctLogLevel.setDescription('Specifies the level of event log messages written to the log by the Accounting Service. To control level of log messages: DBG_MSG_ALL 0x001f0000 - 2031616 DBG_MSG_DEBUG 0x00010000 - 65536 DBG_MSG_INFO 0x00020000 - 131072 DBG_MSG_WARNING 0x00040000 - 262144 DBG_MSG_FAULT 0x00080000 - 524288 DBG_MSG_TRACE 0x00100000 - 1048576')
wfAcctCircularSnapshotFlag = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctCircularSnapshotFlag.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCircularSnapshotFlag.setDescription('This flag indicates whether the collection of snapshots for each interface and queue should act as a circular buffer. If enabled, when the maximum number of snapshots in memory is reached, the oldest snapshot will be deleted, and the next snapshot will be added. If disabled, when the maximum number of snapshots in memory is reached, the collection of snapshots will be maintained, however no new snapshots will be added.')
wfAcctCollectDuration = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctCollectDuration.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCollectDuration.setDescription('This values specifies the duration (in hours) over which the Accounting Service is to collect snapshots of accounting data taken at every wfAcctUpdateInterval activation. When the duration is reached, the collection of snapshots will function as described by the wfAcctCircularSnapshotFlag.')
wfAcctUpdateInterval = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 360)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctUpdateInterval.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctUpdateInterval.setDescription('Specifies the sampling interval (in minutes) at which the Accounting Service will update accounting data both internally and in the data table.')
wfAcctFlushOnRetrieval = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctFlushOnRetrieval.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctFlushOnRetrieval.setDescription('Enables or disables a data flush following export of the accounting data file. If enabled, the Accounting Service will clear all data both internally and in the MIB after the data file is tranported and start over at the next activation of wfAcctUpdateInterval. If disabled, the snapshots of accounting data will remain in memory until either the wfAcctFlushData attribute is set or until the maximum number of snapshots has been reached, at which point the collection of snapshots will function as described by the wfAcctCircularSnapshotFlag.')
wfAcctFlushData = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 1), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctFlushData.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctFlushData.setDescription('Causes the Accounting Service to flush data. When this attribute is set either to 0 or 1, the Accounting Service will immediately delete all snapshots both internally and in the MIB.')
wfAcctLastUpdateTimeStampHigh = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 10), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctLastUpdateTimeStampHigh.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctLastUpdateTimeStampHigh.setDescription('Time stamp (high 32 bits) of the last wfAcctUpdateInterval timer expiration. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctLastUpdateTimeStampLow = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 11), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctLastUpdateTimeStampLow.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctLastUpdateTimeStampLow.setDescription('Time stamp (low 32 bits) of the last wfAcctUpdateInterval timer expiration. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctLastFlushTimeStampHigh = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 12), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctLastFlushTimeStampHigh.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctLastFlushTimeStampHigh.setDescription('Time stamp (high 32 bits) of the last data flush, either invoked after transport of the data file when wfAcctFlushOnRetrieval is enabled, or by setting wfAcctFlushData to 0 or 1. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctLastFlushTimeStampLow = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 13), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctLastFlushTimeStampLow.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctLastFlushTimeStampLow.setDescription('Time stamp (low 32 bits) of the last data flush, either invoked after transport of the data file when wfAcctFlushOnRetrieval is enabled, or by setting wfAcctFlushData to 0 or 1. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctRuleNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctRuleNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleNumEntries.setDescription('The number of rule entries present in the wfAcctRuleTable.')
wfAcctCtrlNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctCtrlNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlNumEntries.setDescription('The number of control entries (regardless of their current state) present in the wfAcctCtrlTable.')
wfAcctDataNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataNumEntries.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataNumEntries.setDescription('The number of data entries present in the wfAcctDataTable.')
wfAcctRuleTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2), )
if mibBuilder.loadTexts: wfAcctRuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleTable.setDescription('Table containing rules which specify the type of statistics to collect.')
wfAcctRuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1), ).setIndexNames((0, "Wellfleet-ACCT-MIB", "wfAcctRuleNumber"))
if mibBuilder.loadTexts: wfAcctRuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleEntry.setDescription('The definition of a data collection rule.')
wfAcctRuleCreate = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctRuleCreate.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleCreate.setDescription('Creates or deletes a rule entry. If a deleted rule is referenced in one or more control table entries, the state of those control entries will be set to passive until a valid rule is specified.')
wfAcctRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctRuleNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleNumber.setDescription('The unique number for this rule.')
wfAcctRuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctRuleName.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleName.setDescription('The user-defined name of this rule.')
wfAcctRuleStatDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("in", 2), ("out", 3), ("both", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctRuleStatDirection.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleStatDirection.setDescription('Specifies the direction of traffic for which to collect statistics. If none, the data collection for this rule is effectively disabled. If in, ingress traffic will be used for data collection. If out, egress traffic will be used. If both, ingress and egress traffic will be used for data collection.')
wfAcctRuleStatCollect = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("octets", 1), ("packets", 2), ("all", 3))).clone('octets')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfAcctRuleStatCollect.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctRuleStatCollect.setDescription('Specifies which statistics to collect for this rule. If octets, octet statistics will be collected. If packets, packet statistics will be collected. If all, octet and packet statistics will be collected.')
wfAcctCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3), )
if mibBuilder.loadTexts: wfAcctCtrlTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlTable.setDescription('Read-only table which contains information about the particular rule from the wfAcctRuleTable which is being used in collecting statistics for a particular access interface and queue.')
wfAcctCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1), ).setIndexNames((0, "Wellfleet-ACCT-MIB", "wfAcctCtrlCctNum"), (0, "Wellfleet-ACCT-MIB", "wfAcctCtrlServicePkg"), (0, "Wellfleet-ACCT-MIB", "wfAcctCtrlQueueIndex"))
if mibBuilder.loadTexts: wfAcctCtrlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlEntry.setDescription('Control information for a particular queue on an access interface.')
wfAcctCtrlCctNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctCtrlCctNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlCctNum.setDescription('The circuit number of an access interface.')
wfAcctCtrlServicePkg = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctCtrlServicePkg.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlServicePkg.setDescription('The service package associated with the control entry.')
wfAcctCtrlQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctCtrlQueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlQueueIndex.setDescription('The queue index for which to collect statistics.')
wfAcctCtrlRuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctCtrlRuleNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctCtrlRuleNumber.setDescription('The number of the rule from the wfAcctRuleTable which will define the set of statistics to collect.')
wfAcctDataTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4), )
if mibBuilder.loadTexts: wfAcctDataTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataTable.setDescription('A list of data entries. The data table contains the snapshots taken at each sampling interval.')
wfAcctDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1), ).setIndexNames((0, "Wellfleet-ACCT-MIB", "wfAcctDataCctNum"), (0, "Wellfleet-ACCT-MIB", "wfAcctDataServicePkg"), (0, "Wellfleet-ACCT-MIB", "wfAcctDataQueueIndex"), (0, "Wellfleet-ACCT-MIB", "wfAcctDataTimeStampHigh"), (0, "Wellfleet-ACCT-MIB", "wfAcctDataTimeStampLow"))
if mibBuilder.loadTexts: wfAcctDataEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataEntry.setDescription('An entry containing accounting data for an interface on a per queue level.')
wfAcctDataCctNum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataCctNum.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataCctNum.setDescription('The circuit number of the access interface.')
wfAcctDataServicePkg = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataServicePkg.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataServicePkg.setDescription('The service package associated with the access interface.')
wfAcctDataQueueIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataQueueIndex.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataQueueIndex.setDescription('The queue for which the data was collected.')
wfAcctDataTimeStampHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 4), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataTimeStampHigh.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataTimeStampHigh.setDescription('Time stamp (high 32 bits) of the time when this snapshot of data was taken. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctDataTimeStampLow = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 5), RtrTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataTimeStampLow.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataTimeStampLow.setDescription('Time stamp (low 32 bits) of the time when this snapshot of data was taken. This value is the number of seconds since Jan. 1, 1970, 00:00 (GMT).')
wfAcctDataBitmask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctDataBitmask.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctDataBitmask.setDescription('Indicates which statistics were collected for this data entry, and whether there were any changes in the state of the interface since the last update interval expiration. Current bit definitions are: bit 31 bit 0 +--------------------------------+ | | +--------------------------------+ bit0 - wfAcctInBelowCirOctets bit1 - wfAcctInAboveCirOctets bit2 - wfAcctInAboveBrOctets bit3 - wfAcctInBelowCirPkts bit4 - wfAcctInAboveCirPkts bit5 - wfAcctInAboveBrPkts bit6 - wfAcctOutOctets bit7 - wfAcctOutPkts bits8-29 - reserved for future use bit30 - Interface is currently down bit31 - Interface is up, but was down during the current interval Bits 30 and 31 are intended to give an indication as to the current state of the interface and whether the interface state changed during the current interval. If bit 30 is set, the interface was down when statistics were requested, therefore all counter fields will be set to zero. If bit 31 is set, the interface was up when statistics were requested, however the state of the interface transitioned from down to up at some point during the interval, therefore statistics may have been lost.')
wfAcctInBelowCirOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInBelowCirOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInBelowCirOctets.setDescription('The number of octets received which were below the committed information rate (CIR).')
wfAcctInAboveCirOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInAboveCirOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInAboveCirOctets.setDescription('The number of octets received which exceeded the committed information rate, but which were within the allocated burst rate (BR).')
wfAcctInAboveBrOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInAboveBrOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInAboveBrOctets.setDescription('The number of octets received which exceeded the allocated burst rate (BR).')
wfAcctInBelowCirPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInBelowCirPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInBelowCirPkts.setDescription('The number of packets received which were below the committed information rate (CIR).')
wfAcctInAboveCirPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInAboveCirPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInAboveCirPkts.setDescription('The number of packets received which exceeded the committed information rate, but which were within the allocated burst rate (BR).')
wfAcctInAboveBrPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctInAboveBrPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctInAboveBrPkts.setDescription('The number of packets received which exceeded the allocated burst rate (BR).')
wfAcctOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctOutOctets.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctOutOctets.setDescription('The total number of octets transmitted.')
wfAcctOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2, 4, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfAcctOutPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfAcctOutPkts.setDescription('The total number of packets transmitted.')
wfAcctBufferFull = NotificationType((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 23, 2) + (0,1))
if mibBuilder.loadTexts: wfAcctBufferFull.setDescription('The wfAcctBufferFull trap indicates that the maximum number of snapshots has been reached and that the snapshot buffer will function as defined by the wfAcctCircularSnapshotFlag.')
mibBuilder.exportSymbols("Wellfleet-ACCT-MIB", wfAcctDataCctNum=wfAcctDataCctNum, wfAcctRuleStatCollect=wfAcctRuleStatCollect, wfAcctDataTimeStampLow=wfAcctDataTimeStampLow, wfAcctBufferFull=wfAcctBufferFull, wfAcctRuleName=wfAcctRuleName, wfAcctFlushData=wfAcctFlushData, wfAcctLastFlushTimeStampHigh=wfAcctLastFlushTimeStampHigh, wfAcctDataTable=wfAcctDataTable, wfAcctDataServicePkg=wfAcctDataServicePkg, wfAcctRuleEntry=wfAcctRuleEntry, wfAcctCtrlCctNum=wfAcctCtrlCctNum, wfAcctDataQueueIndex=wfAcctDataQueueIndex, wfAcctLastFlushTimeStampLow=wfAcctLastFlushTimeStampLow, wfAcctRuleCreate=wfAcctRuleCreate, wfAcctCircularSnapshotFlag=wfAcctCircularSnapshotFlag, wfAcctCtrlRuleNumber=wfAcctCtrlRuleNumber, wfAcctDataBitmask=wfAcctDataBitmask, wfAcctCtrlEntry=wfAcctCtrlEntry, wfAcctLastUpdateTimeStampHigh=wfAcctLastUpdateTimeStampHigh, wfAcctCtrlTable=wfAcctCtrlTable, wfAcctOperState=wfAcctOperState, wfAcctCtrlQueueIndex=wfAcctCtrlQueueIndex, wfAcctFlushOnRetrieval=wfAcctFlushOnRetrieval, wfAcctInAboveBrPkts=wfAcctInAboveBrPkts, wfAcctCtrlNumEntries=wfAcctCtrlNumEntries, wfAcctDataEntry=wfAcctDataEntry, wfAcctLastUpdateTimeStampLow=wfAcctLastUpdateTimeStampLow, wfAcctCreate=wfAcctCreate, wfAcctInAboveCirPkts=wfAcctInAboveCirPkts, wfAcctRuleTable=wfAcctRuleTable, wfAcctDataTimeStampHigh=wfAcctDataTimeStampHigh, wfAcctRuleNumEntries=wfAcctRuleNumEntries, wfAcctOutOctets=wfAcctOutOctets, wfAcctLogLevel=wfAcctLogLevel, wfAcctRuleStatDirection=wfAcctRuleStatDirection, wfAcctInAboveCirOctets=wfAcctInAboveCirOctets, RtrTimeStamp=RtrTimeStamp, wfAcct=wfAcct, wfAcctRuleNumber=wfAcctRuleNumber, wfAcctCtrlServicePkg=wfAcctCtrlServicePkg, wfAcctInBelowCirPkts=wfAcctInBelowCirPkts, wfAcctUpdateInterval=wfAcctUpdateInterval, wfAcctInBelowCirOctets=wfAcctInBelowCirOctets, wfAcctEnable=wfAcctEnable, wfAcctCollectDuration=wfAcctCollectDuration, wfAcctOutPkts=wfAcctOutPkts, wfAcctInAboveBrOctets=wfAcctInAboveBrOctets, wfAcctDataNumEntries=wfAcctDataNumEntries)